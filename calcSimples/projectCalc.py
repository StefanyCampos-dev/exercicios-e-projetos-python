from calcSimples import menu

print('Minha primeira calculadora em Python')

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))



while True:
    op = menu()
    print("Você escolheu a função",op)


    if op == 1:
        res =  n1 + n2
    elif op == 2:
        res = n1 - n2
    elif op == 3:
        res = n1 * n2
    elif op == 4:
        if n2 != 0:
            res = n1/n2
        else:
            print('Erro! divisão por zero')
    elif op == 5:
        break
    else:
        print('Erro! operação inválida')