import numpy as np

import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

#La idea es bien sencilla. Para cda dirección cartesiana (X,Y,Z) se obtiene un 1 o 0 (ese valor indica si se mueve o no en esa dirección) para saber el sentido, buscamos un valor entre -1 y 1, por ejemplo en X, -1 es a la izquierda y 1 a la derecha. Se debe obtener bien el tamaño del paso, ya que no puede ser agresivo para la grilla ingresada, sólo por el ejemplo lo dejamos en 1. Luego nos movemos en las 3 direcciones, pero vamos a multiplicar el paso, la dirección y la decisión de moverse o no en una dirección cartesiana, por lo que algunos valores seguirán en 0.
#Esto importa para la parte en GPU, ya que este código no generará divergencia.
step_size = 1
num_steps=200

walks = [[0,0,0]]
for step in range(num_steps):
    walk = np.zeros(3)
    #Primero obtenemos un 1 o un 0 para saber si nos movemos en esa coordenada
    move_in_direct = np.random.choice([0,1])
    #Luego obtenemos la dirección, negativa o positiva
    move_pos_or_neg = np.random.choice([-1,1])
    #Aquí deberiamos obtener el tamaño del paso tmbn, pero por ahora se omite
    #Multiplicamos los 3 valores y sumamos en esa coordenada respecto al último 
    #valor obtenido en esa coordenada
    walk[0] = move_pos_or_neg*step_size*move_in_direct
    move_in_direct = np.random.choice([0,1])
    move_pos_or_neg = np.random.choice([-1,1])
    walk[1] = move_pos_or_neg*step_size*move_in_direct
    move_in_direct = np.random.choice([0,1])
    move_pos_or_neg = np.random.choice([-1,1])
    walk[2] = move_pos_or_neg*step_size*move_in_direct
    #Aquí sumamos respecto al último paso obtenido en cada coordenada
    walks.append(np.array(walks[-1])+walk)

walks = np.transpose(walks)
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(*walks)
#En negro el inicio y en rojo el final
ax.plot3D(walks[0][0],walks[1][0],walks[2][0],marker='o',color='black')
ax.plot3D(walks[0][-1],walks[1][-1],walks[2][-1],marker='o',color='red')
plt.show()
