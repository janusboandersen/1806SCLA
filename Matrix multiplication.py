#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 10:34:06 2017

@author: janusboandersen
"""

import numpy as np

#Examples in matrix multiplication using arrays
A = np.array([[1,2,3],[2,5,2],[6,-3,1]])

#Perhaps a slightly more convenient way to input the matrix
A_alternative = np.array([1,2,3,2,5,2,6,-3,1]).reshape((3,3))

print("A and A_alternative are equal?", np.all(A == A_alternative), "\n")

x = np.array([[0],[0],[2]])

b = A.dot(x)
print("Multiplication using arrays:")
print(b)


#Examples in matrix multiplication using matrices
A2 = np.matrix("1 2 3; 2 5 2; 6 -3 1")
x2 = np.matrix("0; 0; 2")

b2 = A2*x2
print("\nMultiplication using matrices:")
print(b2)


#Product by linear combination of columns
prod_lin_comb = A[:,0] * x[0][0] + A[:,1] * x[1][0] + A[:,2] * x[2][0] 
#Returns a (3)-vector


#Product by computing each row's dot product with x  (returns a 1x1 array)
b_1 = np.dot(A[0,],x)[0]
b_2 = np.dot(A[1,],x)[0]
b_3 = np.dot(A[2,],x)[0]
prod_row_dots = np.array([b_1, b_2, b_3])

#Compare
print(prod_row_dots == prod_lin_comb)
