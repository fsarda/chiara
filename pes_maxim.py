def pes_maxim(V,M):

  # Obtener tamanio de la lista
  size = len(V)
  
  # Verificamos las condiciones base
  # 1) la lista tiene al menos un elemento
  if(size < 1):
    return 0

  # Verificamos que M esta en el rango correcto
  if( 1 < M > size ):
    return 0

  # Calculamos el resultado
  result = 0 #Valor para acumular la suma
  V.sort(reverse=True) # ordenamos la lista de mayor a menor

  # Sumamos los elementos desde 1 hasta la posicion M
  for i in range(M):
    result += V[i]

  # retornamos el resultado calculado
  return result

#deberia ser 15
print(pes_maxim([1,2,3,4,5,6], 3))

#deberia ser 3
print(pes_maxim([0,0,0,0,0,1,2], 7))

#deberia ser 0
print(pes_maxim([0,0,0,0,0,1,2], -1))

#deberia ser 0
print(pes_maxim([1,2,3,4,5,6], 15))