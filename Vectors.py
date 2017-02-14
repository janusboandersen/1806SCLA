#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 14:27:19 2017

@author: janusboandersen
"""

import numpy as np

# Column vectors
v = np.arange(2,5).reshape((3,1))
w = np.ones(3).reshape((3,1))

#dot product
print("Column vector dot product vT * w: ", np.dot(v.T,w))


# row vectors
v = np.arange(2,5)
w = np.ones(3)
u = 2*v + 3*w

#dot product
print("Row vector dot product v * w: ", np.dot(v,w))

print("Linear combination of row vectors: ", u)

print("multiplication : ", v.T*w)

V = np.matrix("1, 2").T
print(V)
