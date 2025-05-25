import numpy as np

# Sistema 1: 4x - 2y + z = 11; -2x + 4y - 2z = -16; x - 2y + 4z = 17
A1 = np.array([[4, -2, 1], [-2, 4, -2], [1, -2, 4]])
b1 = np.array([11, -16, 17])

print("=== SISTEMA 1 ===")

# 1. Solución con np.linalg.solve
sol1 = np.linalg.solve(A1, b1)
print("\n1. Solución con np.linalg.solve:")
print(sol1)

# 2. Método de matriz inversa
A1_inv = np.linalg.inv(A1)
sol1_inv = A1_inv @ b1
print("\n2. Solución con matriz inversa:")
print(sol1_inv)

# 3. Método de Cramer
detA1 = np.linalg.det(A1)
A1_x = A1.copy(); A1_x[:,0] = b1
A1_y = A1.copy(); A1_y[:,1] = b1
A1_z = A1.copy(); A1_z[:,2] = b1

x = np.linalg.det(A1_x)/detA1
y = np.linalg.det(A1_y)/detA1
z = np.linalg.det(A1_z)/detA1
print("\n3. Solución con Cramer:")
print(f"x = {x}, y = {y}, z = {z}")

# 4. Descomposición LU (Doolittle)
def doolittle(A):
    n = len(A)
    L = np.eye(n)
    U = np.zeros((n,n))
    for i in range(n):
        for k in range(i, n):
            U[i,k] = A[i,k] - L[i,:i] @ U[:i,k]
        for k in range(i+1, n):
            L[k,i] = (A[k,i] - L[k,:i] @ U[:i,i]) / U[i,i]
    return L, U

L1, U1 = doolittle(A1)
print("\n4. Descomposición LU:")
print("Matriz L:")
print(L1)
print("\nMatriz U:")
print(U1)
print("\nComprobación L@U:")
print(L1 @ U1)

# Resolver usando LU
z = np.linalg.solve(L1, b1)
x_lu = np.linalg.solve(U1, z)
print("\nSolución usando LU:")
print(x_lu)

# 5. Descomposición Cholesky
def cholesky(A):
    n = len(A)
    L = np.zeros((n,n))
    for i in range(n):
        for j in range(i+1):
            s = sum(L[i,k] * L[j,k] for k in range(j))
            if i == j:
                L[i,j] = np.sqrt(A[i,i] - s)
            else:
                L[i,j] = (A[i,j] - s) / L[j,j]
    return L

try:
    L1_chol = cholesky(A1)
    print("\n5. Factorización Cholesky:")
    print(L1_chol)
    print("\nComprobación L@L.T:")
    print(L1_chol @ L1_chol.T)
except:
    print("\n5. La matriz no es simétrica definida positiva para Cholesky")

# Sistema 2: x1 + x2 + x3 = 6; x1 + 2x2 + 5x3 = 12; x1 + 4x2 + 25x3 = 36
A2 = np.array([[1, 1, 1], [1, 2, 5], [1, 4, 25]])
b2 = np.array([6, 12, 36])

print("\n\n=== SISTEMA 2 ===")

# 1. Solución con np.linalg.solve
sol2 = np.linalg.solve(A2, b2)
print("\n1. Solución con np.linalg.solve:")
print(sol2)

# 2. Método de matriz inversa
A2_inv = np.linalg.inv(A2)
sol2_inv = A2_inv @ b2
print("\n2. Solución con matriz inversa:")
print(sol2_inv)

# 3. Método de Cramer
detA2 = np.linalg.det(A2)
A2_x = A2.copy(); A2_x[:,0] = b2
A2_y = A2.copy(); A2_y[:,1] = b2
A2_z = A2.copy(); A2_z[:,2] = b2

x = np.linalg.det(A2_x)/detA2
y = np.linalg.det(A2_y)/detA2
z = np.linalg.det(A2_z)/detA2
print("\n3. Solución con Cramer:")
print(f"x = {x}, y = {y}, z = {z}")

# 4. Descomposición LU
L2, U2 = doolittle(A2)
print("\n4. Descomposición LU:")
print("Matriz L:")
print(L2)
print("\nMatriz U:")
print(U2)
print("\nComprobación L@U:")
print(L2 @ U2)

# Resolver usando LU
z = np.linalg.solve(L2, b2)
x_lu = np.linalg.solve(U2, z)
print("\nSolución usando LU:")
print(x_lu)

# 5. Cholesky (no aplica para este sistema)
print("\n5. Este sistema no es simétrico definido positivo, no aplica Cholesky")

# Sistema 3: x1 + 2x2 + x3 = 2; 3x1 + 8x2 + x3 = 12; 4x2 + x3 = 2
A3 = np.array([[1, 2, 1], [3, 8, 1], [0, 4, 1]])
b3 = np.array([2, 12, 2])

print("\n\n=== SISTEMA 3 ===")

# 1. Solución con np.linalg.solve
sol3 = np.linalg.solve(A3, b3)
print("\n1. Solución con np.linalg.solve:")
print(sol3)

# 2. Método de matriz inversa
A3_inv = np.linalg.inv(A3)
sol3_inv = A3_inv @ b3
print("\n2. Solución con matriz inversa:")
print(sol3_inv)

# 3. Método de Cramer
detA3 = np.linalg.det(A3)
A3_x = A3.copy(); A3_x[:,0] = b3
A3_y = A3.copy(); A3_y[:,1] = b3
A3_z = A3.copy(); A3_z[:,2] = b3

x = np.linalg.det(A3_x)/detA3
y = np.linalg.det(A3_y)/detA3
z = np.linalg.det(A3_z)/detA3
print("\n3. Solución con Cramer:")
print(f"x = {x}, y = {y}, z = {z}")

# 4. Descomposición LU
L3, U3 = doolittle(A3)
print("\n4. Descomposición LU:")
print("Matriz L:")
print(L3)
print("\nMatriz U:")
print(U3)
print("\nComprobación L@U:")
print(L3 @ U3)

# Resolver usando LU
z = np.linalg.solve(L3, b3)
x_lu = np.linalg.solve(U3, z)
print("\nSolución usando LU:")
print(x_lu)

# 5. Cholesky (no aplica para este sistema)
print("\n5. Este sistema no es simétrico definido positivo, no aplica Cholesky")

