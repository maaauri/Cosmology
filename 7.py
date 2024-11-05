import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Constants
H0 = 70  # Hubble constant in km/s/Mpc
Omega_r = 5e-5  # Radiation density today

# Function to compute E(z) including Omega_r
def E_with_r(z, Omega_m, Omega_Lambda, Omega_K, Omega_r):
    return np.sqrt(Omega_r * (1 + z)**4 + Omega_m * (1 + z)**3 + Omega_K * (1 + z)**2 + Omega_Lambda)

# Function to compute comoving distance chi(z) with radiation
def chi_with_r(z, Omega_m, Omega_Lambda, Omega_r):
    Omega_K = 1 - Omega_m - Omega_Lambda - Omega_r
    integral, _ = quad(lambda z_: 1 / (H0 * E_with_r(z_, Omega_m, Omega_Lambda, Omega_K, Omega_r)), 0, z)
    return integral

# Function to compute f_K(chi) based on curvature
def f_K(chi, Omega_m, Omega_Lambda):
    Omega_K = 1 - Omega_m - Omega_Lambda - Omega_r
    if Omega_K > 0:
        return (1 / H0) / np.sqrt(Omega_K) * np.sinh(np.sqrt(Omega_K) * chi)
    elif Omega_K == 0:
        return (1 / H0) * chi
    else:
        return (1 / H0) / np.sqrt(-Omega_K) * np.sin(np.sqrt(-Omega_K) * chi)

# Grid of Omega_m and Omega_Lambda values
Omega_m_vals = np.linspace(0.1, 0.6, 100)
Omega_Lambda_vals = np.linspace(0.4, 0.9, 100)

# Initialize the grid for f_K with Omega_r included
fK_vals_r = np.zeros((len(Omega_m_vals), len(Omega_Lambda_vals)))

# Compute f_K for each pair of Omega_m and Omega_Lambda with radiation density
z = 1  # fixed redshift for the plot
for i, Omega_m in enumerate(Omega_m_vals):
    for j, Omega_Lambda in enumerate(Omega_Lambda_vals):
        chi_z_r = chi_with_r(z, Omega_m, Omega_Lambda, Omega_r)
        fK_vals_r[i, j] = f_K(chi_z_r, Omega_m, Omega_Lambda)

# Plot the updated results with Omega_r
plt.figure(figsize=(8, 6))
cs_r = plt.contour(Omega_m_vals, Omega_Lambda_vals, fK_vals_r.T, levels=10)
plt.clabel(cs_r, inline=1, fontsize=10)
plt.title(r'Lines of Constant $f_K(\chi)$ in $\Omega_m - \Omega_\Lambda$ Plane (with $\Omega_r$) at z = 1')
plt.xlabel(r'$\Omega_m$')
plt.ylabel(r'$\Omega_\Lambda$')
plt.grid(True)
plt.show()
