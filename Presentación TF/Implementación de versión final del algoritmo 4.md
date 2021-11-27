# Erick Alonso Brocca Hernandez

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

# Función para interpretación el grafo

```
def structure_bfs(grupo, plt=None, ntown=80):
  nodos = grupo["casas"]
  nodos.append(grupo["almacen"])
  label = list()
  for nodo in nodos:
    label.append(str(get_node(nodo, ntown)))
  label[-1] = str(get_node(nodo, ntown))
  grafo = [[] for _ in range(len(nodos))]
  for i, _ in enumerate(nodos):
    for j, _ in enumerate(nodos):
      if i == j: continue
      grafo[i].append((j, manhattan_distance(nodos[i], nodos[j])))
  T = Orden_par(grafo)
  n = len(grafo)
  Gp = [[] for _ in range(n)]
  for u, v, _ in T:
    Gp[u].append(v)
    Gp[v].append(u)
  path = bfs(Gp, 5)
  if(plt == None): return NodeShow(grafo, weighted=True, path=path, labels=label)
  else: 
    for i in range(len(path)):
      if path[i] == None: continue
      nodefir = get_cod(int(label[i]), ntown)
      nodesec = get_cod(int(label[path[i]]), ntown)
      plt.plot([nodefir[0], nodesec[0]], [nodefir[1], nodesec[1]])
```
 ### Visualización del grafo interpretado
 https://cdn.discordapp.com/attachments/893982069846335513/914276155719290900/unknown.png
 
