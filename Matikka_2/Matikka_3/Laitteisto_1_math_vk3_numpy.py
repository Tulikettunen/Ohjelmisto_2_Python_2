import numpy as np
import numpy.linalg as la

print("Eka tehtävä")

A = np.array([[-1, 2],[3, -5]])
B = np.array([[2,0],[-1,4]])

print(A)
print(B)
print()

print(2*A + 3*B)
print()
print(A -B)

print("Toka tehtävä")



D = np.array([[5, 3], [2, 1]])
F = np.array([[9], [4]])

X = la.inv(D).dot(F)

print(f"Answare a): \n{X}")

G = np.array([[2, 1, 1], [1, 3, 1], [2, 1, 2]])
H = np.array([[6], [2], [9]])

Z = la.inv(G).dot(H)
print(f"Answare b): \n{Z}")

I = np.array([[1, 1, 3], [3, 1, 1], [2, 1, 2]])
J = np.array([[-1], [5], [2]])

try:
       K = la.inv(I).dot(J)
       print(f"Answare c): \n{K}")
except la.LinAlgError:
       print("Error in answare c)")
