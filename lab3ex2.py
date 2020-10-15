import numpy as np
import lab3ex1
g=lab3ex1.g
h = 100
alpha=np.pi/3
betha_deg=30
betha=np.radians(betha_deg)
q1 = g * h * np.tan(betha)**2
q2 = 2 * np.cos(alpha)**2
q3 = 1 - (np.tan(betha) * np.tan(alpha))
v = np.sqrt( q1 / (q2 * q3))
print(v)
