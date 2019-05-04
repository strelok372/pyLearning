import sys

if not (len(sys.argv) == 2) and (sys.argv[1].type != str):
    print("HEY, WHERE IS MY STRING?!")
    exit()
else:
    p = (sys.argv[1])[::-1].lower().replace(' ', '')
    if p == sys.argv[1].lower().replace(' ',''):
        print("Ваша строчка палиндромчик")
    else:
        print("Введённая строка не является палиндромом, скучный ответ")