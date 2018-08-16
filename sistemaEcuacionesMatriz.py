import numpy as np

A = np.array([ [3, -9], [2, 4] ])
print(A)
b = np.array([-42, 2])

print(np.linalg.solve(A, b))

'''
z = A-^1 * b

x -2y -z = 6
2x +2y = z + 1
2z -1 = y + x
'''
print("#####")
A = np.array([ [1, -2, -1], [2, 2, -1], [-1, -1, 2] ])
B = np.array([6, 1, 1])
print(np.linalg.solve(A, B))
