import menu
import calculos

def main():
    while True:
        try:  # tratamento de erro
            n1 = float(input('Informe o primeiro valor do cálculo:  '))
            n2 = float(input('Informe o segundo valor do cálculo:  '))
        except ValueError:  # tratamento de erro
            print('Erro! Digite apenas números.')
            return  # encerra o programa se entrada inválida

        while True:
            op = menu.menu()  # chama a função menu() que está dentro do módulo menu

            if op == 5:  # opção de sair
                print('Saindo...')
                break  # sai do loop do menu e permite reinserir novos números

            resultado = calculos.calculos(n1, n2, op)

            # mostra o resultado se não for None
            if resultado is not None:
                print(f'\nO resultado é: {resultado}\n')

if __name__ == "__main__":
    main()
