from nodepy import rk, semidisc
import numpy as np
import matplotlib.pyplot as plt
import nodepy.rooted_trees as rt 
import nodepy.convergence as cv 
from nodepy import ivp
from nodepy import *
import matlab.engine

print('Start')

rk4 = rk.loadRKM('RK44')
print(rk4)
rk4.plot_stability_region()
print('The order of the method is', rk4.order())

fig = rt.plot_all_trees(4)
plt.setp(fig, dpi=500)
plt.draw()

SSP2 = rk.loadRKM('SSP22')
SSP104 = rk.loadRKM('SSP104')

myivp = ivp.load_ivp('test')

cv.ctest([rk4,SSP2,SSP104], myivp, verbosity=1)

bs5 = rk.loadRKM('BS5')
f5 = rk.loadRKM('Fehlberg45')
dp5 = rk.loadRKM('DP5')

ivps = ivp.detest_suite()
tols = list(map(lambda x:10**-x, range(4,10)))
conv.ptest([bs5,dp5,f5],ivps,tols)

rk4 = rk.loadRKM('RK44')
upwind = semidisc.upwind_advection_matrix(100, dx=0.1)

rk.linearly_stable_step_size(rk4, upwind)
spectral = semidisc.load_semidisc('spectral difference advection', order=6)
rk.linearly_stable_step_size(rk4, spectral.L)

weno5 = semidisc.weno5_linearized_matrix(100)
rk.linearly_stable_step_size(rk4, weno5)

centered_diff = semidisc.centered_advection_diffusion_matrix(10.,1.,N=100)
rk.linearly_stable_step_size(rk4,centered_diff)

rkc = rk.RKC2(10)
rk.linearly_stable_step_size(rkc,centered_diff)

rkc_damped = rk.RKC2(10,epsilon=0.2)
rk.linearly_stable_step_size(rkc_damped,centered_diff)

rkc.real_stability_interval()
rkc_damped.real_stability_interval()

# Creating custom Butcher Tableau
A = np.array([[0,0,0],[1.5,0.5,0],[0,1.,0]])
b = np.array([0,0.5,0.5])
rk22 = rk.ExplicitRungeKuttaMethod(A,b)
print(rk22)
rk22.plot_stability_region()

# b = np.array([0.75,0,0.25])
# rk22 = rk.ExplicitRungeKuttaMethod(A,b)
# print(rk22)
# rk22.plot_stability_region()


rk4 = rk.loadRKM('RK44')
SSP2 = rk.loadRKM('SSP22')
SSP104 = rk.loadRKM('SSP104')

myivp = ivp.load_ivp('test')
cv.ctest([rk4,SSP2,SSP104],myivp,verbosity=1)

print('Finished')