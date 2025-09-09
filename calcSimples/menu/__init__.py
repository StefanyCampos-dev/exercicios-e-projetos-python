def menu():

    print('\nCalculadora Simples PYTHON') #quebra linha
    print(' === ESCOLHA A OPERAÇÃO === ')
    print('1 - Soma ')
    print('2 - Subtração ')
    print('3 - Multiplicação ')
    print('4 - Divisão ')
    print('5 - SAIR ')

    while True:
        try:
            escolha = int(input('Digite o numero da operação:  '))
            return escolha
        except ValueError:
            print("Erro! Digite um numero invalido")
#corrigir a entrada do code