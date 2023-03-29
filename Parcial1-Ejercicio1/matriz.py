#Ignacio Alvarado Reyes A01656149
import numpy as np
import sys

def esPrimo(n):
    if (n % 2 == 0):
        return False
    for i in range(3, int(n**0.5 + 1), 2):
        if (n % i == 0):
            return False
    return True

m=0
while m<3:
    m = int(input("Dame el valor m de la dimensión de la matriz cuadrada, mayor o igual a 3: "))

matriz = np.zeros((m,m))
numTodos= m*m
elementos=[2]
num = 3

while (len(elementos) < numTodos):
    if(esPrimo(num)):
        elementos.append(num)
    num = num + 2
    
indiceElem=0

for i in range(m):
    for j in range(m):
        matriz[i][j]= elementos[indiceElem]
        indiceElem+=1
indiceElem = 0
suma=0
indiceB = 0

for i in range(m):
    while indiceB< m:
        suma+= matriz[i][indiceB]
        indiceB+=1
    indiceElem+= 1
    indiceB = indiceElem

maximo= len(str(int(matriz.max())))

print()
print("La matriz A de números primos consecutivos es:")
print()
fila = -1

for i in range(m):
    for j in range(m):
        num= str(int(matriz[i][j]))
        indi= i
        indj=j
        lo= len(num)
        if(lo<maximo):
            for j in range(maximo-lo):
                num+=" "
        if(indj>fila):
            print("\033[4m{}\033[0m".format(num), end=" ")
        else:
            print(num, end=" ")
    fila+=1
    print()
    
print()  

print("La suma de los elementos de la matriz diagonal superior es: " + str(int(suma)))