m = int(input('Uma distância em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('A medida de {0:.1f} corresponde a\n {1}km\n {2}hm\n {3}dam\n {4}dm\n {5}cm\n {6}mm\n'.format(m, km, hm, dam, dm, cm, mm))