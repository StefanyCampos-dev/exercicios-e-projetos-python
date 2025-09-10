import menu
import calculos

def main():
    while True:
        try:  # tratamento de erro
            n1 = float(input('Informe o primeiro valor do cálculo:  '))
            n2 = float(input('Informe o segundo valor do cálculo:  '))
        except ValueError:  # tratamento de erro
            print('Erro! Digite apenas números.')
            continue # volta para pedir os números novamente

        while True:
            op = menu.menu()  # chama a função menu() que está dentro do módulo menu

            resultado = calculos.calculos(n1, n2, op)

            if op == 5:  # opção de sair
                print('Saindo...')
                return  # sai do loop do menu e permite reinserir novos números

            # mostra o resultado se não for None
            if resultado is not None:
                print(f'\nO resultado é: {resultado}\n')

            continuar = input('Continuar?  (s/n): ').strip().lower()
            if continuar != "s":
                print('Encerrando calculadora...')
                return
            else:
                break
if __name__ == "__main__":
    main()
#corrigir loop e operação