import numpy as np
import random
import networkx as nx
import pylab as pl

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
	
	#вычленяем определённый столбец из матрицы
        w = matr[:, s].copy()
        if all(w):
            allM.append(tempM.append(s))
            tempM.clear()
        for i in range(matr.shape[0]):

		#проверка на самоприсваивание
            if i == s and i != matr.shape[0]-1: 
                continue

            w += matr[:, i] #сумма
            tempM.append([s, i])

		#проверяем столбец на заполнение единицами
            if all(w): 
                allM.append(tempM.copy())
                tempM.clear()
                w = matr[:, s].copy()

    print('Количество найденных множеств: ' + str(len(allM)))
    for x in allM:
        print(x)
    g = nx.from_numpy_matrix(matr)
    nx.draw_networkx(g)
    pl.savefig('graph.png')
    pl.close()
