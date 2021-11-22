def dijkstra(G, s):
  n = len(G)
  visited = [False]*n
  path = [None]*n
  cost = [math.inf]*n
  cost[s] = 0
  queue = [(0, s)]
  while queue:
    g_u, u = hq.heappop(queue)
    if not visited[u]:
      visited[u] = True
      for v, w in G[u]:
        f = g_u + w
        if f < cost[v]:
          cost[v] = f
          path[v] = u
          hq.heappush(queue, (f, v))

  return path, cost


def Dijkstra_modificado(almacenes,entregas,GRAFO):
  res = []
  for i in almacenes:
    camino,costo = dijkstra(G,i)
    for l in entregas:
      nodo = l
      p = [l]
      c = costo[l]
      while nodo != i:
        nodo = camino[nodo]
        p.append(nodo)
      p.reverse()
      res.append((i,l,c, p))
  return re



def dijkstra2(Almacenes,Puntos, Grafo, nodo_inicial):
  visited = {node:False for node in M}
  visitedPts = []
  camino = {node:None for node in M}
  costo = {node:math.inf for node in M}
  costo[s] = 0
  queue = [(0, s)]
  while queue:
    if len(visitedPts) == len(Pts):
      break
    g_u, u = hq.heappop(queue)
    if visited[u]:continue
    visited[u] = True
    if u in Pts:        
      visitedPts.append(1)
      for v in G[u]:
        if v not in M:
          continue
        f = g_u + 1
        if f < costo[v]:
          costo[v] = f
          camino[v] = u
          hq.heappush(queue, (f, v))

  return camino, costo
