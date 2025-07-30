def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return idade, 'Não Vota!'
    elif 16 <= idade < 18 or idade > 65:
        return idade, 'Voto Opcional'
    elif idade >= 18:
        return idade, 'Voto Obrigatório'

print('-='*30)
ano = int(input('Em que ano você nasceu? '))
idade, resp = voto(ano) 
print(f'Com {idade} anos: {resp}') 