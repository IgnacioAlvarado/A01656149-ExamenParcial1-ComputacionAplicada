#Ignacio Alvarado Reyes

import numpy as np

matriz= [[0.25,0.15,0],
         [0.45,0.5,0.75],
         [0.3,0.35,0.25]
        ]

matrizA = np.array(matriz)

inversA= np.linalg.inv(matrizA)

resultados = np.array([1.5, 5,3])

vars = np.linalg.inv(matrizA).dot(resultados)

print(vars)