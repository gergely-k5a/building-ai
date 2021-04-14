# Least squares method - poor man's version

import numpy as np

# data
X = np.array([[66, 5, 15, 2, 500],
              [21, 3, 50, 1, 100],
              [120, 15, 5, 2, 1200]])
y = np.array([250000, 60000, 525000])

# alternative sets of coefficient values
c = np.array([[3000, 200 , -50, 5000, 100],
              [2000, -250, -100, 150, 250],
              [3000, -100, -150, 0, 150]])

def find_best(X, y, c):
    smallest_error = np.Inf
    best_index = -1
    ci = -1
    for coeff in c:
        est_prices = X @ coeff
        ci += 1
        error = sum([diff**2 for diff in np.subtract(est_prices, y)])
        if smallest_error == np.Inf or smallest_error > error:
            smallest_error = error
            best_index = ci

    print("the best set is set %d" % best_index)


find_best(X, y, c)