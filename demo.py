import numpy as np

X = np.array([[40, 150],
               [50, 130],
               [50, 170],
               [60, 160],
               [70, 140],
               [70, 180]])
Y = np.array(['N', 'Y', 'N', 'Y', 'Y', 'N'])
P = np.array([30, 145])
D = np.zeros(len(X))
for id, x in enumerate(X):
    D[id] = np.sqrt(np.sum((x-P) ** 2))
print(Y[D.argmin()])