from math import hypot
copost = float(input('Comprimento do cateto oposto: '))
cadj = float(input('Comprimento do cateto adjacente: '))
hip = hypot(copost, cadj)
print('A hipotenusa vai medir {:.2f}'.format(hip))