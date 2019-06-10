import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
from scipy.fftpack import fft
from scipy.io import wavfile as wav


# Number of samplepoints
N = 600
# sample spacing
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N)
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)

rate, data = wav.read('Samples/ze2.wav')
a = data.T[0]
fft_out = fft(a)

yf = scipy.fftpack.fft(a)
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)

fig, ax = plt.subplots()
ax.plot(xf, 2.0/N * np.abs(yf[:N//2]))
plt.xlabel('Frequency (Hz)')
# plt.ylabel('Count single-sided')
plt.show()
