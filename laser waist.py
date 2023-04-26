import matplotlib.pyplot as plt
import numpy as np

w0 = 70*10**(-6)
LAMBDA = 532*10**(-9)
zr = (np.pi * w0**2)/LAMBDA

def w(w0, zr, z):
    return w0*np.sqrt(1+(z/zr)**2)

def w2(w0, zr, z):
    return w0/2*np.sqrt(1+(z/zr)**2)

z = np.linspace(-0.1, 0.1, 1000)
yp = w(w0, zr, z)
ym = -w(w0, zr, z)

y2p = w2(w0, zr, z)
y2m = -w2(w0, zr, z)

plt.plot(z, y2p, "C1")
plt.plot(z, y2m, "C1")
plt.ylabel(r"Taille du faisceau $w(z)$ (m)")
plt.xlabel(r"Distance $z$ au waist (m)")
plt.show()
