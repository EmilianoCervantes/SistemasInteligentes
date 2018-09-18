from estructuras import *


'''def bsV03(g, s, m):
	frontera = Cola()
	frontera.put(s)
	anteriores = {}
	anteriores[s] = None
	
	while not frontera.esVacia():
		actual = frontera.get()
		if actual == m:
			break
		for n in g.vecinos(actual):
			if n not in anteriores:
				frontera.put(n)
				anteriores[n] = actual
	
	return anteriores'''
# Sólo es sustituir lo del grafo con cola sencilla por el metodo nuevo
# de cola priorizada que esta en estructuras
def bsV03(g, s, m):
	frontera = ColaPriorizada()
	frontera.put(0, s)
	anteriores = {}
	anteriores[s] = None
	
	while not frontera.esVacia():
		actual = frontera.get()
		if actual == m:
			break
		for n in g.vecinos(actual):
			if n not in anteriores:
				sumaGrafo = g.costo(actual, n)
				frontera.put(sumaGrafo, n)
				anteriores[n] = actual

	return anteriores

def main():
	g = Grafo()
	with open("espana.txt") as f:
		for l in f:
			(c1, c2, c) = l.split(',')
			g.agregarAristaPeso(c1, c2, c)
	
	print(g)
	'''
	g.aristas ={
	'A': ['B'],
	'B': ['A','C','D'],
	'C': ['A'],
	'D': ['E','A'],
	'E': ['B'],
	}
	print(bsV03(g,'D','B'))'''


if __name__ == '__main__':
	main()
