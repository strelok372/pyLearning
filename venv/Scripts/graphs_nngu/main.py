import numpy as np
import random
import networkx as nx
import pylab as pl
import matplotlib

#
# def find(*matr):
#     arrSize, sizeCount = 0, 0
#     tempArr, arrIndexes = [], []
#     cycle = len(matr)
#     temp = np.arange(1, cycle, 1)
#     while cycle > 0:
#         found = findmax(matr)
#         for f in found:
#             pass
#     k = [h + 1 for h in range(len(matr))]
#     print(k)
#     return k
#
#
# # def generate(size):
#
# def findSizeAndCount(*matr):
#     count, b = 0, []
#     for i in matr:
#         if len(i) > count:
#             count = len(i)
#             b.clear()
#             b.append(matr.index(i))
#
#
#
# def findmax(*mass, num):
#     count, b = 0, []
#     for i in mass:
#         if len(i) > count:
#             count = len(i)
#             b.clear()
#             b.append(mass.index(i))
#     return mass

def generation(q):
    w = np.eye(q, dtype=int)
    for i in range(q):
        for p in range(i):
            w[i][p] = random.randint(0,1)
            w[p][i] = w[i][p]
    print(w)
    return w

def finder(matr):
    allM, tempM = [],[]
    w = np.array
    for s in range(matr.shape[0]):
        w = matr[:, s].copy()
        for i in range(s+1, matr.shape[0], 1):
            w += matr[:, i]
            tempM.append([s, i])
            # print(tempM)
            if all(w):
                # print(w, all(w))
                allM.append(tempM.copy())
                tempM.clear()
                w = matr[:, s].copy()
            # print(w)
    for x in allM:
        print(x)
    g = nx.from_numpy_matrix(matr)
    # nx.draw(g)
    nx.draw_networkx(g)
    pl.savefig('graph.png')
    pl.close()
    # print(allM)

# x = [[2, 6],
#      [3, 4],
#      [2, 4],
#      [2, 3, 5, 6],
#      [4],
#      [1, 4]]
#
# x1 = [[2],
#       [1,3],
#       [2,4],
#       [3,5,6],
#       [4,6],
#       [4,5,7],
#       [6]]

# o = find(*x)
# print(o)

finder(generation(10))

# nx.draw()