
import numpy as np
from sympy import true
np.set_printoptions(precision=2)

A = np.array([
    [-1, -2],  # vector 1
    [-1, 1],  # vector 2
    [1, 0],  # vector 3
    [0, 1],  # vector 4
    [0, -1]  # vector 5
])

b = np.array([
    [-2],
    [1],
    [3],
    [2],
    [0]
])

# objective function
c = np.array([
    [-3, -1]
])

# initial vertex
vertex = (2, 0)

# vertex is the intersection of vector 1 and vector 5
# Important! always select in ascendent order
# B = {1,2} is okay, but B={2,1} not good
B = (1, 5)

#####################################
##### CALCULATION STARTS HERE ! #####
#####################################
while(True):
    A_B = np.array([
        A[B[0]-1],  # vector 1
        A[B[1]-1]  # vector 5
    ])

    b_B = np.array([
        b[B[0]-1],  # vector 1
        b[B[1]-1]  # vector 5
    ])

    # calculating the inverse v = A_b^-1 *b_B
    A_B_i = np.linalg.inv(A_B)

    v = np.matmul(A_B_i, b_B)
    print("v: ", v)

    u = np.matmul(c, A_B_i)

    print("u: ", u)
    print("Any negative value: ", np.any(u < 0))

    # checking if there are not negative values
    if(not np.any(u < 0)):
        print("Solution found")
        break

    if(np.all((u == 0))):
        print("Solved!")
        break

    index_of_min = np.argmin(u)
    print(index_of_min)

    j = u[0][index_of_min]
    print("j: ", j)

    d = -1 * np.array([A_B_i[:, index_of_min]]).transpose()
    print("d: ", d)

    p1 = np.matmul(A, v)
    p2 = np.matmul(A, d)

    part1 = p2
    part2 = b - p1

    index = 0
    alpha = 0
    minIndex = 0  # k -> index  of min value

    for x in part1:
        if(x[0] == 0 or x[0] < 0):
            index += 1
            continue
        else:
            # print(x[0])
            # print(part2[index][0])
            partial_cal = part2[index][0] // x[0]  # integer division

            print("partial cal: ", partial_cal)

            if(alpha == 0):
                alpha = partial_cal
                minIndex = index
            else:
                if(partial_cal < alpha):
                    alpha = partial_cal
                    minIndex = index
        index += 1

    print("##########################")
    print("minIndex: ", minIndex)
    print("alpha value: ", alpha)
    print("u: ", u)
    print("index of min: ", index_of_min)

    # Replacing values in B
    print("B: ", B)
    k = minIndex + 1
    B_aux = list(B)
    B_aux[minIndex] = k
    B = tuple(B_aux)
    print("B: ", B)
