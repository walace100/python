maior = 0
menor = 0

for i in range(7):
    p = int(input('Em que ano a {}º pessoa nasceu? '. format(i + 1)))

    if p >= 18:
        maior += 1
    else:
        menor += 1

print('Ao todo tivemos 3 pessoas maiores de idade')
print('É também tivemos 4 pessoas menores de idade')