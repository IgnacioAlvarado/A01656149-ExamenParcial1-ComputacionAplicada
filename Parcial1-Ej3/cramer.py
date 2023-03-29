#Ignacio Alvarado Reyes A01656149

def reglaSarrus(m):
    
    return m[1-1][1-1]*m[2-1][2-1]*m[3-1][3-1] + m[2-1][1-1]*m[3-1][2-1]*m[1-1][3-1] + m[3-1][1-1]*m[1-1][2-1]*m[2-1][3-1] - m[1-1][3-1]*m[2-1][2-1]*m[3-1][1-1] - m[2-1][3-1]*m[3-1][2-1]*m[1-1][1-1] - m[3-1][3-1]*m[1-1][2-1]*m[2-1][1-1]

def obtenerVar(var,det):
    arriba= reglaSarrus(var)
    return arriba/det

matriz= [[0.25,0.15,0],
         [0.45,0.5,0.75],
         [0.3,0.35,0.25]
        ]

determinante= reglaSarrus(matriz)


matrizA=[[1.5,0.15,0],
         [5,0.5,0.75],
         [3,0.35,0.25]
        ]

A= obtenerVar(matrizA,determinante)

matrizB=[[0.25,1.5,0],
         [0.45,5,0.75],
         [0.3,3,0.25]
        ]

B= obtenerVar(matrizB,determinante)

matrizC=[[0.25,0.15,1.5],
         [0.45,0.5,5],
         [0.3,0.35,3]
        ]

C= obtenerVar(matrizC,determinante)

print("A= "+str(A)+", B="+str(B)+", C="+str(C))