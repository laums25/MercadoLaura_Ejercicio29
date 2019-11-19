import os
import numpy as np
import matplotlib.pyplot as plt

plt.figure(1, figsize=(8,4))

plt.subplot(1,2,2)
data = np.loadtxt("Ejercicio29.dat")

plt.plot(data[:,0], data[:,1])
plt.plot(data[:,0], data[:,2])
plt.plot(data[:,0], data[:,3])
plt.plot(data[:,0], data[:,4])
plt.plot(data[:,0], data[:,5])
plt.plot(data[:,0], data[:,6])
plt.plot(data[:,0], data[:,7])

plt.subplot(1,2,1)
plt.imshow(data.T)            
            
plt.title("hola")
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig("Ejercicio29.png")



plt.figure(2, figsize=(8,4))

plt.subplot(1,2,2)
da = np.loadtxt("Ejer29.dat")

plt.plot(da[:,0], da[:,1])
plt.plot(da[:,0], da[:,2])
plt.plot(da[:,0], da[:,3])
plt.plot(da[:,0], da[:,4])
plt.plot(da[:,0], da[:,5])
plt.plot(da[:,0], da[:,6])
plt.plot(da[:,0], da[:,7])

plt.subplot(1,2,1)
plt.imshow(da.T)            
            
plt.title("hola")
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig("Ejer29.png")


plt.figure(3, figsize=(8,4))

plt.subplot(1,2,2)
d = np.loadtxt("Ej29.dat")

plt.plot(d[:,0], d[:,1])
plt.plot(d[:,0], d[:,2])
plt.plot(d[:,0], d[:,3])
plt.plot(d[:,0], d[:,4])
plt.plot(d[:,0], d[:,5])
plt.plot(d[:,0], d[:,6])
plt.plot(d[:,0], d[:,7])

plt.subplot(1,2,1)
plt.imshow(d.T)            
            
plt.title("hola")
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig("Ej29.png")



