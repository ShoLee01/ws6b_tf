## PRIM Algorithm
```
def prim(G):
  n = len(G)
  visited = [False]*n
  path = [-1]*n
  cost = [math.inf]*n
  q = [(0, 0)]
  while q:
    _, u = hq.heappop(q)
    if not visited[u]:
      visited[u] = True
      for v, w in G[u]:
        if not visited[v] and w < cost[v]:
          cost[v] = w
          path[v] = u
          hq.heappush(q, (w, v))

  return path, cost
```

 ## Análisis Asintótico

- Establecer / obtener una etiqueta de vértice / borde lleva O(1)tiempo
- Cada vértice está etiquetado dos veces
  - una vez como SIN EXPLORAR
  - una vez como VISITADO
- Cada borde se etiqueta dos veces
  - una vez como SIN EXPLORAR
  - una vez como DESCUBRIMIENTO o ATRÁS
- El método incidenteEdges se llama una vez para cada vértice
- DFS se ejecuta a O(n + m)tiempo siempre que el gráfico esté representado por la estructura de la lista de adyacencia
- Recordar que Σv deg(v) = 2m


## Conclusiones

- El proceso es como sigue: visitar el nodo inicial y ponerlo en la pila, ahora para ver los siguientes nodos a visitar sacamos el nodo tope de la pila y vemos sus adyacentes, los que no han sido visitados los insertamos en la pila. El proceso se repite hasta que la pila se encuentre vacía ( se han visitado todos los nodos ).
