larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
a = larg * alt
tinta = a / 2
print('Sua parede tem a dimensão de {0}x{1} e sua área é de {2}m².'.format(larg, alt, a))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))
