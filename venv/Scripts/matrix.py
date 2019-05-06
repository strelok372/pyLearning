import copy

class Mat:
    def __init__(self, *list_matr):
        self.o = copy.deepcopy(list_matr)

    def __str__(self):
        for i in self.o:
            for a in i:
                print(str(a) + '\t ')
                # repr()

    # def size(self):


q = Mat([[3,6,2,8],[2,8,1,7],[9,3,5,7],[7,2,1,6]])
q.__str__()

