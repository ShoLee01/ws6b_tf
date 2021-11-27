# Sebastian Alonso Gonzales Sotomayor

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

# Función para interpretación el grafo

```
def structure_bellmanFord(grupo, plt=None, town=80):
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
  path, cost = bellmanFord(grafo, len(node) - 1)
  if(plt == None): return NodeShow(grafo, weighted=True, path=path, labels=label)
  else: 
    for i in range(len(path)):
      nodefir = get_cod(int(label[i]), town)
      nodefsec = get_cod(int(label[path[i]]), town)
      plt.plot([nodefir[0], nodefsec[0]], [nodefir[1], nodefsec[1]])
```
 ### Visualización del grafo interpretado
![image](https://user-images.githubusercontent.com/66757138/143722736-438c7c19-a532-4f73-aa94-d4a3e187ccaf.png)
