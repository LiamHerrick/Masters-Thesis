from nodepy import rk, semidisc
import numpy as np
import matplotlib.pyplot as plt
import nodepy.rooted_trees as rt 
import nodepy.convergence as cv 
from nodepy import ivp
from nodepy import *
import matlab.engine



eng = matlab.engine.start_matlab()
eng.addpath(r'C:\Users\herri\OneDrive\Documents\Groningen\Thesis\Scripts\Matlab')
eng.addpath(r'C:\Users\herri\OneDrive\Documents\Groningen\Thesis\Scripts\Matlab\RK-coeff-opt')
eng.addpath(r'C:\Users\herri\OneDrive\Documents\Groningen\Thesis\Scripts\Matlab\RKtools')
eng.addpath(r'C:\Users\herri\OneDrive\Documents\Groningen\Thesis\Scripts\Matlab\polyopt')
eng.addpath(r'C:\Users\herri\OneDrive\Documents\Groningen\Thesis\Scripts\Matlab\am_radius-opt')
test = eng.sqrt(4.0)
print(test)


try:
    N = 6400
    s = 4
    p = 4
    matlab_code = f"opt_poly_bisect(spectrum2('gap',{N}),{s},{p},'chebyshev');"
    [h, poly_coeff] = eng.eval(matlab_code,nargout=2)
    print('The maximum stable time step is', h)
except Exception as e:
    print(f"There was an error with: {e}")
poly_coeff = np.asarray(poly_coeff)
print('h is', h)
# print(type(poly_coeff))
print('poly_coeff has size', poly_coeff.shape, 'and is \n', poly_coeff)
print('Previous h was 0.13259862899780273')
    
# try:
#     s = 4
#     p = 4
#     # lam = eng.spectrum2("gap", 500)
#     [h, poly_coeff] = eng.opt_poly_bisect(eng.spectrum2("gap",500),4,4,"chebyshev")
#     print('h is', h)
#     print('coeffs are', poly_coeff)
# except Exception as e:
#     print(f"There was an error with: {e}")


eng.quit()
print("Finished")