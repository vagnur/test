import numpy as np

import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

step_size = 1
num_steps=1000

walks = [[0,0,0]]
for step in range(num_steps):
    walk = np.zeros(3)
    move_in_direct = np.random.choice(3)
    move_pos_or_neg = np.random.choice([-1,1])
    walk[move_in_direct] = move_pos_or_neg*step_size
    walks.append(np.array(walks[-1])+walk)

walks = np.transpose(walks)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(*walks)
plt.show()
