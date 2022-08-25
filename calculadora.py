from defs import formatacao


formatacao.head()
peso = float(input('DIGITE SEU PESO: '))
altura = float(input('DIGITE SUA ALTURA: '))
imc = peso / (altura * altura)
formatacao.line()
print(f'Seu IMC é igual a {imc:.2f}')
formatacao.line()
formatacao.answer(imc)
