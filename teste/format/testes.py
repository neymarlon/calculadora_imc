def head():
    print('-' * 50)
    print('CALCULADORA DE IMC'.center(50))
    print('-' * 50)


def line():
    print('-' * 50)


def answer(resultado):
    if resultado <= 15.99:
        print('Magreza grave\n'
              'Consequências para a saúde:\n'
              'Fadiga, stress, ansiedade')
    elif 16 <= resultado <= 16.99:
        print('Magreza moderada\n'
              'Consequências para a saúde:\n'
              'Fadiga, stress, ansiedade')
    elif 17 <= resultado <= 18.49:
        print('Magreza leve\n'
              'Consequências para a saúde:\n'
              'Fadiga, stress, ansiedade')
    elif 18.5 <= resultado <= 24.99:
        print('Saudável\n'
              'Consequências para a saúde:\n'
              'Menor risco de doenças cardíacas e vasculares')
    elif 25 <= resultado <= 29.99:
        print('Sobrepeso\n'
              'Consequências para a saúde:\n'
              'Fadiga, má circulação, varizes')
    elif 30 <= resultado <= 34.99:
        print('Obesidade grau I\n'
              'Consequências para a saúde:\n'
              'Diabetes, angina, infarto, aterosclerose')
    elif 35 <= resultado <= 39.99:
        print('Obesidade grau II\n'
              'Consequências para a saúde:\n'
              'Apneia do sono, falta de ar')
    elif resultado >= 40:
        print('Obesidade grau III\n'
              'Consequências para a saúde:\n'
              'Refluxo, dificuldade para se mover, escaras, diabetes, infarto, AVC')

