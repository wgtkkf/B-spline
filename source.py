# Coded by Takuro TOKUNAGA
# Last modified: March 22 2022

import numpy as np
import time
import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
start = time.time()

sys.path.append('../bspline/upload/')
from knotvector import kntvctr   # import function
from basisfunction import bbasis # import function
from comments import begin, end  # import function

f0 = open('spline.txt', 'w') # read mode (input, fixed value)
f1 = open('control.txt', 'w') # read mode (input, fixed value)

# main
def main():
    begin()

    # references
    df1 = pd.read_csv('3rdOrder.txt', encoding = 'UTF8', sep=' ', header=None, names=('x [-]','y [-]'))

    # parameters
    p = 6 # number of control points
    n = 3 # order of b-spline curve
    m = p + n + 1

    # control points (x,y)
    ctrl_vctr = np.array([[0,0],[1,2],[3,2],[3,0],[5,2],[6,0]])
    #print(ctrl_vctr)
    f1.write(str(ctrl_vctr))

    # knot vector
    kv = kntvctr(m, n)
    #print(kv)

    division = 100 # division of u[0] to u[end]
    delta_t = (kv[np.int64(len(kv)-1)]-kv[0])/division
    #print(delta_t)
    graph_x = np.zeros(division+1, dtype='float64')
    graph_y = np.zeros(division+1, dtype='float64')

    t = 0
    dof = 2 # degree of freedom, x & y

    svector = np.zeros([division, dof]) # [height, width]
    #print(svector)
    svector[0] = ctrl_vctr[0]
    #print(svector[0])

    for i in range(1, division):
        t = t + delta_t
        for j in range(0, p):
            b = bbasis(kv, j, n, t) # need check
            svector[i] = svector[i] + ctrl_vctr[j]*b # need check

    for i in range(0, division):
        graph_x[i] = svector[i][0]
        graph_y[i] = svector[i][1]
        # file outputs
        f0.write(str(graph_x[i]))
        f0.write(str(' '))
        f0.write(str(graph_y[i]))
        f0.write('\n')

    # last elements
    graph_x[division] = ctrl_vctr[np.int64(len(ctrl_vctr))-1][0]
    graph_y[division] = ctrl_vctr[np.int64(len(ctrl_vctr))-1][1]

    f0.write(str(graph_x[division]))
    f0.write(str(' '))
    f0.write(str(graph_y[division]))
    f0.write('\n')

    #print(graph_x, graph_y)

    # graph display
    csfont = {'fontname':'Times New Roman'} # define font
    plt.plot(df1['x [-]'], df1['y [-]'], 'green', label="3rd order B-spline curve, extracted", marker="s", markersize=4, linestyle='None')
    plt.plot(graph_x, graph_y, 'black', label="3rd order B-spline curve, reproduced")
    plt.plot(ctrl_vctr[:, 0], ctrl_vctr[:, 1], label="Control points", linestyle='solid', marker="o", markersize=4)
    #plt.xlabel('x [-]', fontdict=None, labelpad=None, **csfont)
    #plt.ylabel('y [-]', fontdict=None, labelpad=None, **csfont)
    plt.xlabel('Number of turns [turns]', fontdict=None, labelpad=None, **csfont)
    plt.ylabel('Inner radius [mm]', fontdict=None, labelpad=None, **csfont)
    # font for legend
    font = font_manager.FontProperties(family='Times New Roman',
                                       weight='bold',
                                       style='normal', size=10)
    plt.legend(loc='upper left', prop=font) # legend
    # plot options
    #plt.xticks([0, 1, 2, 3, 4, 5, 6], **csfont)
    #plt.yticks([0, 0.5, 1.0, 1.5, 2.0, 2.5], **csfont)
    plt.savefig("graph.png") # 1. file saving (1. should be before 2.)
    plt.show()              # 2. file showing (2. should be after 1.)

    # file close
    f0.close()
    f1.close()

    end()

if __name__ == "__main__":
    main()

# time display
elapsed_time = time.time()-start
print("elapsed_time:{:.2f}".format(elapsed_time) + "[sec]")
