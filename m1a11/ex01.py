# \033[style;text;backgroundm
# style:
# 0 - none;
# 1 - bold;
# 4 - underline;
# 7 - negative 
# text:
# 30 - branco;
# 31 - vermelho;
# 32 - verde;
# 33 - amarelo;
# 34 - azul;
# 35 - roxo;
# 36 - ciano;
# 37 - cinza
# background:
# 40 - branco;
# 41 - vermelho;
# 42 - verde;
# 43 - amarelo;
# 44 - azul;
# 45 - roxo;
# 46 - ciano;
# 47 - cinza
# ex: \033[0;33;44m(texto)
print('\033[0;30;41mTeste\033[m')
print('\033[4;33;44mTeste\033[m')
print('\033[1;35;43mTeste\033[m')
print('\033[1;35;43mTeste\033[m')
print('\033[30;42mTeste\033[m')
print('\033[mTeste\033[m')
print('\033[7;30mTeste\033[m')
