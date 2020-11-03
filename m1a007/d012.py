preco = float(input('Qual é o preço do produto? R$'))
desconto = preco - preco * .05
print('O produto que custava R${0}, na promoção com desconto de 5% vai custar R${1:.2f}'.format(preco, desconto))