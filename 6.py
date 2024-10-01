import sys, platform, os
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import camb


H0 = 67.74
omega_m = 0.315
omega_ch2 = 0.120
omega_bh2 = 0.0224
ns = 0.965
tau = 0.054

pars = camb.CAMBparams()

pars.set_cosmology(H0=H0, ombh2=omega_bh2, omch2=omega_ch2, tau=tau)

pars.set_dark_energy(w=-1)
results= camb.get_results(pars)
a = np.logspace(-5, 0, 1000)
z= 1/a - 1

rho_de= results.get_Omega(var='de', z=z)  # Densidad de energía oscura
rho_b = results.get_Omega(var='baryon',z=z) # Densidad de baryones
rho_c = results.get_Omega(var='cdm', z=z) # Densidad de darkmatter
rho_r = results.get_Omega(var='photon', z=z) # Densidad de radiación
rho_k = results.get_Omega(var='K', z=z) # Densidad de curvatura
rho_m=rho_b+rho_c



plt.plot(a, rho_de, color='r', label='Energía Oscura')
plt.plot(a, rho_m, color='b', label='Materia')
plt.plot(a, rho_r, color='g', label='Radiación')
plt.plot(a, rho_k, color='m', label='Curvatura')


plt.xscale('log') 
plt.xlabel('Factor de escala $a$')
plt.ylabel(r'$\Omega$')
plt.title('Evolución de densidades')
plt.legend(loc='best')
plt.xlim(1e-5, 1) 

plt.show()
