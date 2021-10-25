```
import csv
import numpy as np
import matplotlib.pyplot as plt
def spell_csv(headers, fields, filename):
  with open(filename, 'w') as f:   
    write = csv.writer(f)
    if headers != None: write.writerow(headers)
    write.writerows(fields)
def interpret_csv(filename):
  csv_file = list()
  with open(filename) as File:
    reader = csv.reader(File, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        if row[0] != 'x':
          row[0], row[1] = int(row[0]), int(row[1])
          csv_file.append(row)
  csv_file.sort(key = lambda x: (x[0], x[1]))
  return csv_file
warehouse = interpret_csv("almacenes.csv")
Home = interpret_csv("puntos_entrega.csv")
x, y = np.array(warehouse).T
x2, y2 = np.array(Home).T
plt.figure(figsize=(15, 15))
plt.scatter(x,y, 2, c="red")
plt.scatter(x2,y2, 2, c="blue")
plt.show()
for i, _ in enumerate(warehouse):
  warehouse[i].append("W")
for i, _ in enumerate(Home):
  Home[i].append("H")
city = list()
city.extend(warehouse)
city.extend(Home)
city.sort(key = lambda x: (x[0], x[1]))
graph = [[] for _ in city]
for i, _ in enumerate(city):
  for j, _ in enumerate(city):
    if i == j: continue
    if city[i][0] == city[j][0] or city[i][1] == city[j][1]: graph[i].append(j)
spell_csv(['x', 'y', 'type'], city, 'town.csv')
spell_csv(None, graph, 'graph.csv')
```