import numpy as np

import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

step_size = 1
num_steps=100

walks = [[0,0,0]]
directions = [[0],[1],[2],[0,1],[0,2],[1,2],[0,1,2]]
for step in range(num_steps):
    walk = np.zeros(3)
    move_in_direct = np.random.choice(directions)
    for direction in move_in_direct:
        move_pos_or_neg = np.random.choice([-1,1])
        walk[direction] = move_pos_or_neg*step_size
    walks.append(np.array(walks[-1])+walk)

walks = np.transpose(walks)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(*walks)
ax.plot3D(walks[0][0],walks[1][0],walks[2][0],marker='o',color='black')
ax.plot3D(walks[0][-1],walks[1][-1],walks[2][-1],marker='o',color='red')
plt.show()
