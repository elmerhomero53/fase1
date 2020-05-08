# -*- coding: utf-8 -*-
"""
Created on Mon May  4 10:41:00 2020
@author: jefe de jefes
"""

import pandas as pd
import numpy as np

url = "https://forms.gle/ZvXUaycQtQVJLUQg8"
ans = "no"

while "si" not in ans:
    print("Por favor, llene la siguiente encuesta:\n ",url)
    ans = input("ya la lleno? ingrese si cuando ya la haya llenado por favor\n")

url = 'https://docs.google.com/spreadsheets/d/1AjZpofZv3Y5U6QRUFtpI_XQgvjJpWXk_6oxGnb2te3o/export?format=csv&gid=1067477951'

data = pd.read_csv(url)

data = data.drop(columns=['Timestamp'])

## df to npndarray

#data = data.replace('no lo conozco',np.nan)

dataMatrix = data.to_numpy()

def GradientD(fila,col,verd):
    fila=fila+0.1*col*(verd-np.dot(fila,col))
    col=col+0.1*fila*(verd-np.dot(fila,col))
    return(fila,col)
    
f,c = np.shape(dataMatrix)

caracteristicas = 10 ##caracteristicas de restaurantes

u=np.random.rand(f,caracteristicas)
v=np.random.rand(caracteristicas,c)

for k in range(1000):###NUMERO DE ITERACIONES
    for i in range(f):
        for j in range(c):
            if isinstance(dataMatrix[i][j], (int,float)):
                fila=u[i]
                col=v[:,j]
                fila,col=GradientD(fila,col,dataMatrix[i][j])
                u[i]=fila
                v[:,j]=col

prediccion = np.dot(u,v).astype(int)

print('Prediccion:\n ',prediccion)
print('\nOriginal:\n',dataMatrix)

ultimo = prediccion[-1]

ultra = []

for i in range(len(dataMatrix[-1])):
    if dataMatrix[-1][i]=='no lo conozco':
        ultra.append(i)

print('Se le recomienda ir a los siguientes restaurantes: \n')

for n in ultra:
    if ultimo[n]>=np.mean(ultimo):
        print(data.columns[n])
    if ultra==[]:
        print('Ya conoce todos los restaurantes')