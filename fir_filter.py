#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 14:38:32 2018

@author: esar
"""

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

text_file = open("actual_data/120sec_diaphr/diaphr_p10.txt", "r")
lines = text_file.readlines()
depth=[]
time=[]
for x in lines:
    depth.append(x.split(" ")[0])
    time.append(x.strip("\n").split(" ")[1])


#t = np.linspace(-3, 3, 201)
#x = (np.sin(2*np.pi*0.75*t*(1-t) + 2.1) +
#     0.1*np.sin(2*np.pi*1.25*t + 1) +
#     0.18*np.cos(2*np.pi*3.85*t))
#xn = x + np.random.randn(len(t)) * 0.08
t = [float(i) for i in time]
xn = [((float(i)*0.4196)+96.096) for i in depth]
#xn = [((float(i)*1.03)+39) for i in depth]
#xn = [float(i) for i in depth]
b, a = signal.butter(3, 0.05)
zi = signal.lfilter_zi(b, a)
z, _ = signal.lfilter(b, a, xn, zi=zi*xn[0])
z2, _ = signal.lfilter(b, a, z, zi=zi*z[0])
y = signal.filtfilt(b, a, xn)

fourier=np.fft.fft(z)
freq=np.fft.fftfreq(len(z),d=0.05)

plt.figure
#plt.subplot(311)
plt.title("Data Perubahan Nafas Perut P10")
#plt.title("Data Frekuensi Nafas Dada P01")
plt.plot(t, xn,"b",t,y,"g")
plt.xlabel("Waktu(s)")
plt.ylabel("Jarak(cm)")
plt.legend(("Noisy Signal","Filter Signal"),loc="best")
#plt.subplot(312)
#plt.plot(freq,abs(fourier)*0.05)
#plt.xlabel("Frekuensi(Hz)")
#plt.ylabel("Gain")
#plt.subplot(313)
#plt.plot((freq*60),abs(fourier)*0.05)
#plt.xlabel("Breaths per minute")
#plt.ylabel("Gain")
plt.grid(True)
plt.show()
