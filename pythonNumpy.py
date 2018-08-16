import numpy as np

#Semilla al aleatorio
rand = np.random.RandomState(42)

x = rand.randint(100, size= 10)

print(x)
print(x[0], x[5])

ind = [3, 4, 8]
print(x[ind])

ind = np.array([[1, 7], [4, 5]])
print(x[ind])

bool_index = (x > 50)
print(bool_index)

print(x[x > 80])
