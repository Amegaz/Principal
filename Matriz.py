file = open("compilador.lr")
fil = file.read()
fi = fil.split("\n")
print(fi[0])
for i in range(int(fi[0])):
    print(fi[i+1])
print(fi[int(fi[0])+1])
size = fi[int(fi[0])+1].split("\t")
s = [0] * int(size[0])
s = [s] * int(size[1])
for i in range(int(fi[0])+2,int(size[0])+int(fi[0])+2):
    s[0] = fi[i].split("\t")
    print(s[0])
