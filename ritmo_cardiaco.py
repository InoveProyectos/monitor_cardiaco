#!/usr/bin/env python
'''
Ritimo cardíaco [Python]
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para mostrar ejemplos se análisis de señales y procesamiento
y cálculo del ritmo cardíaco
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import numpy as np

import matplotlib.pyplot as plt
import mplcursors
from scipy.signal import find_peaks

# Libreria heartpy
# instalar ejecutar --> pip install heartpy
import heartpy as hp

# Comencemos con nuestro primer ejemplo
data, timer = hp.load_exampledata(0)
sample_rate = 100

plt.figure()
plt.plot(data)
plt.title("Ritmo cardíaco: Ejemplo 1")
plt.legend(['ritmo cardíaco'])
plt.ylabel('pulsos')
plt.xlabel('muestras')
plt.show()

# Utilizaremos la libreria scipy para detectar picos
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.find_peaks.html
sample_rate = 100
peaks, _ = find_peaks(data, distance=50)

# Plotear los picos
plt.figure()
plt.plot(data)
plt.plot(peaks, data[peaks], "x")
plt.title("Ritmo cardíaco: Ejemplo 1")
plt.legend(['ritmo cardíaco', 'pulsos'])
plt.ylabel('pulsos')
plt.xlabel('muestras')
mplcursors.cursor(multiple=True)
plt.show()

# Calcular el ritmo cardíaco como la diferencia
# de tiempo entre los picos
delta_time = np.diff(peaks) / 100
promedio = np.mean(delta_time)
pulsaciones_por_minuto = promedio * 60
print("Pulsaciones", pulsaciones_por_minuto)

# Ahora veamos un ejemplo más real de uso, en donde se puede
# ver el ruido introducido por la colocación del instrumento
# y los movimientos del paciente.
data, timer = hp.load_exampledata(1)
sample_rate = hp.get_samplerate_mstimer(timer)

plt.figure()
peaks, _ = find_peaks(data, distance=sample_rate/2.0)
plt.plot(data)
plt.plot(peaks, data[peaks], "x")
plt.title("Ritmo cardíaco: Ejemplo 2")
plt.legend(['ritmo cardíaco', 'pulsos'])
plt.ylabel('pulsos')
plt.xlabel('muestras')
mplcursors.cursor(multiple=True)
plt.show()

delta_time = np.diff(peaks) / 100
promedio = np.mean(delta_time)
pulsaciones_por_minuto = promedio * 60
print("Pulsaciones", pulsaciones_por_minuto)

# Buscar picos que prevalezcan superiores a su entorno por más del tiempo
# definido (medio ciclo de la señal) --> "prominencia"
peaks, properties = find_peaks(data, prominence=1, width=sample_rate/2.0)

plt.figure()
plt.plot(data)
plt.plot(peaks, data[peaks], "x")
plt.vlines(x=peaks, ymin=data[peaks] - properties["prominences"],
        ymax = data[peaks], color = "C1")
plt.hlines(y=properties["width_heights"], xmin=properties["left_ips"],
        xmax=properties["right_ips"], color = "C1")
mplcursors.cursor(multiple=True)
plt.show()


# Veamos ahora el potencial de heartpy
# Ejemplo 1
data, timer = hp.load_exampledata(0)
sample_rate = 100
wd, m = hp.process(data, sample_rate = sample_rate)

hp.plotter(wd, m)
measure = 'bpm'
print("Pulsaciones", m['bpm'])

# Ejemplo 2
data, timer = hp.load_exampledata(1)
sample_rate = hp.get_samplerate_mstimer(timer)
wd, m = hp.process(data, sample_rate = sample_rate)

hp.plotter(wd, m)
measure = 'bpm'
print("Pulsaciones", m['bpm'])