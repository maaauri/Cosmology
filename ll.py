import numpy as np
import matplotlib.pyplot as plt
import camb
import scienceplots


H0 = 67.4 # km/s/Mpc
omega_m = 0.315
omega_ch2 = 0.120
omega_bh2 = 0.0224
ns = 0.965
tau = 0.054
mnu=0

pars = camb.CAMBparams()
pars2=camb.CAMBparams()
pars.set_cosmology(H0=H0, ombh2=omega_bh2, omch2=omega_ch2, tau=tau)
results = camb.get_results(pars)
pars2.set_cosmology(H0=H0, ombh2=omega_bh2, omch2=omega_ch2, tau=tau,mnu=mnu)
results2 = camb.get_results(pars2)

print(results2)


# z_max = 250
# z_min = 0
# redshifts = np.arange(z_min, z_max, z_max//5)

# # set Matter Power Spectrum, para los redshifts que tenemos y un kmax (escala minima)
# pars.set_matter_power(redshifts=redshifts, kmax=1)
# pars2.set_matter_power(redshifts=redshifts, kmax=1)

# # Calculamos el matter power spectrum
# results = camb.get_results(pars)
# results2=camb.get_results(pars2)

# # obtenemos el Matter Power Spectrum, kh son los numeros de onda, z reshifts y 
# # PK el valor del power spectrum para ese par de kh y z.
# kh, z, PK = results.get_linear_matter_power_spectrum(hubble_units=True,
#                                                      k_hunit=True)
# kh2, z2, PK2 = results2.get_linear_matter_power_spectrum(hubble_units=True,
#                                                      k_hunit=True)
# fig, (ax, ax2) = plt.subplots(1,2,figsize=(5, 5))

# for iz, redshift in enumerate(redshifts):
#     ax.loglog(kh, PK[iz, :], label=f"z={redshift}")

# for iz2, redshift2 in enumerate(redshifts):
#     ax2.loglog(kh2, PK2[iz2, :], label=f"z={redshift2}")


# plt.legend(loc='upper right', bbox_to_anchor=(1, 1))
# ax.set_ylabel(r"$\mathcal{P}(k, z)$", fontsize=15)
# ax.set_xlabel(r"$k$ [h/Mpc]", fontsize=15)
# ax.set_title(f"$H_0$: {pars.H0} $\\frac{{km/s}}{{Mpc}}, $" + 
#                 f" $w$: {pars.DarkEnergy.w}, $c_s^2$: {pars.DarkEnergy.cs2}")

# ax2.set_ylabel(r"$\mathcal{P}(k, z)$", fontsize=15)
# ax2.set_xlabel(r"$k$ [h/Mpc]", fontsize=15)
# ax2.set_title(f"$H_0$: {pars2.H0} $\\frac{{km/s}}{{Mpc}}, $" + 
#                 f" $w$: {pars2.DarkEnergy.w}, $c_s^2$: {pars2.DarkEnergy.cs2}")

# fig.suptitle("Matter Power Spectrum", fontsize=15)

# plt.show()