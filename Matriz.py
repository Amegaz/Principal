file = open("compilador.txt")
s = [""] * 95
s = [s] * 46
#s = [[for j in range(95)] for i in range(46)]
fil = file.read()
fi = fil.split("\n")
x = 0
for i in fi:
    y = 0;
    f = i.split(",")
    for j in f:
        s[y][x] = j
        print(s[y][x] + ",",end="")
        y = y + 1
    print("\n")
    x = x + 1
