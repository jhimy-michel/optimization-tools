""" Work in progress, 
the idea is to receive the matrix A and B and plot a graph """


""" plt.figure(figsize=(8, 6))
for i in range(len(A)):
    div = A[i][1] if A[i][1] > 0 else 1
    
    if A[i][1] != 0:
        x2 = (x1 * A[i][0] + b[i][0])/div
        plt.plot(x1, x2, colors[i], label='x2 = ( x1 * {0} + {1} ) / {2}'.format(
            A[i][0], b[i][0], div), linewidth=2.0)
    else:
        x2 = xaux * 0 + b[i][0]
        plt.plot(x2, xaux, colors[i], label='x1 =  x2 * {0} + {1} '.format(
            0, b[i][0]), linewidth=2.0)


plt.title('Graph')
plt.xlabel('x1', color='#1C2833')
plt.ylabel('x2', color='#1C2833')
plt.legend(loc='upper left')


plt.grid()
plt.show() """