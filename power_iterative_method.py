"""
Linear Algebra - Q1
이름: 허버트
학번: 2020110876
"""


import numpy as np

# get matrix order
orderNum = int(input("Enter the order of matrix A: "))

# make an array of orderNum * orderNum for Matrix A
a = np.zeros((orderNum, orderNum))

print("Enter coefficients:")

for i in range(orderNum):
    for j in range(orderNum):
        a[i][j] = float(input("A[" + str(i) + "] [" + str(j) + "] = "))

# create an orderNum * 1 size array to store vector x values
x = np.zeros(orderNum)

print("\nEnter initial vector x\u2080")

for i in range(orderNum):
    x[i] = float(input("x[" + str(i) + "] = "))


# get maximum number of iterations
maxIterations = int(input("Enter maximum number of iterations: "))

eigenOld = 1.0
# condition = True
iteration = 0

while True:

    if iteration > maxIterations:
        break

    print("\n Iteration %d" % iteration)
    print("----------------")
    # display x
    print(f"Eigen Vector x{iteration}:")
    print("[")
    for i in range(orderNum):
        print("%0.6f\t" % (x[i]))

    print("]")

    x = np.matmul(a, x)

    # display Ax
    print(f"Ax{iteration}:")
    for i in range(orderNum):
        print("%0.6f\t" % (x[i]))

    eigenNew = max(abs(x))
    # display μk
    print("μx: %0.8f" % eigenNew)

    x = x / eigenNew

    iteration = iteration + 1

    # error calculation
    error = abs(eigenNew - eigenOld)
    print("Error = " + str(error))

    eigenOld = eigenNew
