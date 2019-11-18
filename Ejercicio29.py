import os
import numpy as np
import matplotlib.pyplot as plt

plt.figure(1)

data = np.loadtxt("Ejercicio29.dat")

plt.plot(data[:,0], data[:,1])
plt.plot(data[:,0], data[:,2])
plt.plot(data[:,0], data[:,3])
plt.plot(data[:,0], data[:,4])
plt.plot(data[:,0], data[:,5])
plt.plot(data[:,0], data[:,6])
plt.plot(data[:,0], data[:,7])

plt.title("hola")
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig("Ejercicio29.png")
