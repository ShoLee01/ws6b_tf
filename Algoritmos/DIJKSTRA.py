#Implementación del algoritmo de dijkstra

import heapq as hp

def dijkstra(G, s):
  n = len(G)
  visited = [False]*n
  path = [-1]*n
  cost = [math.inf]*n
  cost[s] = 0
  queue = [(s, 0)]
  while queue:
    _,u = hq.heappop(queue)
    if visited[u]:continue
     visited[u] = True
     for v,w in G[u]:
        f = w + 1
        if f < cost[v]:
          cost[v] = f
          path[v] = u
          hq.heappush(queue, (v, f))

  return path, cost
