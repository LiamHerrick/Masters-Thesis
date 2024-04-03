import numpy as np
# from nodepy import rk

msg = 'Testing...'

print(msg)

print(np.random.randint(1,9))

import matlab.engine

# try:
#     # Start MATLAB engine
#     eng = matlab.engine.start_matlab()

#     # Display a simple message
#     print("MATLAB Engine for Python is working correctly.")

#     # Stop MATLAB engine
#     eng.quit()

# except Exception as e:
#     print(f"An error occurred: {e}")

eng = matlab.engine.start_matlab()
A = [[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]]
b = [1/6, 1/3, 1/3, 1/6]
c = [1, 1, 1]
# results_rkopt = eng.runtests('test_rkopt.m'); #table(results_rkopt)
# rk = eng.rk_opt(4,3,'erk','acc','num_starting_points',2,'np',1,'solveorderconditions',1)
rk = eng.check_RK_order(A,b,c)
eng.quit()

print('Finished')