s = 0
c = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        c += 1
        s += i
print("A soma de todos os {} valores solititados é {}".format(c, s))