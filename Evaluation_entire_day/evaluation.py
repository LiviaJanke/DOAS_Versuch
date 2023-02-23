# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math as math
#from pandas.compat import StringIO


#%%

File, Datum, StartZeit, SZA, AMF, ChiSquare, \
Fraunhofer_reference_log, Fraunhofer_reference_log_Error, \
Ring_Spectrum, Ring_Spectrum_Error, convolution_result_H2O, \
convolution_result_H2O_Error , 	convolution_result_NO2, 	convolution_result_NO2_Error, \
convolution_result_O3,	convolution_result_O3_Error, \
convolution_result_O4,	convolution_result_O4_Error\
= np.loadtxt('ozonres.dat', skiprows = 1, unpack = True, delimiter = '	', dtype = str)

#%%

a,b,c,d,e, \
f,g,h,i,j,k,l,m,n,o,p,q,r,s = np.loadtxt('ozonres.dat', skiprows = 1, unpack = True, delimiter = '	', dtype = str)

#%%

o3_df = pd.read_csv('ozonres.dat', sep='\t')
no2_df = pd.read_csv('no2res.dat', sep='\t')

#%%


#o3_df.plot(x = 'AMF  ', y = 'convolution_result_O3')

AMF_array = o3_df['AMF  ']
conv_res_O3_array = o3_df['convolution_result_O3']


#%%

amf_conc_o3 = np.stack((AMF_array, conv_res_O3_array), axis=-1)

print(len(amf_conc_o3))

amf_O3_below_5 = []
conc_O3_below_5 = []
for i in range(len(amf_conc_o3[:,0])):
    if amf_conc_o3[:,0][i] < 5:
        amf_O3_below_5.append(AMF_array[i])
        conc_O3_below_5.append(conv_res_O3_array[i])

print(len(amf_O3_below_5))
plt.figure()
plt.plot(amf_O3_below_5, conc_O3_below_5,'*')
plt.show()









