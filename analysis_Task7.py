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

plt.errorbar(exposure_times, dark_currents, dark_currents_errs, elinewidth = 0.1, capsize = 1)
plt.xlabel('Exposure Time (s)')
plt.ylabel('Intensity (a.u.)')
plt.grid()
plt.title('Dark Current vs Exposure Time')
plt.savefig('Dark Current vs Exposure Time')




