from nodepy import rk, semidisc
import numpy as np
import matplotlib.pyplot as plt
import nodepy.rooted_trees as rt 
import nodepy.convergence as cv 
from nodepy import ivp
from nodepy import *
import matlab.engine

# Heun's Method
A = np.array([[0, 0], [1, 0]])
b = np.array([1/2, 1/2])
Heun = rk.ExplicitRungeKuttaMethod(A,b)
# print(Heun.c)
# Heun.plot_stability_region()
# plt.show()

# Prijective Heun's Method
lam = 0.1
A1 = np.array([[0, 0, 0], [lam, 0, 0], [lam, lam, 0]])
A2 = np.zeros([3, 3])
A3 = np.array([[lam, lam, 1-2*lam], [lam, lam, 1-2*lam], [lam, lam, 1-2*lam]])

A = np.block([[A1, A2], [A3, A1]])
b = np.array([lam, lam, 1/2-(1/2)*lam, 0, 0, 1/2-(3/2)*lam])
Proj_Heun = rk.ExplicitRungeKuttaMethod(A,b)
print(Proj_Heun)
Proj_Heun.plot_stability_region(bounds = [-30, 1, -30, 30])
plt.show()

A = np.array([[0, 0, 0], [lam, 0, 0], [lam, lam, 0]])
b = np.array([lam, lam, 1-2*lam])
test_rk = rk.ExplicitRungeKuttaMethod(A, b)
# print(test_rk.c)
test_rk.plot_stability_region(bounds = [-30, 1, -30, 30])
plt.show()


print("Finished")