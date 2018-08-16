import numpy as np

rand = np.random.RandomState(42)
x = rand.randint(100, size=100)
print(x)
#Todos los elementos, 3 versiones
print("Todos los elementos")
print(x[:])
print(x[0:])
print(x[:-1])

#Los elementos de las posiciones pares, 2 versiones
print("Elementos de posiciones pares")
print(x[::2])
print("Elementos pares version 2")
listEven = range(0, 100, 2)
print(x[listEven])

#Los elementos de las posiciones impartes, 2 versiones
print("Elementos de posiciones IMpares")
print(x[::-2])
print("Elementos IMpares version 2")
print(x[1::2])

#Los elementos mayores a 50
print("Elementos mayores a 50")
bool_index = (x > 50)
print(bool_index)

mayoresA50 = [i for i in x if i > 50]
print(mayoresA50)

#Una matriz de 5 * 5
print("Matriz de 5 x 5")
matriz5x5 = np.empty([5, 5])
print(matriz5x5)

print("Test range")

