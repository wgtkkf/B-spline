# basis function generator for b-spline curve
# Coded by Takuro TOKUNAGA
# Last modified: March 21 2022

import numpy as np

# bspline basis function
def bbasis(u, j, k, t):
    w1 = 0
    w2 = 0
    #print(u)

    if k==0:
        if u[j] < t and t <= u[j+1]:
            #print("one")
            tmp = 1
        else:
            tmp = 0
            #print("zero")
    else:
        if (u[j+k+1]-u[j+1])!=0:
            w1 = bbasis(u,j+1,k-1,t) * (u[j+k+1]-t)/(u[j+k+1]-u[j+1])
            #print("w1", w1)
        if (u[j+k]-u[j])!=0:
            w2 = bbasis(u,j,k-1,t) * (t-u[j])/(u[j+k] - u[j]);
            #print("w2", w2)
        tmp = w1 + w2

    return tmp
