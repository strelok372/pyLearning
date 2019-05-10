import copy
import pickle


class Mat:
    def __init__(self, *list_matr):
        if len(list_matr) > 0:
            self.o = copy.deepcopy(list_matr)
            self.v, self.b = self.size()

    def __str__(self):
        for i in self.o:
            for a in i:
                print(str(a), end='\t')
            print()

    def size(self):
        return len(self.o), len(self.o[0])

    def __add__(self, *matr):
        for i in range(self.v):
            for a in range(self.b):
                self.o[i][a] += matr[i][a]

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            for i in range(self.v):
                for a in range(self.b):
                    self.o[i][a] *= other
        print(self.o)

    def __rmul__(self, other):
        if type(other) == int or type(other) == float:
            for i in range(self.v):
                for a in range(self.b):
                    self.o[i][a] *= other
        print(self.o)

    def save(self, file):
        with open('C:/' + file + '.pickle', 'w+b') as f:
            pickle.dump(self.o, f)

    def load(self, file):
        with open('C:/' + file + '.pickle', 'r+b') as f:
            self.o = pickle.load(f)

    @staticmethod
    def genmatr(w, h, num):
        genmat = [[num for q in range(h)] for i in range(w)]
        return genmat

    def __matmul__(self, *other):
        a, b = self.size()
        tempm = self.genmatr(a, b, 0)
        # print(tempm)
        # print(self.o)
        # print(a, b)
        for k in range(a):
            for j in range(b):
                l = 0
                for i in range(a):
                    # print(str(k) + ':' + str(i) + '___' + str(i) + ':' + str(j))
                    l += self.o[k][i] * other[0][i][j]
                tempm[k][j] = l
        print(tempm)


        pass

#


q = Mat([3, 6, 2, 8, 1], [2, 8, 1, 7, 8], [9, 3, 5, 7, 2], [7, 2, 1, 6, 1])
# q = Mat()
q.__matmul__(Mat.genmatr(4, 5, 2))

# p = q.genmatr(4,4)
# print(p)
# q.load('matrix')
# q.__str__()
# print(q.size())
# q.add([3,6,2,8,1],[2,8,1,7,8],[9,3,5,7,2],[7,2,1,6,1])
# q.__str__()
# q.__mul__(5)
# q.__str__()
# q.save('matrix')
