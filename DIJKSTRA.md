## Algoritmo de Dijkstra


- El algoritmo de Dijkstra consiste en encontrar una ruta o camino óptimo entre un nodo fuente y un nodo destino, los cuales están enlazados a través de arcos que 
  poseen un cierto atributo, el cual puede ser costo, distancia, tiempo, etc. El problema del trabajo parcial puede resolverse de forma exacta a través de una gran 
  variedad de algoritmos, en este caso se usará Dijkstra.

- En nuestro caso, primero se agruparían los puntos de entrega más cercanos a cada almacén y después se procederá a calcular los caminos mínimos desde cada almacén a 
  cada punto de entrega agrupado anteriormente.Ejemplo: 

- Como de requisito tenemos que los almacenes deben estar en el rango de 50 y 100 y los puntos de entregas en el rango de 2500 y 5000. Por lo tanto, si elegimos 70 almacenes 
  y 4900 puntos de entregas.Además, sabemos que cada distribución y punto de entregas estan definidos por una posición X, Y correspondiente a un punto de la ciudad, y ha base
  de esta información se sabrá la cantidad aproximada de cada distribución, en este caso le tocara 70 entregas.Se utilizará el algoritmo de Dijsktra para calcular el camino     mínimo
  
- de cada distribución hacia sus 70 entregas.El algoritmo sería de la siguiente forma:

## Pseudocódigo

``` [python]

      DIJKSTRA (Grafo G, nodo_fuente s)       
       para u ∈ V[G] hacer
           distancia[u] = INFINITO
           padre[u] = NULL
           visto[u] = false
       costo[s] = 0
       cola = [(
       mientras que cola no es vacía hacer
           u = extraer_mínimo(cola)
           visto[u] = true
           para todos v ∈ adyacencia[u] hacer
               si no visto[v] y distancia[v] > distancia[u] + peso (u, v) hacer
                   distancia[v] = distancia[u] + peso (u, v)
                   padre[v] = u
                   adicionar(cola,(v, distancia[v])
                   
```

- El algoritmo comienza con nodo fuente en este caso llamado s en el grafo,  su costo inicial será 0 y no tendrá padre asociado, para los demás nodos las distancias son    infinitas.
  En el siguiente paso se traslada hacia los puntos entregas adyacentes y se procederá a actualizar las distancias de cada punto seleccionado. Además, uno vez hecho este paso se 
  continuará guardando en la cola de prioridad y si encuentra una mejor se extraerá de la cola que tienen guardados. El algoritmo de Dijkstra termina cuando todos los nodos  puntos 
  fueron visitados.


# **Análisis Asintótico**

- La complejidad del algoritmo de Dijkstra utilizando cola de prioridad es:
  O((|E|+|V|) log |V|)
  
- Se puede estimar la complejidad computacional del algoritmo de Dijkstra (en términos de suma y comparaciones).
- El algoritmo realiza a los más n-1 iteraciones, ya que cada iteración se añade un vértice.
- Para estimar el número total de operaciones que se llevan a cabo en cada iteración.
- Podemos identificar el nodo con la menor etiqueta entre los que no están realizando n-1 comparaciones.
  Por lo tanto, en cada iteración se realiza 2(n-1).
