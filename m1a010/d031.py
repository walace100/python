distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distancia))
if distancia <= 200:
    preco = distancia * .5
else:
    preco = distancia * .45
print('E o preço da sua passagem será de R${:.2f}'.format(preco))
