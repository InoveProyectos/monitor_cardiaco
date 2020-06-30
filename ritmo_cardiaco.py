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
import matplotlib.image as mpimg
import matplotlib.gridspec as gridspec
import mplcursors
import pandas as pd
from scipy.signal import find_peaks

# Libreria heartpy
# instalar ejecutar --> pip install heartpy
import heartpy as hp


def deteccion_estres():
    # Observar la variación del pulso cardíaco de una persona
    # mirando la serie "Vikingos"
    df = pd.read_csv('vikings_female_24.csv')

    plt.figure()
    plt.plot(df['heart'])
    plt.title('Variación del rítmo cardíaco observando Vikingos')
    plt.legend(['ritmo cardíaco'])
    plt.ylabel('pulsos')
    plt.xlabel('muestras')
    plt.show()

    # Entrenamiento de una inteligencia artificial para detección de estrés
    # Autor: Christopher Ottesen
    # https://dataespresso.com/en/2019/01/30/Stress-detection-with-wearable-devices-and-Machine-Learning/

    # Cálculo de la diferencia de tiempo entre pulsos
    R_R = np.diff(df['heart'])

    gs = gridspec.GridSpec(2, 2)
    plt.figure()
    axs1 = plt.subplot(gs[0, 0]) # row 0, col 0
    axs2 = plt.subplot(gs[0, 1]) # row 0, col 1
    axs3 = plt.subplot(gs[1, :]) # row 1, span all columns

    # Graficar el rítmo cardíaco
    axs1.plot(df['heart'])
    axs1.set_title('Rítmo cardíaco observando Vikingos')
    axs1.set_ylabel('pulsos')
    axs1.set_xlabel('muestras')
    axs1.legend(['ritmo cardíaco'])
    
    # Graficar la variación del rítmo cardíaco
    axs2.plot(R_R, color = 'red')
    axs2.set_title('Variación del rítmo cardíaco observando Vikingos')
    axs2.set_ylabel('R-R')
    axs2.set_xlabel('muestras')
    axs2.legend(['R-R'])

    img=mpimg.imread('deteccion_estres.png')
    axs3.imshow(img)
    axs3.set_title('Detector de estrés con inteligencia artificial')
    axs3.get_xaxis().set_visible(False)
    axs3.get_yaxis().set_visible(False)

    plt.show()
    

def medicion_ritmo_cardiaco():

    # Comencemos con nuestro primer ejemplo
    # Señal capturada con un pulsómetro con la técnica
    # de fotoplestimografía (PPG).
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
    delta_time_rate = np.diff(peaks)
    delta_time = delta_time_rate / sample_rate
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
    # Autor: Paul van Gent
    # https://github.com/paulvangentcom/heartrate_analysis_python/blob/master/examples/1_regular_PPG/Analysing_a_PPG_signal.ipynb
    # Ejemplo 1
    data, timer = hp.load_exampledata(0)
    sample_rate = 100
    wd, m = hp.process(data, sample_rate = sample_rate)

    hp.plotter(wd, m)
    print("Pulsaciones", m['bpm'])

    # Ejemplo 2
    data, timer = hp.load_exampledata(1)
    sample_rate = hp.get_samplerate_mstimer(timer)
    wd, m = hp.process(data, sample_rate = sample_rate)

    hp.plotter(wd, m)
    print("Pulsaciones", m['bpm'])


if __name__ == '__main__':
    medicion_ritmo_cardiaco()
    deteccion_estres()
