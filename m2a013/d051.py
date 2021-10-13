i0 = int(input('Primeiro termo: '))
r = int(input('Razão: '))


for i in range(10):
    print(i0, end=' → ')
    i0 += r
print('Acabou')
