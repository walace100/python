n = int(input('Digite um número: '))
c = 0

for i in range(1, n + 1):
    if n % i == 0:
        c += 1
        print('\033[1;33m{}\033[m'.format(i), end=' ')
    else:
        print('\033[1;31m{}\033[m'.format(i), end=' ')

print('O número {} foi divisível {} vezes'.format(n, c))

if c == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
