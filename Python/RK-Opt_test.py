from nodepy import rk, semidisc
import numpy as np
import matplotlib.pyplot as plt
import nodepy.rooted_trees as rt 
import nodepy.convergence as cv 
from nodepy import ivp
from nodepy import *
import matlab.engine

# A = np.array([[0,0,0],[1.5,0.5,0],[0,1.,0]])
# b = np.array([0,0.5,0.5])
# rk22 = rk.ExplicitRungeKuttaMethod(A,b)
# print(rk22)
# rk22.plot_stability_region()

# rk4 = rk.loadRKM('RK44')
# print(rk4) # Prints the Butcher tableau for the method

# rk4.plot_stability_region()
# plt.show()

# eng = matlab.engine.connect_matlab(name=None)
eng = matlab.engine.start_matlab()

eng.addpath(r'PATH')
test = eng.sqrt(4.0)
print(test)

# Example Butcher tableau for a given A matrix and b vector
def butcher_test():
    a = 0.25
    p = 4
    A = np.array([[0,0,0,0],[a,0,0,0],[a,a,0,0],[a,a,a,0]])
    # b = np.array([[0.5],[a],[a],[0]])
    b = np.array([0.5,a,a,0])
    # b = np.transpose(b)
    c = np.array([[0],[a],[2*a],[3*a]])
    # A = matlab.double(A.tolist())
    # b = matlab.double(b.tolist())
    # c = matlab.double(c.tolist())
    print(A.shape, b.shape)
    # b_test = eng.oc_butcher(A,b,c,p)
    b_test = rk.ExplicitRungeKuttaMethod(A,b)
    print(b_test)

    return None

# Converts non_matlab.double to matlab.double
def to_Matlab_Double(data):
    if not isinstance(data, matlab.double):
        try:
            matlab_data = matlab.double(data)
            return matlab_data
        except Exception as e:
            print(f"Error converting to matlab.double: {e}")
            return None
    else:
        return data
    
def to_MD(input):
    if not isinstance(input, matlab.double):
        try:
            numpy_array = np.array(input, dtype=float)
            matlab_data = matlab.double(numpy_array.tolist())

            return matlab_data
        except Exception as e:
            print(f"Error converting to matlab.double: {e}")
            
            return None
    else:
        return input

# Returns the order and Butcher tableau
def Butcher(A,b,c,p):
    # A = matlab.double(A.tolist())
    # b = matlab.double(b.tolist())
    # c = matlab.double(c.tolist())

    order = eng.check_RK_order(A,b,c)
    print('The order is ', order)

    B_t = eng.oc_butcher(A,b,c,p)
    print('The Butcher Tableau is')
    print(B_t)

# Extracts and returns values from rk_opt matlab function
def rk_opt_super(s, p, method, objective, **kwargs):
    rk = eng.rk_opt(s, p, method, objective, **kwargs)
    A = rk.get('A')
    b = rk.get('b')
    c = rk.get('c')
    # p = rk.get('p')

    r = rk.get('r')
    errcoeff = rk.get('errcoeff')
    v_opt = rk.get('v_opt')
    alpha_opt = rk.get('alpha_opt')
    beta_opt = rk.get('beta_opt')

    return [A,b,c,r, errcoeff, v_opt, alpha_opt, beta_opt]


rk_super = rk_opt_super(4,4,"erk","ssp")
# rk_super = eng.rk_opt(4,1,"erk","ssp")
# print(rk_super)
A = rk_super[0]
b = rk_super[1]
A = np.asarray(A)
b = np.asarray(b)
b = np.squeeze(b)
# print(A.shape, b.shape)
left = -20
right = 10
bottom = -10
top = 10
bounds = [left, right, bottom, top]
rk_super_test = rk.ExplicitRungeKuttaMethod(A,b)
print(rk_super_test)
rk_super_test.plot_stability_region(bounds = bounds)
plt.show()

# c = rk_super[2]
# p = rk_super[3]
# print('A', A)
# print('b', b)
# print('c', c)
# print('p', p)

# print(type(p))

# Butcher(A,b,c,p)
# B_T = eng.oc_butcher(A,b,c,p)
# print('The Butcher tableau is')
# print(B_T)




# butcher_test()






eng.quit()



print('Finished')