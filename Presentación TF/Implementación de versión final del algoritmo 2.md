# Miguel Angel Alfaro Gonzales

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

# Función para interpretación el grafo

```
def structure_prim(grupo, plt=None, town=80):
  node = grupo["casas"]
  node.append(grupo["almacen"])
  label = list()
  for nodo in node:
    label.append(str(get_node(nodo, town)))
  grafo = [[] for _ in range(len(node))]
  for i, _ in enumerate(node):
    for j, _ in enumerate(node):
      if i == j: continue
      grafo[i].append((j, manhattan_distance(node[i], node[j])))
  path, cost = prim(grafo)
  if(plt == None): return NodeShow(grafo, weighted=True, path=path, labels=label)
  else: 
    for i in range(len(path)):
      nodefir = get_cod(int(label[i]), town)
      nodesec = get_cod(int(label[path[i]]), town)
      plt.plot([nodefir[0], nodesec[0]], [nodefir[1], nodesec[1]])
```
 ### Visualización del grafo interpretado
 
![Imagen del grafo interpretado](https://cdn.discordapp.com/attachments/893982069846335513/914250905925349397/unknown.png)
