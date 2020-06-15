import numpy as np

import matplotlib.pyplot as plt
import mplcursors
from scipy.misc import electrocardiogram
from scipy.signal import find_peaks

# pip install heartpy
import heartpy as hp


#first let's load the clean PPG signal
data, timer = hp.load_exampledata(0)

time = np.arange(0, len(data)/100, 0.01)

peaks, _ = find_peaks(data, distance=50)

# Plotear los picos
plt.plot(data)
plt.plot(peaks, data[peaks], "x")
mplcursors.cursor(multiple=True)
plt.show()

# Calcular el ritmo cardiaco
delta_time = np.diff(peaks) / 100
promedio = np.mean(delta_time)
pulsaciones_por_minuto = promedio * 60
print("Pulsaciones", pulsaciones_por_minuto)