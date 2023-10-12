"""
Linear Algebra - Q2
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

# create an orderNum * orderNum size array to store identity matrix
identity = np.zeros((orderNum, orderNum))

for i in range(3):
    for j in range(3):
        if j == i:
            identity[i][j] = 1


eigenEstimates = np.zeros(orderNum)

print("\nEnter eigen value estimates")
for i in range(orderNum):
    eigenEstimates[i] = float(input("estimate " + str(i + 1) + ": "))

# sort estimate array
eigenEstimates = np.sort(eigenEstimates)
for i in range(3):
    print(f"{eigenEstimates[i]}")

# first smallest value
eigenMin = eigenEstimates[0]
# print(eigenMin)

# get maximum number of iterations
maxIterations = int(input("Enter maximum number of iterations: "))


eigenOld = 1.0
iteration = 0
initVec = x

print(f"\nUsing {eigenEstimates[0]} as the smallest value")
print("*************************************************")
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

    # eigenMin * Identity
    e = np.multiply(identity, eigenMin)

    # yk
    y = np.matmul(np.linalg.inv(np.subtract(a, e)), x)

    # display yk
    print("[")
    print("yk:")
    for i in range(orderNum):
        print("%0.9f\t" % (y[i]))
    print("]")

    eigenNew = max(abs(y))
    # display μk
    print(f"μk: {eigenNew}")

    v = eigenMin + (1.0 / eigenNew)
    # display vk
    print(f"vk: {v}")

    x = np.multiply(y, (1.0 / eigenNew))

    iteration = iteration + 1


# reset values
# new smallest value to use
eigenMin = eigenEstimates[1]
eigenOld = 1.0
iteration = 0

print(f"\n\nUsing {eigenEstimates[1]} as the smallest value")
print("*************************************************")

while True:

    if iteration > maxIterations:
        break

    print("\n Iteration %d" % iteration)
    print("----------------")
    # display x
    print(f"Eigen Vector x{iteration}:")
    print("[")
    for i in range(orderNum):
        print("%0.6f\t" % (initVec[i]))

    print("]")

    # eigenMin * Identity
    e = np.multiply(identity, eigenMin)

    # yk
    y = np.matmul(np.linalg.inv(np.subtract(a, e)), initVec)

    # display yk
    print("yk:")
    print("[")
    for i in range(orderNum):
        print("%0.9f\t" % (y[i]))
    print("]")

    eigenNew = max(abs(y))
    # display μk
    print(f"μk: {eigenNew}")

    v = eigenMin + (1.0 / eigenNew)
    # display vk
    print(f"vk: {v}")

    initVec = np.multiply(y, (1.0 / eigenNew))

    iteration = iteration + 1
