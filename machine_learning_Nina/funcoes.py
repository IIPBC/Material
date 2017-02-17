#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np

# Funções para regressão linear
def computeCost(X, y, w):
    m = y.size
    J = 0
    for i in range(m):
        J += np.square(X[i, :].dot(w) - y[i])
    J /= (2 * m)
    return (J)


def gradientDescent(X, y, w, alpha, num_iters):
    m = y.size
    J_history = np.zeros(num_iters)
    temp = np.zeros(w.size)
    numParameters = w.size

    for iter in range(num_iters):
        for j in range(numParameters):
            delta_j = 0
            for i in range(m):
                delta_j += (X[i, :].dot(w) - y[i]) * X[i, j]
            temp[j] = w[j] - alpha * (delta_j / m)
        w = temp
        J_history[iter] = computeCost(X, y, w)

    return (w, J_history)

