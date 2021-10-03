## DFS Algorithm
```
procedimiento DFS(grafo &g,int s){
    nodoVisitado[s] ← true
    procesarNodo(s);
    list<int>::iterator it

    para (it=g.lados[s].begin(); it!← g.lados[s].end(); ++it) entonces
        si (!nodoVisitado[*it]) entonces
            nodoPadre[*it] ← s
            DFS(g,*it)
        fin si
	si no(!nodoProcesado[*it]) entonces
            procesarLado(s,*it)
        fin si
    fin para
    nodoProcesado[s] ← verdadero
fin procedimiento 
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

- El concepto es el similar que BFS solo que se cambia la Cola por una Pila, el proceso es como sigue: visitar el nodo inicial y ponerlo en la pila, ahora para ver los siguientes nodos a visitar sacamos el nodo tope de la pila y vemos sus adyacentes, los que no han sido visitados los insertamos en la pila. El proceso se repite hasta que la pila se encuentre vacía ( se han visitado todos los nodos ).
