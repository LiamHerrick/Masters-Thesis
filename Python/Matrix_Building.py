from nodepy import rk
import numpy as np
import matplotlib.pyplot as plt
from nodepy import *


def PFEasRK(lam, K):
    # A
    A = np.zeros([K+1,K+1])
    counter = 0
    for i in range(1, K+1):
        for j in range(counter+1):
            A[i,j] = 1
        
        counter +=1
    A *= lam

    # b
    b = np.ones([K+1,1])
    b[K] = (1 / lam) - K
    b *= lam

    return [A, b]

def get_c_values(A, b):
    method = rk.ExplicitRungeKuttaMethod(A,b)
    
    return method.c

def allmost_zero_mat(S, lam, K, A, b, L):
    c = get_c_values(A, b)
    Z = np.zeros([K+1,K+1])
    Z[:,-1] = ((c[S]/lam) - (K+1))*(A[S,L]/c[S])
    Z *= lam
    
    return Z

def gen_lam_mat(S, lam, K, A, b):
    c = get_c_values(A, b)
    lam_mat = np.ones([K+1,K+1])
    lam_mat[:,-1] = 1 + ((c[S-1]/lam) - (K+1))*(A[S-1,0]/c[S-1])
    lam_mat *= lam
    
    return lam_mat

def gen_zeros(K):
    empty_mat = np.zeros([K+1,K+1])

    return empty_mat

def gen_zeros_vec(K):
    empty_vec = np.zeros([K+1])

    return empty_vec

def b1_vec(b, lam, K):
    b1 = np.ones([K+1])
    b1[K] = b[0] * ((1/lam) - (K+1)) + 1
    b1 *= lam

    return b1

def gen_b_matrix(S, b, lam, K):
    b_structure = []
    b_structure.append(b1_vec(b, lam, K))

    for i in range(1, S):
        b_list = gen_zeros_vec(K)
        b_list[K] = ((1/lam) - (K+1))*b[i]
        b_list *= lam

        b_structure.append(b_list)

    b_structure = np.concatenate(b_structure, axis=None)

    return b_structure

def gen_block_matrix(S, lam, K, A, b):
    c = get_c_values(A, b)
    block_structure = []

    matrix_list = []
    # First row of the block matrix
    for i in range(S):
        matrix_list.append(gen_zeros(K))
    matrix_list[0] = PFEasRK(lam, K)[0]
    block_structure.append(matrix_list)
    # Remove values from matrix_list
    matrix_list = []

    # Second row of the block matrix
    for i in range(S):
        matrix_list.append(gen_zeros(K))
    matrix_list[0] = gen_lam_mat(2, lam, K, A, b)
    matrix_list[1] = PFEasRK(lam, K)[0]
    block_structure.append(matrix_list)
    # Everything above this line works fine

    # Second attempt
    # Main loop for rows 2 to S
    # for i in range (2, S):
    #     matrix_list = []
    #     for j in range (S):
    #         matrix_list.append(gen_zeros(K))
    #     for j in range (i):
    #         Z = np.zeros([K+1,K+1])
    #         Z[:,-1] = lam * ((c[S-1]/lam) - (K+1))*(A[S-1,j]/c[S-1])
    #         matrix_list[j] = Z
    #         # matrix_list[j] = allmost_zero_mat(i, lam, K, A, b)
    #     matrix_list[i] = PFEasRK(lam, K)[0]
    #     matrix_list[0] = gen_lam_mat(i, lam, K, A, b)
    
    #     block_structure.append(matrix_list)


    # First attempt
    # Main loop for rows 2 to S
    # S=4, so S=[0,1,2,3]
    # This loop is for s=2,3 (0 and 1) are handled above
    for j in range(2, S):
        matrix_list = []
        for i in range(S):
            matrix_list.append(gen_zeros(K))
        for i in range(j):
            matrix_list[i] = allmost_zero_mat(j, lam, K, A, b, i) # This could be the issue (or maybe an indexing issue)
        matrix_list[j] = PFEasRK(lam, K)[0]
        matrix_list[0] = gen_lam_mat(j+1, lam, K, A, b)
    
        block_structure.append(matrix_list)

    # print(len(block_structure[0]))
    # print(len(block_structure[1]))
    block_structure = np.concatenate(block_structure, axis=1)
    block_structure = np.concatenate(block_structure, axis=1)

    return block_structure


