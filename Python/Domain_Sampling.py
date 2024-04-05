import numpy as np
import matplotlib.pyplot as plt
from nodepy import rk
from nodepy import *
import matlab.engine
import time
import pathlib

from Matrix_Building import PFEasRK
from Matrix_Building import gen_block_matrix
from Matrix_Building import gen_b_matrix

start = time.time()
eng = matlab.engine.start_matlab()
eng.addpath(r'C:\Users\herri\OneDrive\Documents\Groningen\Thesis\Scripts\Matlab')

#skeleton
# The user will be asked the path to a matlab foldeer
# matlab_path_reference: pathlib.Path = pathlib.Path("./matlab_codes")
# if isinstance(path_from_user, str):
#     path_from_user: pathlib.Path = pathlib.Path(path_from_user)

# path_to_engine: str = matlab_path_reference.joinpath("examples").as_posix()
# eng.addpath(path_to_engine)



p = 5
test = f"squareValue({p});"
r_test = eng.eval(test, nargout=1)

print(r_test)


lam = 0.01
K = 3
S = 2


# ## PIFE
# A = PFEasRK(lam, K)[0]
# b = np.squeeze(PFEasRK(lam, K)[1])
# A_block = gen_block_matrix(S, lam, K, A, b)
# b_block = gen_b_matrix(S, b, lam, K)
# result = rk.ExplicitRungeKuttaMethod(A_block, b_block)
# bounds = [-1/lam-100, 50, -300, 300]
# # result.plot_stability_region(bounds = bounds)
# # plt.show()

# # Test to get stability polynomial
# print(result)
# stab = result.stability_function()[0]


# # Uses stability from polynomial above as domain to sample values
# cs_arr = stab.coeffs
# cs_arr = np.array(cs_arr, dtype=float)
# polynomial = matlab.double(cs_arr)
# N = 10
# matlab_code = f"spectrum_from_polynomial({polynomial},{N});"
# # matlab_code = f"Gen_Discrete_Values({polynomial},{N});"
# q = eng.eval(matlab_code, nargout=1)



eng.quit()
print("Finished")
end = time.time()
print('This took', end-start, 'seconds')