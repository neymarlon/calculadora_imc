from módulos.defs import *


head()
peso = float(input('DIGITE SEU PESO: '))
altura = float(input('DIGITE SUA ALTURA: '))
imc = peso / (altura * altura)
line()
print(f'Seu IMC é igual a {imc:.2f}')
line()
answer(imc)
