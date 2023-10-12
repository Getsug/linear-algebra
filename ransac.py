"""
Linear Algebra - Q3
이름: 허버트
학번: 2020110876
"""

import numpy as np
import matplotlib.pyplot as plt
import random
import math


# read whole file into numpy as 2d array
data = np.loadtxt(fname="data.txt", delimiter="\t", dtype=float)
# print(data)

x = []
y = []

for i in range(len(data)):
    for j in range(2):
        if j == 0:
            x.append(data[i][j])
        else:
            y.append(data[i][j])

# print(x)
# print(y)


n = 2  # minimum number of points to estimate to make line
t = 0.2  # threshold
k = 20  # maximum iterations
d = 80    # minimum number of points to asert that a model fits well

iterations = 0
bestError = 100
ratio = 0.
bestFit_x = 0.
bestFit_y = 0.
bestFit_m = 0.
bestFit_b = 0.

while iterations < k:

    in_liners = []

    # randomly select two points
    num1 = random.randint(0, 99)
    num2 = random.randint(0, 99)

    point1x = x[num1]
    point1y = y[num1]

    point2x = x[num2]
    point2y = y[num2]

    if point2x is not point1x:

        # find the slope m of the two randomly selected points
        slope_m = (point2y - point1y) / (point2x - point1x)
        # print(slope_m)
        # print(f"point2:{point2x} {point2y}  point1: {point1x} {point1y}")
        b1 = point1y - (slope_m * point1x)
        # print(b1)

        # find the perpendicular slope to slope_m
        m1 = (-1 / slope_m)

        for value in range(100):

            if value is not num1 or value is not num2:
                # find intercept
                b2 = y[value] - (m1 * x[value])

                # find coordinates of intersection of the two lines
                intersect_x = ((-b2) + b1) / (m1 - slope_m)
                intersect_y = (m1 * intersect_x) + b2

                distance = math.sqrt(((intersect_x - x[value]) ** 2) + ((intersect_y - y[value]) ** 2))

                if distance < t:
                    maybe_inline = (x[value], y[value])
                    in_liners.append(maybe_inline)

        in_liners_count = len(in_liners)
        if in_liners_count > ratio:
            ratio = in_liners_count

        # we have enough inlines
        if in_liners_count > d:
            bestFit_x = point1x
            bestFit_y = point1y
            bestFit_m = slope_m
            bestFit_b = b1
            break

    iterations += 1


# find least squares solution
X_mean = np.mean(x)
Y_mean = np.mean(y)
num = 0
den = 0

for i in range(len(x)):
    num += (x[i] - X_mean) + (y[i] - Y_mean)
    den += ((x[i]) - X_mean)**2

m = num / den
c = Y_mean - m*X_mean

least_sq_x = np.linspace(0., 10., 100)
least_sq_predict = m * least_sq_x + c


x_eq_line = np.linspace(0., 10., 100)
y_eq_line = (bestFit_m * x_eq_line) + bestFit_b


print(f"Ransac Equation: y = {bestFit_m}.x + ({bestFit_b})")
print(f"least Squares Equation: y = {m}.x + ({c})")

filename = "output.png"

# plot the graph
plt.figure(figsize=(7, 7))
plt.title("100 COORDINATES FROM data.txt")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.scatter(x, y, color="green")
plt.plot(x_eq_line, y_eq_line, label="y=mx+c(RANSAC)", color="red", linewidth=3.0)
plt.plot(x, least_sq_predict, label="y=mx+c(least squares solution)", color="blue", linewidth=3.0)
plt.legend(loc="lower right", fontsize=7)
plt.savefig(filename)
plt.show()


