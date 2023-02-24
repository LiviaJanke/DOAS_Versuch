# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 13:25:26 2023

@author: lme19
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



#%%

exposure_times = (60,50,40,30,20,10)
dark_currents = np.array((255.27, 213.12, 170.44, 125.73, 82.267, 65.313))
dark_currents_errs = np.array((394.05, 337.13, 278.4, 205.26, 134.44, 65.313))
dark_current_time_averaged = dark_currents / exposure_times
dc_error_time_avg = dark_currents_errs / exposure_times



#%%

plt.errorbar(exposure_times, dark_currents, dark_currents_errs, elinewidth = 0.5, capsize = 5, marker = 'X', linewidth = 0)
plt.xlabel('Exposure Time (s)')
plt.ylabel('Intensity (a.u.)')
plt.grid()
plt.title('Dark Current vs Exposure Time')
plt.savefig('Dark Current vs Exposure Time')
plt.show()

#%%

plt.errorbar(exposure_times, dark_current_time_averaged, dc_error_time_avg, elinewidth = 0.5, capsize = 5, marker = 'X', linewidth = 0)
plt.xlabel('Exposure Time (s)')
plt.ylabel('Time Averaged Intensity (a.u.)')
plt.grid()
plt.title('Time Averaged Dark Current vs Exposure Time')
plt.savefig('Time Averaged Dark Current vs Exposure Time')
plt.show()


#%%


number_scans = (10000, 9000, 8000, 7000, 6000, 5000)
instrument_noises = (220.82, 205.92, 193.50, 173.64, 163.72, 144.09)


#%%

plt.plot(number_scans, instrument_noises, marker = 'X', linewidth = 0)
plt.xlabel('Number of Scans')
plt.ylabel('Instrument Noise')
plt.title('Instrument Noise vs Number of Scans')
plt.grid()
plt.savefig('Instrument Noise vs Number of Scans')
plt.show()


#%%

stan_devs_photon_noise = (414.87, 386.55, 367.05, 343.41, 323.04, 283.34)

exposures = (10000, 9000, 8000, 7000, 6000, 5000)

plt.plot(exposures, stan_devs_photon_noise, marker = 'X', linewidth = 0)
plt.grid()
plt.xlabel('Exposures')
plt.ylabel('Standard Deviation')
plt.title('Photon Noise')
plt.savefig('Photon Noise')
plt.show()



#%%

relative_optical_density_noise = ( -0.00699,  -0.015046 , -0.0085272 , -0.011589549 , -0.01568564,  -0.01547557)
rel_op_dens_noise_delta = (0.021182, 0.027817, 0.024901871, 0.029738359, 0.034668914, 0.04885212)
rel_op_dens_noise_err = (0.0037046, 0.005306, 0.00467379, 0.00537876, 0.006716826, 0.00871387)


plt.errorbar(exposures, rel_op_dens_noise_delta, yerr = rel_op_dens_noise_err, marker = 'X', linewidth = 0, capsize = 1, elinewidth = 0.5)
plt.grid()
plt.xlabel('Exposures')
plt.ylabel('Optical Density')
plt.title('Relative Total Noise')
plt.savefig('Relative Total Noise')
plt.show()

#%%















