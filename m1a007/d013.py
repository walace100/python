salario = float(input('Qual é o salário do Funcionário? R$'))
desconto = salario + salario * .15
print('Um funcionário que ganhava R${0}, com 15% de aumento, passa a receber R${1:.2f}'.format(salario, desconto))
