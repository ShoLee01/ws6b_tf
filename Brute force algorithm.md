## Brute force algorithm
```
procedimiento Burbuja(a(0),a(1),a(2),a(n-1))
	i ← 1 
	repetir
		i ← 1 + i
		ordenado <- si
		para j ← 0 hasta n-i hacer
			si a(j) > a(j+1) entonces
				ordenado ← no
				aux ← a(j)
				a(j) ← a(j+1)
				a(j+1) ← aux
			fin si
		fin para
	hasta que (i < n) && (ordenado = si)
fin procedimiento 
```
![image](https://upload.wikimedia.org/wikipedia/commons/3/37/Bubble_sort_animation.gif)

## Análisis Asintótico
- La complejidad del algoritmo Bfs depende del recorrido que ejecuta, si hace un recorrido total del grafo al que se le esta aplicando Bfa seria O(n) donde n representa el numero   de nodos.
 - Este analisis tambien varia dependiendo de su representacion , ya sea por listas de adyacencias o matrices de adyacencia.
     - **Lista de adyacencia:** cuando el grafo es presentado mediante listas de adyacencia, todos sus nodos mantienen una lista de sus bordes adyacentes. De esta manera mediante la lista de adyacencia sabremos todos sus vecinos al hacerle un recorrido unico.
          - **Grafo dirigido:** al ser un grafo dirigido su lista de adyacencia de cada nodo dan una suma total de A, donde A representa el numero de aristas existentes en el grafo dando como resultado una complejidad de O(n+A).
          - **Grafo no dirigido:** en este caso al ser un grafo no dirigido  su borde aparece dos veces, a pesar de esto el equivalente en analisis de tiempo seria igual al del grafo no dirigido dando como resultado O(n+A)
     - **Matriz de adyacencia cuadrada:** En este caso se recorre una fila  de longitud igual al numero de filas o columnas de la matriz(esta se asume que es cuadrada) para hallar todas las aristas de esta. Debemos tener en cuenta que  en una matriz de adyacencia cada fila es equivalente al nodo del grafo . Su analisis de tiempo en este caso seria de O(c^2) donde c representa el numero de filas o culumnas de la matriz.
 ## Conclusiones
 La complejidad de nuestro algoritmo BFS depende mucho del recorrido que ejecute, depende de la estructura de datos que se use en la representacion del grafico. Por esta razon no se puede definir con exactitud un tiempo asintotico para nuestro proyecto , pero si llegar a diferentes conclusiones dependiendo de su uso y graficacion del problema.
