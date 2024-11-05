import numpy as np
import matplotlib.pyplot as plt
import camb

H0 = 67.4 # km/s/Mpc
omega_m = 0.315
omega_ch2 = 0.120
omega_bh2 = 0.0224
ns = 0.965
tau = 0.054

pars = camb.CAMBparams()

pars.set_cosmology(H0=H0, ombh2=omega_bh2, omch2=omega_ch2, tau=tau)

pars.set_dark_energy(w=-1)
results = camb.get_results(pars)

pars2 = camb.set_params(H0=67.4, w=-0.1, cs2=0.1)
results2 = camb.get_results(pars2)

def Hz(z, omegar, omegam, omegaa, omegak, omega):
    res=np.sqrt(omegar*(1+z)**(4)+omegam*(1+z)**3 + omegaa*(1+z)**(3*(1+omega))+ omegak*(1+z)**2)
    return res

omegam=0.05 
omegar=0.2 
omegaa=0.75
omegak=0

z=np.linspace(0, 10, 1000)

