import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Constants and parameters
H0 = 67 * 1e3 / (3.086e22)  # H0 in s^-1
Omega_r0 = 1e-4
Omega_m0 = 0.3
Omega_Lambda = 1 - Omega_r0 - Omega_m0
a_start, a_end = 1e-4, 1.0
k_values = [H0, 5 * H0, 20 * H0, 200 * H0]

# Define H(a)
def H(a):
    return H0 * np.sqrt(Omega_m0 * a**-3 + Omega_r0 * a**-4 + Omega_Lambda)

# Define the system of equations
def perturbation_eqs(a, y, k):
    delta, theta = y
    H_a = H(a)
    d_delta = -theta
    d_theta = -H_a * theta + 1.5 * H0**2 * Omega_m0 * a**-3 * delta / (k**2 / a**2)
    return [d_delta, d_theta]

# Initial conditions
delta_0 = 1e-5
theta_0 = 0
initial_conditions = [delta_0, theta_0]

# Solve and plot for each k
fig, ax = plt.subplots(figsize=(10, 6))

for k in k_values:
    solution = solve_ivp(perturbation_eqs, [a_start, a_end], initial_conditions, args=(k,),
                         t_eval=np.logspace(np.log10(a_start), np.log10(a_end), 500))
    a_vals = solution.t
    delta_vals = solution.y[0]
    ax.plot(a_vals, delta_vals, label=f'$k = {k / H0:.0f} H_0$')

ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlabel(r"$a$", fontsize=14)
ax.set_ylabel(r"$\delta(a)$", fontsize=14)
ax.set_title("Matter Density Contrast for Different Scales in $\Lambda$CDM", fontsize=16)
ax.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.show()
