def pes_maxim(V, M):

  maximos=[]

# Vamos a hacer esto M veces -->
  
  j=0
  while j<M:

    # i inicia en 0 y termina en la casilla len(V) - 1
    i=0
    max_local=0
    max_indice_local=0

    # Para buscar el mayor elemento
    # Voy recorriendo el vector para 
    # conseguir el siguiente elemento a sumar
    # 3,2,6,4,5

    if len(V) == 1:
      max_local = V[0]
      max_indice_local=0

    while i < len(V) - 1:
      # Comparo V[i] con V[i+1] y determino cual es mayor
      max_V=0
      max_i_V=0
      if V[i]<V[i+1]:
        max_V=V[i+1]
        max_i_V=i+1
      else:
        max_V=V[i]
        max_i_V=i

      # Actualizo el maximo local solo si el mayor determinado 
      # es mayor que el maximo local
      if max_V>max_local:
        max_local=max_V
        max_indice_local=max_i_V

      #Me muevo en una casilla
      i=i+1

    # anexo a un nuevo arreglo el elemento maximo
    # max = [6]   3,2,6,4,5
    maximos.append(max_local)

    # Elimino el maximo que ya extraje
    # max=[6]    3,2,4,5
    del(V[max_indice_local])
    j=j+1

  # Cuando hemos terminado las M iteraciones
  #max = [6,4,5]   3,2
  # Calcular la suma de todos los elementos
  # en max y retornarla

  s=0
  for i in range(len(maximos)):
    s=s+maximos[i]

  return s


#maximo=[3,4,8,6,5] V=[2]
print(pes_maxim([5], 1))
print(pes_maxim([2,3,4,8,6,5], 6))
print(pes_maxim([0,0,0,0,0,0,1], 1))