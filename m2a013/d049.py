n = int(input('Digite un número para ver sua tabuada: '))

for i in range(1, 11):
    print('{} x {} = {}'.format(n, i, n * i))