from nodepy import rk, semidisc
import numpy as np
import matplotlib.pyplot as plt
import nodepy.rooted_trees as rt 
import nodepy.convergence as cv 
from nodepy import ivp
from nodepy import *
import matlab.engine


rk4 = rk.loadRKM('RK44')
A_py = rk4.A
b_py = rk4.b
c_py = rk4.c
p = rk4.p
# print(type(rk4.A))

A_py2 = np.array([[0, 0, 0, 0], [1/2, 0, 0, 0], [0, 1/2, 0, 0], [0, 0, 1/2, 0]])

# print(type(A_py))
# print(type(A_py2))

eng = matlab.engine.start_matlab()
# eng.addpath(r'PATH')


A_list = A_py.tolist()
A_list = [[float(val) for val in row] for row in A_list]
b_list = b_py.tolist()
b_list = [[float(val) for val in row] for row in b_list]
c_list = c_py.tolist()
c_list = [[float(val) for val in row] for row in c_list]
A = matlab.double(A_list)
b = matlab.double(b_list)
c = matlab.double(c_list)


# A = matlab.double(A_py.tolist())
# b = matlab.double(b_py.tolist())
# c = matlab.double(c_py.tolist())

butcher = eng.oc_butcher(A,b,c,p)
# butcher = eng.oc_butcher(A_py, b_py, c_py, p)

eng.quit()