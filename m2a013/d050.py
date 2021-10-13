c = 0
s = 0
for i in range(6):
    n = int(input('Digite o {} valor: '.format(i + 1)))
    if n % 2 == 0:
        s += n
        c += 1
print('Você informou {} números pares e a soma foi {}'.format(c, s))