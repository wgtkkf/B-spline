# knot vector generator
# Coded by Takuro TOKUNAGA
# Last modified: March 21 2022

import numpy as np

# knot vector
def kntvctr(arg_m, arg_n):
    uvector=np.zeros((arg_m), dtype='float64')

    for i in range(0, arg_m):
        if i < arg_n+1:
            uvector[i] = 0

        elif i >= arg_m-arg_n-1:
            uvector[i] = arg_m-1-2*arg_n
        else:
            uvector[i] = i-arg_n

    return uvector/uvector[arg_m-1]
