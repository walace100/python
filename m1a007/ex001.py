print('='*20)
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
print('Soma entre {0} e {1} é igual a {2}'.format(n1, n2, n1 + n2))
print('Subtração entre {0} e {1} é igual a {2}'.format(n1, n2, n1 - n2))
print('Multiplicação entre {0} e {1} é igual a {2}'.format(n1, n2, n1 * n2))
print('Divisão entre {0} e {1} é igual a {2:.2f}'.format(n1, n2, n1 / n2))
print('Potenciação entre {0} e {1} é igual a {2}'.format(n1, n2, n1 ** n2))
print('A divisão inteira entre {0} e {1}\n é igual a {2}'.format(n1, n2, n1 // n2), end=' >>> ')
print('A o resto da divisão entre {0} e {1} é igual a {2}'.format(n1, n2, n1 % n2))
print('='*20)