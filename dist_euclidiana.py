""" from math import sqrt

def point_distance(x1,y1,x2,y2):
  x = (x1 - x2)*(x1 - x2)
  y = (x1 - x2)*(x1 - x2)
  return sqrt(x+y)

def dist_euclidiana(V1, V2):
  points = len(V1)
  distances = []
  for i in range(points):
    for k in range(points):
      if i != k:
        distances.append(point_distance(V1[i], V2[i], V1[k], V2[k])) """

# itero por cada punto P
#   itero por cada punto diferente a P y calculo su distancia respecto a P
#   almaceno cada distancia calculada 
# Determino la menor distancia y la retorno

import math

def dist_euclidiana(V1,V2):
  menor = 100000000000
  for i in range(len(V2)):
    for j in range(len(V2)):
      if i!=j:
        x=(V1[i]-V1[j])**2
        y=(V2[i]-V2[j])**2
        sum=x+y
        d=math.sqrt(sum)
        if d < menor:
          menor=d
          
  return menor  

print(dist_euclidiana([3,4,5,2],[5,3,1,1]))
print(dist_euclidiana([2,4,5,8,6],[3,4,4,6,3]))