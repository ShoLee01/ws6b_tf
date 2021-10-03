## Bellman-Ford
   ## Bellman-Ford Pseudocodigo
``` [python]
dado un grafo dirigido G(V,E) el nodo de inicio S y el peso W de cada arista
procedimiento Bellman-Ford
   D[S]=0
   R=V-S
   C=cardinalidad(V)
   para cada nodo v hacer
       D[v]=∞
   fin
   para cada nodo i=1 hasta (C-1) hacer
       para cada arista (e1,e2) hacer
           actualizar distancia (e1,e2)
       fin
   fin
   para cada arista(e1,e2) en E hacer
       si D[e2]>D[e1]+W[e1,e2] entonces
           D[e2]=D[e1]+ W[e1,e2]
       fin
   fin
```
## Análisis Asintótico

- El algoritmo se inicializa en el primer paso tomando O(V) 
- Luego el algoritmo se repite por (V-1) veces, cada vuelta al bucle resultaria en un tiempo O(1)
- Debido a que el algoritmo visita todos las aristas E el tiempo final resilta O(V*E)
