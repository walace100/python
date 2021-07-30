casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
financiamento = int(input('Quantos anos de financiamento? '))
prestacao = casa / (financiamento * 12)

print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa, financiamento,prestacao))
if prestacao > salario * .3:
    print('Empréstimo pode ser NEGADO!')
else:
    print('Empréstimo pode ser CONCEDIDO!')