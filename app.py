import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from scipy.fftpack import fft
import numpy as np


rate, data = wav.read('Samples/ze1.wav')
# a = data.T[0] # this is a two channel soundtrack, I get the first track
# b=[(ele/2**8.)*2-1 for ele in a] # this is 8-bit track, b is now normalized on [-1,1)
# c = fft(b) # calculate fourier transform (complex numbers list)
# d = len(c)/2  # you only need half of the fft list (real signal symmetry)
# plt.plot(abs(c[:(d-1)]),'r') 
# plt.show()




N = 600
a = data.T[0]
fft_out = fft(a)
print(fft_out)
# plt.plot(data, np.abs(fft_out))
fig, ax = plt.subplots()
ax.plot(data, 2.0/N * np.abs(fft_out))
plt.show()
