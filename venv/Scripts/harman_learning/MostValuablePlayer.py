def calc(w, a, b):
    if w == 1:
        return a * b
    else:
        return a / b


arrayNames = ["массу ", "объём ", "плотность "]

inType = int(input('Привет! Если хочешь найти \n массу: жми 1 \n объём: жми 2 \n плотность: жми 3\n'))
c = arrayNames.pop(inType - 1)

inVar1, inVar2 = float(input('Окей, теперь задай ' + arrayNames[0])), \
                 float(input('И ' + arrayNames[1]))

print(c + "равняется: " + str(calc(inType, inVar1, inVar2)))
