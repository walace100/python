menor = 0
maior = 0

for i in range(5):
    p = float(input('Peso da {}º pessoa: '.format(i + 1)))

    if i == 0:
        menor = p
        maior = p
    elif p > maior:
        maior = p
    else:
        menor = p

print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))