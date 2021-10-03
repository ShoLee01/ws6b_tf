# ESPACIO DE BUSQUEDA
- Para la definicion del espacio de busqueda veamos la siguiente imagen:


![image](https://user-images.githubusercontent.com/66757138/135743505-4786dbf9-73cd-4b62-addf-69da783b8dca.png)

Nuestro estado inicial en este caso tomando como referencia la imagen seria el numero 1 y queremos llegar al punto numero 5 , y tenemos diferentes caminos por los cuales 
podemos llegar a nuestro destino. Cada camino como podemos apreciar tiene un "costo" por recorrerlo y nuestro trabajo es llegar al punto 5 con el menor costo posible de todos
los posibles caminos que podemos tomar que en este caso partiendo desde el estado inicial tenemos 3 posibles caminos para tomar que podrian ser el numero 6, 2 y 3

**Supongamos que tomamos el numero 6** que tiene un coste de 14, nuestro nuevo estado seria el numero 6 y nuestro costo total que en nuestro primer estado era 0 ahora paso a ser 14.

Ahora tenemos dos nuevos posibles escenarios dirigirnos hacia el numero 5 o ir hacia el numero 3. En este caso tomemos el camino hacia 5 que tiene un coste de 9. Al haber llegado a nuestro  punto de destino este sera considerado nuestro estado final y el costo de haberlo alcanzado tiene un total de 23

**Supongamos que tomamos el numero 3** que tiene un coste de 9, nuestro nuevo estado seria el numero 3 y nuestro costo total que en nuestro primer estado era 0 ahora paso a ser 9.

Ahora tenemos dos nuevos posibles escenarios dirigirnos hacia el numero 6 o ir hacia el numero 4. En este caso tomemos el camino hacia 6 que tiene un coste de 2. 

Ahora nuestro nuevo costo paso a ser 11 y tenemos solo un posible escenario que es el de llegar a nuestro destino final de 5 con coste 9.

Al haber llegado a nuestro  punto de destino este sera considerado nuestro estado final y el costo de haberlo alcanzado tiene un total de 20

**Supongamos que tomamos el numero 2** que tiene un coste de 7, nuestro nuevo estado seria el numero 2 y nuestro costo total que en nuestro primer estado era 0 ahora paso a ser 7.

Ahora tenemos dos nuevos posibles escenarios dirigirnos hacia el numero 3 o ir hacia el numero 4. En este caso tomemos el camino hacia 4 que tiene un coste de 15.

Ahora nuestro nuevo costo paso a ser 22 y tenemos solo un posible escenario que es el de llegar a nuestro destino final de 5 con coste 6.

Al haber llegado a nuestro  punto de destino este sera considerado nuestro estado final y el costo de haberlo alcanzado tiene un total de 28

- Luego de haber analizado unos cuantos casos de posibles caminos y costos nos quedamos con el segundo caso anteriormente explicado ya que es el camino que nos hace llegar a nuestro destino con un coste mucho menor al de los demas

# Imagen para un mejor entendimiento de los caminos tomados
![Dijkstra_Animation](https://user-images.githubusercontent.com/66757138/135743554-d109159b-c309-4dfe-8d2e-ae4dd2d69d68.gif)

# Conclusiones
- Luego de haber analizado unos cuantos casos para llegar a nuestro destino podemos afirmar que no siempre tomar el menor numero de caminos es siempre la mejor opcion debido a los costos que estos requieren
- Si aplicamos este pequeño ejemplo a nuestro proyecto podremos indicar con certeza que posee miles de escenarios posteriores al inicial pero siempre tendra un solo escenario final que es cuando se llega al destino requerido
