## Brute force algorithm
```
procedimiento Burbuja(a(0),a(1),a(2),a(n-1))
	i ← 1 
	repetir
		i ← 1 + i
		ordenado <- si
		para j ← 0 hasta n-i hacer
			si a(j) > a(j+1) entonces
				ordenado ← no
				aux ← a(j)
				a(j) ← a(j+1)
				a(j+1) ← aux
			fin si
		fin para
	hasta que (i < n) && (ordenado = si)
fin procedimiento 
```