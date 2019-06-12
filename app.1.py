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

rate, data = wav.read('Samples/ze1.wav')
l_audio = len(data.shape)
if l_audio == 2:
    data = data.sum(axis=1) / 2
N = data.shape[0]
secs = N / float(rate)
print ("secs", secs)
Ts = 1/rate  # Timestep between samples Ts
t = scipy.arange(0, secs, Ts) # time vector as scipy arange field / numpy.ndarray
print (t)
FFT_side = abs(scipy.fft(data))[range(N//2)]
freqs = scipy.fftpack.fftfreq(data.size, t[1]-t[0])
fft_freqs = np.array(freqs)
# freqs_side = freqs[range(N//2)]
# fft_freqs_side = np.array(freqs_side)
p1 = plt.plot(t, data, "g")
plt.show()





# print(rate)
# l_audio = len(data.shape)
# print ("Channels", l_audio)
# secs = N / float(rate)
# print(secs)
# a = data.T[0]
# fft_out = fft(a)

# yf = scipy.fftpack.fft(a)
# xf = np.linspace(0.0, 1.0/(2.0*T), N/2)

# fig, ax = plt.subplots()
# ax.plot(xf, 2.0/N * np.abs(yf[:N//2]))
# plt.xlabel('Frequency (Hz)')
# # plt.ylabel('Count single-sided')
# plt.show()
