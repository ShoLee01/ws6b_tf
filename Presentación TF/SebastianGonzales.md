{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "AhuSZbTJfyrV"
   },
   "source": [
    "# **Algoritmo Bellman Ford - Sebastian Alonso Gonzales Sotomayor**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "zw1ICjt6_7oK"
   },
   "outputs": [],
   "source": [
    "def bellmanFord(G, s):\n",
    "  n = len(G)\n",
    "  cost = [float('inf')]*n\n",
    "  cost[s] = 0\n",
    "  path = [-1]*n\n",
    "  for _ in range(n-1):\n",
    "    for u in range(n):\n",
    "      for v, w in G[u]:\n",
    "        if cost[u] + w < cost[v]:\n",
    "          cost[v] = cost[u] + w\n",
    "          path[v] = u\n",
    "  for u in range(n):\n",
    "    for v, w in G[u]:\n",
    "      if cost[u] + w < cost[v]:\n",
    "        return None, None\n",
    "  return path, cost"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "e05H11s9A7gJ"
   },
   "outputs": [],
   "source": [
    "def structure_bellmanFord(grupo, plt=None, town=80):\n",
    "  node = grupo[\"casas\"]\n",
    "  node.append(grupo[\"almacen\"])\n",
    "  label = list()\n",
    "  for nodo in node:\n",
    "    label.append(str(get_node(nodo, town)))\n",
    "  grafo = [[] for _ in range(len(node))]\n",
    "  for i, _ in enumerate(node):\n",
    "    for j, _ in enumerate(node):\n",
    "      if i == j: continue\n",
    "      grafo[i].append((j, manhattan_distance(node[i], node[j])))\n",
    "  path, cost = bellmanFord(grafo, len(node) - 1)\n",
    "  if(plt == None): return NodeShow(grafo, weighted=True, path=path, labels=label)\n",
    "  else: \n",
    "    for i in range(len(path)):\n",
    "      nodefir = get_cod(int(label[i]), town)\n",
    "      nodefsec = get_cod(int(label[path[i]]), town)\n",
    "      plt.plot([nodefir[0], nodefsec[0]], [nodefir[1], nodefsec[1]])"
   ]
  }
 ],
 "metadata": {
  "colab": {
   "collapsed_sections": [],
   "name": "Untitled6.ipynb",
   "provenance": []
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
