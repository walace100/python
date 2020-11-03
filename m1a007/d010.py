dolar = float(input('Qual o valor do dólar? US$'))
dinheiro = float(input('Quanto você tem na carteira? R$'))
print('Com R${0:.2f} você pode comprar US${1:.2f}'.format(dinheiro, dinheiro / dolar))
