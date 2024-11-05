import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Constants
c = 3e5  # Speed of light in km/s
H0 = 70  # Hubble constant in km/s/Mpc

# Function to calculate E(z)
def E(z, Omega_m0, Omega_Lambda0):
    Omega_k0 = 1.0 - Omega_m0 - Omega_Lambda0
    return np.sqrt(Omega_m0 * (1 + z)**3 + Omega_k0 * (1 + z)**2 + Omega_Lambda0)

# Function to calculate fK(chi)
def fK(chi, Omega_k0):
    if Omega_k0 > 0:
        return c / H0 / np.sqrt(Omega_k0) * np.sinh(np.sqrt(Omega_k0) * chi)
    elif Omega_k0 == 0:
        return c / H0 * chi
    else:
        return c / H0 / np.sqrt(-Omega_k0) * np.sin(np.sqrt(-Omega_k0) * chi)

# Function to calculate chi
def chi(z, Omega_m0, Omega_Lambda0):
    integral, _ = quad(lambda x: 1.0 / E(x, Omega_m0, Omega_Lambda0), 0, z)
    return integral

# Grid of Omega_m0 and Omega_Lambda0 values
Omega_m0_values = np.linspace(0.1, 0.9, 100)
Omega_Lambda0_values = np.linspace(0.1, 0.9, 100)
Omega_m0, Omega_Lambda0 = np.meshgrid(Omega_m0_values, Omega_Lambda0_values)

# Calculate fK(chi) for a fixed redshift z
z = 1.0
fK_values = np.zeros_like(Omega_m0)

for i in range(Omega_m0.shape[0]):
    for j in range(Omega_m0.shape[1]):
        Omega_k0 = 1.0 - Omega_m0[i, j] - Omega_Lambda0[i, j]
        chi_value = chi(z, Omega_m0[i, j], Omega_Lambda0[i, j])
        fK_values[i, j] = fK(chi_value, Omega_k0)

# Plotting
plt.figure(figsize=(10, 6))
contour = plt.contour(Omega_m0, Omega_Lambda0, fK_values, levels=10, cmap='viridis')
plt.clabel(contour, inline=True, fontsize=8)
plt.xlabel(r'$\Omega_{m,0}$')
plt.ylabel(r'$\Omega_{\Lambda,0}$')
plt.title(r'Lines of Constant $f_K(\chi)$ in the $\Omega_{m,0}$ - $\Omega_{\Lambda,0}$ Plane')
plt.colorbar(label=r'$f_K(\chi)$')
plt.grid(True)
plt.show()
