import matplotlib.pyplot as plt
import numpy as np
""" ONLY WORKS FOR 2D GRAPH """
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
A = np.array([
    [1, 0],  # vector 1
    [1, 1],  # vector 2
    [-1, 0],  # vector 3
    [0, -1],  # vector 4
])


b = np.array([
    [2],
    [4],
    [0],
    [0]
])

x1 = np.linspace(-2, 5, 100)
plt.figure(figsize=(8, 6))

for i in range(len(A)):
    
    if A[i][0] != 0 and A[i][1] != 0:
        div = A[i][1]
        x2 = (x1 * A[i][0] + b[i][0])/div
        plt.plot(x1, x2, colors[i], label='({0}) x1 * {1} + x2 * {2} <= {3}'.format(
            i+1, A[i][0], div, b[i][0]), linewidth=2.0)
        # continue
    # validate if is a horizontal line
    if A[i][0] == 0 and A[i][1] != 0:
        x2 = b[i][0]/A[i][1]
        plt.axhline(x2, -5, 5, c=colors[i], label='({0}) x2 * {1} <= {2}'.format(
            i+1, A[i][1], b[i][0]))

    # validate if is a vertical line
    if A[i][0] != 0 and A[i][1] == 0:
        x2 = b[i][0]/A[i][0]
        plt.axvline(x2, -5, 5, c=colors[i], label='({0}) x1 * {1} <= {2}'.format(
            i+1, A[i][0], b[i][0]))


plt.title('Graph')
plt.xlabel('x1', color='#1C2833')
plt.ylabel('x2', color='#1C2833')
plt.ylim(-5,8)
plt.legend(loc='upper left')


plt.grid()
plt.show()
