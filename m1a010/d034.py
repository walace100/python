salario = float(input('Qual é o salario do funcionário? R$'))
if salario <= 1250:
    novo = salario + (salario * .15)
else:
    novo = salario + (salario * .10)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, novo)) 
