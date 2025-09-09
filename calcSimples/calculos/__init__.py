
def calculos(n1,n2, op):
    if op == 1:
        return  n1 + n2
    elif op == 2:
        return n1 - n2
    elif op == 3:
        return n1 * n2
    elif op == 4:
        if n2 != 0:
            return n1 / n2
        else:
            print('Erro! divisão por zero')
            return None
    elif op == 5:
        print('Saindo...')
        return "sair"
    else:
        print('Erro! operação inválida')
        return None #usado return pq ele encerra a função e devolve algo para quem chamou