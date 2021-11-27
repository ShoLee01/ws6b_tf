# Dino Iván Pérez Vásquez

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

# Función para interpretación el grafo

```
def structure_dijkstra(grupo, plt=None, town=80):
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
  path, cost = dijkstra(grafo, len(node) - 1)
  if(plt == None): return NodeShow(grafo, weighted=True, path=path, labels=label)
  else: 
    for i in range(len(path)):
      nodefir = get_coord(int(label[i]), town)
      nodefsec = get_coord(int(label[path[i]]), town)
      plt.plot([nodefir[0], nodefsec[0]], [nodefir[1], nodefsec[1]])
```
 ### Visualización del grafo interpretado
 
 ![Imagen del grafo interpretado](https://discord.com/channels/893982069846335508/893982069846335513/914274722571780146/unknown.png)
