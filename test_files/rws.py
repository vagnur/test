import numpy as np
import random

import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

step_size_r = 1
step_size_theta = np.pi / 10
step_size_phi = 2*np.pi / 100
limits =[[-100,100],[0,np.pi],[0,2*np.pi]]

walks = [[50,np.pi/2,np.pi]]
directions = [[1,0,0],[0,1,0],[0,0,1],[1,1,0],[1,0,1],[0,1,1],[1,1,1]]
while(walks[-1][0] > limits[0][0] and walks[-1][0] < limits[0][1] and walks[-1][1] > limits[1][0] and walks[-1][1] < limits[1][1] and walks[-1][2] > limits[2][0] and walks[-1][2] < limits[2][1]):
    walk = np.zeros(3)
    move_in_direct = random.choice(directions)
    move_pos_or_neg = np.random.choice([-1,1])
    walk[0] = move_pos_or_neg*step_size_r*move_in_direct[0]
    move_pos_or_neg = np.random.choice([-1,1])
    walk[1] = move_pos_or_neg*step_size_theta*move_in_direct[1]
    move_pos_or_neg = np.random.choice([-1,1])
    walk[2] = move_pos_or_neg*step_size_phi*move_in_direct[2]
    walks.append(np.array(walks[-1])+walk)

walks = np.transpose(walks)
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(*walks)
ax.plot3D(walks[0][0],walks[1][0],walks[2][0],marker='o',color='black')
ax.plot3D(walks[0][-1],walks[1][-1],walks[2][-1],marker='o',color='red')
plt.show()
