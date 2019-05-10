# pylint:disable=W0312
def find(*matr):
    count, b = 0, None
    for i in matr:
        if len(i) > count:
            count = len(i)
            b = i
            number = matr.index(i)
    k = [h + 1 for h in range(len(matr))]
    print(k)
    k.remove(4)
    for p in b:
        k.remove(p)
    return k


# def generate(size):

x = [[2, 6], [3, 4], [2, 4], [2, 3, 5, 6], [4], [1, 4]]
o = find(*x)
print(o)
