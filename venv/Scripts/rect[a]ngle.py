import sys

print("Wrong args") if len(sys.argv) < 3 else print\
    ("у-ля-ля, ваш прямоугольник готов: " + str(int(sys.argv[1]) * int(sys.argv[2])))