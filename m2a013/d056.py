idades = 0
menor20 = 0
velho = ''
velhoIdade = 0

for i in range(4):
    print('----- {}ª PESSOA -----'.format(i + 1))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper()

    if i == 0:
        velho = nome
        velhoIdade = idade
    elif idade >= velhoIdade and sexo == 'M':
        velho = nome
        velhoIdade = idade
    
    if sexo == 'F' and idade < 20:
        menor20 += 1

    idades += idade

print('A média de idade do grupo foi de {:.2f} anos'.format(idades / 4))
print('O home mais velho tem {} anos e se chama {}.'.format(velhoIdade, velho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(menor20))
