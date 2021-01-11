# itero por cada punto P
#   itero por cada punto diferente a P y calculo su distancia respecto a P
#   almaceno cada distancia calculada 
# Determino la menor distancia y la retorno

import math

def dist_euclidiana(V1,V2):
  distancias=[]
  for i in range(len(V2)):
    for j in range(len(V2)):
      if i!=j:
        x=(V1[i]-V1[j])**2
        y=(V2[i]-V2[j])**2
        sum=x+y
        d=math.sqrt(sum)
        distancias.append(d)
  
  menor=1000000000
  for e in distancias:
    if e<menor:
      menor=e
  return menor  

print(dist_euclidiana([3,4,5,2],[5,3,1,1]))
print(dist_euclidiana([2,4,5,8,6],[3,4,4,6,3]))