import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Constantes
H0 = 67  # Constante de Hubble en Km/(s Mpc)
Omega_r0 = 1e-4  # Parámetro de densidad de radiación
Omega_m0 = 0.3  # Parámetro de densidad de materia
Omega_lambda0 = 1 - Omega_r0 - Omega_m0  # Parámetro de densidad de energía oscura

# Definir los factores de escala y los números de onda
a_values = np.logspace(-4, 0, 1000)
k_values = [H0, 5*H0, 20*H0, 200*H0]

# Definir las ecuaciones de perturbación
def perturbations(y, a, k):
    delta, delta_prime = y
    E = np.sqrt(Omega_r0/a**4 + Omega_m0/a**3 + Omega_lambda0)
    ddelta_da = delta_prime / (a * E)
    ddelta_prime_da = - (3/a + (1/E) * dE_da(a)) * delta_prime / E - (k**2 / (a**2 * E**2)) * delta / E
    return [ddelta_da, ddelta_prime_da]

def dE_da(a):
    return -2 * Omega_r0 / a**5 - 1.5 * Omega_m0 / a**4

# Condiciones iniciales
delta_init = [1e-5, 1e-5]

# Resolver las ecuaciones de perturbación para cada número de onda
results = {}
for k in k_values:
    sol = odeint(perturbations, delta_init, a_values, args=(k,))
    results[k] = sol[:, 0]

# Graficar los resultados
plt.figure(figsize=(10, 6))
for k in k_values:
    plt.plot(a_values, results[k], label=f'k = {k/H0} H0')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Factor de escala (a)')
plt.ylabel('Perturbación de densidad (δ)')
plt.title('Perturbaciones de Densidad para Diferentes Escalas en el Modelo ΛCDM')
plt.legend()
plt.grid(True)
plt.show()
