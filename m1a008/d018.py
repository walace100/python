from math import sin, cos, tan, radians
angulo = int(input('Digite o angulo que você deseja: '))
sen = sin(radians(angulo))
co = cos(radians(angulo))
ta = tan(radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, sen))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, co))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, ta))
