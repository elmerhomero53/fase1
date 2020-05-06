# -*- coding: utf-8 -*-
"""
Created on Mon May  4 10:41:00 2020

@author: jefe de jefes
"""

import networkx as nx
import pandas as pd
import math as m

G = nx.DiGraph()

fn = 'ratings.xlsx'
data = pd.read_excel(fn)
data = data.drop(columns=['Timestamp'])

## df to npndarray

dataMatrix = data.to_numpy()

import numpy as np

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

print('Se le recomienda ir a los siguientes restaurantes: \n')
print('Recomendados: ')
for i in range(len(ultimo)):
    if ultimo[i] >= 4:
        ultra.append(i)
for n in ultra:
    print(data.columns[n])



