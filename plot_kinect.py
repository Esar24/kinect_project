#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 05:49:03 2018

@author: esar
"""
import numpy as np
import matplotlib.pyplot as plt

text_file = open("chest_09.txt", "r")
lines = text_file.readlines()
depth=[]
time=[]
for x in lines:
    depth.append(x.split(" ")[0])
    time.append(x.strip("\n").split(" ")[1])

fourier=np.fft.fft(depth)
freq=np.fft.fftfreq(len(depth),d=0.05)
#print (fourier)
#print (time)
plt.subplot(211)
plt.plot(time,depth)
plt.subplot(212)
plt.plot(freq,abs(fourier)*0.00328)
plt.show()

text_file.close()