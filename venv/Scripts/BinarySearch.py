import random


def search(w, *ww):
    start, end, p, step = 0, len(ww), None, len(ww)/2
    while (end - start) > 1:
        p = ww[int(start) + int(step)]
        print('Start: ' + str(start) + ' End: ' + str(end) + ' Number: ' + str(p))
        if w > p:
            start += step
        elif w < p:
            end -= step
        else:
            break
        step /= 2
    if w == p:
        print('Your item is on index: ' + str(int(start) + int(step)))
        return int(start) + int(step)
    else:
        print('Not found')

q = []
z = None

while z == None:
    q.clear()
    for p in range(1000):
        q.append(random.randint(0, 10000))
    q.sort()
    z = search(8665, *q)