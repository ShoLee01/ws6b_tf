# Problema VRP
### El problema de enrutamiento de vehículos (VRP, por sus siglas en inglés) es un problema de optimización combinatoria  qué pregunta "¿Cuál es el conjunto óptimo de rutas para una flota de vehículos que debe satisfacer las demandas de un conjunto dado de clientes?". Es una generalización del conocido el problema del viajante (TSP, por sus siglas en inglés). La primera definición aparece en un artículo de  George Dantzig y John Ramser en 1959, en donde plantea una aproximación algorítmica y fue aplicado para entregas de gasolina. El problema, requiere la entrega de cierto producto, almacenado en un único local, a los clientes los cuales poseen cierta demanda; el objetivo fundamental es minimizar el coste total de las rutas trazadas. En 1964, Clarke y Wright mejoraron la aproximación de Dantzig y Ramser utilizando una aproximación “greedy” conocido como algoritmo de ahorros.

### Determinar la solución óptima es un problema NP-duro de  optimización combinatoria. Las implementaciones más utilizadas para resolver el problema se basan en heurísticas debido a que para grandes instancias del problema, que como sucede en ejemplos reales, producen buenos resultados. El VRP tiene muchas aplicaciones obvias en industrias. De hecho, el uso de programas de optimización puede dar ahorros de 5% a una compañía cuando el transporte es normalmente un componente significativo del coste de un producto (10%) - de hecho, el sector de transporte hace 10% de PIB de la UE. Consiguientemente, cualesquier ahorros crearon por el VRP.

# Marco Teórico
### •    Python: lenguaje interpretado multipropósito de alto nivel. Su diseño hace uso de una sintaxis simple y facil de aprender con énfasis en la legibilidad del código. Ofrece múltiples librerías y promueve la modularidad del código
### •    Algoritmo: proceso o conjunto de reglas a ser seguido para realizar cálculos u otro tipo de solución de problemas
### •    Vehicle Routing Problem (VRP): problema de optimización y programación definido por el siguiente enuncidado: ¿Cuál es el conjunto de rutas óptimo a realizar para una flota de vehículos con el fin de hacer entregas a un conjunto determinado de clientes? El fin de este problema es el de reducir los costos.

# Grafo generado por Dataset
```
G, identificador = create_city(n_town)
warehouses = pd.read_csv("almacenes.csv", header=None).to_numpy()
houses = pd.read_csv("puntos_entrega.csv", header=None).to_numpy()
plt.subplots(figsize=(10, 10))
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
plt.scatter(warehouses[:, 0], warehouses[:, 1],color='red')
plt.scatter(houses[:, 0], houses[:, 1],color='blue')
```
![Imagen del grafo](https://cdn.discordapp.com/attachments/893982069846335513/914281208945467402/unknown.png)

# Algoritmo con Prim - Miguel Angel Alfaro Gonzales

### El algoritmo de Prim es un algoritmo de la teoría de grafos que encuentra un árbol de expansión mínima para un grafo ponderado conexo. Esto significa que se encuentra un subconjunto de las aristas que forma un árbol que incluye todos los nodos, donde el total peso de todas las aristas en el árbol se reduce al mínimo.  Si el gráfico no está conectado, entonces sólo se encuentra un mínimo  árbol de expansión para uno de los componentes conectados.

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

# Algoritmo Dijkstra - Dino Iván Pérez Vásquez
### El Algoritmo de Dijkstra, también denominado Algoritmo de caminos mínimos, es un modelo que se clasifica dentro de los algoritmos de búsqueda. Su objetivo, es determinar la ruta más corta, desde el nodo origen, hasta cualquier nodo de la red. Su metodología se basa en iteraciones, de manera tal que, en la práctica, su desarrollo se dificulta a medida que el tamaño de la red aumenta, dejándolo en clara desventaja, frente a métodos de optimización basados en programación matemática.

```
def Dijkstra_diccionario(G,S):
  visited,path,cost = {},{},{}
  for i in G.keys():
    visited[i],path[i],cost[i] = False,None,math.inf

  cost[s] = 0
  Cola = [(0,S)]
  while len(Cola)>0:
    g_u,u = hp.heappop(Cola)
    if visited[u]:continue
    visited[u] = True
    for v in G[u]:
      f = g_u+1
      if cost[v]>f:
        cost[v] = f
        path[v] = u
        hp.heappush(Cola,(f,v))

  return path
```

# Algoritmo BFS - Erick Alonso Brocca Hernandez
### Una búsqueda en anchura (BFS) es un algoritmo de búsqueda para lo cual recorre los nodos de un grafo, comenzando en la raíz (eligiendo algún nodo como elemento raíz en el caso de un grafo), para luego explorar todos los vecinos de este nodo. A continuación, para cada uno de los vecinos se exploran sus respectivos vecinos adyacentes, y así hasta que se recorra todo el grafo. Cabe resaltar que, si se encuentra el nodo antes de recorrer todos los nodos, concluye la búsqueda.

```
def bfs(G, s):
  n = len(G)
  visited = [False]*n
  parent = [None]*n
  queue = [s]
  visited[s] = True

  while queue:
    u = queue.pop(0)
    for v in G[u]:
      if not visited[v]:
        visited[v] = True
        parent[v] = u
        queue.append(v)

  return parent
```
# Algoritmo Bellman Ford - Sebastian Alonso Gonzales Sotomayor
### El algoritmo de Bellman-Ford genera el camino más corto en un grafo dirigido ponderado (en el que el peso de alguna de las aristas puede ser negativo). El algoritmo de Dijkstra resuelve este mismo problema en un tiempo menor, pero requiere que los pesos de las aristas no sean negativos, salvo que el grafo sea dirigido y sin ciclos. Por lo que el Algoritmo Bellman-Ford normalmente se utiliza cuando hay aristas con peso negativo. Este algoritmo fue desarrollado por Richard Bellman, Samuel End y Lester Ford.

```
def bellmanFord(G, s):
  n = len(G)
  cost = [float('inf')]*n
  cost[s] = 0
  path = [-1]*n
  for _ in range(n-1):
    for u in range(n):
      for v, w in G[u]:
        if cost[u] + w < cost[v]:
          cost[v] = cost[u] + w
          path[v] = u
  for u in range(n):
    for v, w in G[u]:
      if cost[u] + w < cost[v]:
        return None, None
  return path, cost
```
# Resultado final 
![Imagen del grafo](https://cdn.discordapp.com/attachments/893982069846335513/914214095102832790/descarga.png)
