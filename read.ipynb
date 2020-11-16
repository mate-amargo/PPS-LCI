#!/usr/bin/env python

# Prueba para leer los datos desde las planillas
# y graficar la serie de tiempo y su fft

import pandas
import matplotlib.pyplot as plt
import numpy as np

# variable a anlizar
col = 'H' # temp_amb_prom
# numeros de filas a incluir (rango inclusivo)
firstrow = 41631
lastrow = 127433

# Lectura de datos
temp = pandas.read_excel('datos/Planilla VILLA.xlsx', usecols=col, header=None, skiprows=firstrow-1,nrows=lastrow-firstrow+1)

# Imputation
#temp.fillna(temp.mean(), inplace=True) # reemplazo los nan por el valor medio
values = temp.interpolate(method='akima') # interpolo con splines

# Serie de tiempo
plt.figure(1)
plt.plot(values)

# Calculo la FFT
t = np.arange(lastrow-firstrow+1)
fft = np.fft.fft(values)
freq = np.fft.fftfreq(t.shape[-1])
fft = np.fft.fftshift(fft)
freq = np.fft.fftshift(freq)
plt.figure(2)
plt.plot(freq,np.abs(fft))

plt.show()
exit()
