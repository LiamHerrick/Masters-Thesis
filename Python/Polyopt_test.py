from nodepy import rk
import numpy as np
import matplotlib.pyplot as plt
from nodepy import *
import matlab.engine



eng = matlab.engine.start_matlab()
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
# print('Previous h was 0.13259862899780273')
    
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