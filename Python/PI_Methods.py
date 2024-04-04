from nodepy import rk, semidisc
import numpy as np
import matplotlib.pyplot as plt
import nodepy.rooted_trees as rt 
import nodepy.convergence as cv 
from nodepy import ivp
from nodepy import *

from Matrix_Building import PFEasRK
from Matrix_Building import gen_block_matrix
from Matrix_Building import gen_b_matrix


lam = 0.01
K = 10
S = 2

## PIFE
A = PFEasRK(lam, K)[0]
b = np.squeeze(PFEasRK(lam, K)[1])
A_block = gen_block_matrix(S, lam, K, A, b)
b_block = gen_b_matrix(S, b, lam, K)
result = rk.ExplicitRungeKuttaMethod(A_block, b_block)
bounds = [-1/lam-100, 50, -300, 300]
result.plot_stability_region(bounds = bounds)
plt.show()


# PIH
# A = np.array([[0, 0], [1, 0]])
# b = np.array([1/2, 1/2])
# A_block = gen_block_matrix(S, lam, K, A, b)
# b_block = gen_b_matrix(S, b, lam, K)
# result = rk.ExplicitRungeKuttaMethod(A_block, b_block)
# bounds = [-1/lam-100, 50, -300, 300]
# result.plot_stability_region(bounds = bounds)
# plt.show()


## PIRK4
# A = np.array([[0,0,0,0],[1/2,0,0,0],[0,1/2,0,0],[0,0,1,0]])
# b = np.array([1/6, 1/3, 1/3, 1/6])
# A_block = gen_block_matrix(S, lam, K, A, b)
# b_block = gen_b_matrix(S, b, lam, K)
# result = rk.ExplicitRungeKuttaMethod(A_block, b_block)
# print(b_block.shape)
# bounds = [-1/lam-50, 50, -300, 300] # x_left, x_right, y_bottom, y_top
# bounds = [-10, 10, -10, 10]
# result.plot_stability_region(bounds = bounds)
# result.plot_stability_region()
# result.plot_stability_function()
# plt.show()

print("Finished")