import camb
from camb import model, initialpower
import matplotlib.pyplot as plt
import numpy as np

from camb.dark_energy import DarkEnergyPPF, DarkEnergyFluid
pars = camb.read_ini('https://raw.githubusercontent.com/cmbant/CAMB/master/inifiles/planck_2018.ini')
pars.DarkEnergy = DarkEnergyPPF(w=-1.2, wa=0.2)
print('w, wa model parameters:\n\n', pars.DarkEnergy)
results = camb.get_background(pars)

#or can also use a w(a) numerical function 
#(note this will slow things down; make your own dark energy class in fortran for best performance)
a = np.logspace(-5, 0, 1000)
w = -1.2 + 0.2 * (1 - a)
pars.DarkEnergy= DarkEnergyPPF()
pars.DarkEnergy.set_w_a_table(a, w)
print('Table-interpolated parameters (w and wa are set to estimated values at 0):\n\n' 
      ,pars.DarkEnergy)
results2 = camb.get_background(pars)

rho, _ = results.get_dark_energy_rho_w(a)
rho2, _ = results2.get_dark_energy_rho_w(a)
plt.plot(a, rho, color='k')
plt.plot(a, rho2, color='r', ls='--')
plt.ylabel(r'$\rho/\rho_0$')
plt.xlabel('$a$')
plt.xlim(0,1)
plt.title('Dark enery density')
plt.show()