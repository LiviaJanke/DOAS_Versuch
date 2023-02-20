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
dark_currents = (6.2977, 6.7263, 7.3768, 8.3922, 10.476, 16.69)
dark_currents_errs = (6.4387, 6.4851, 6.8274, 6.7501, 6.7851, 6.9507)

#%%


plt.plot(exposure_times, dark_currents)


#%%

plt.errorbar(exposure_times, dark_currents, dark_currents_errs, elinewidth = 0.5, capsize = 5, marker = 'X', linewidth = 0)
plt.xlabel('Exposure Time (s)')
plt.ylabel('Intensity (a.u.)')
plt.grid()
plt.title('Dark Current vs Exposure Time')
plt.savefig('Dark Current vs Exposure Time')
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

stan_devs = (407.1, 393.79, 386.33, 326.82, 307.27)

exposures = (10000, 9000, 8000, 7000, 6000)

plt.plot(exposures, stan_devs, marker = 'X', linewidth = 0)
plt.grid()
plt.xlabel('Exposures')
plt.ylabel('Standard Deviation')
plt.title('Photon Noise')
plt.savefig('Photon Noise')



#%%




















