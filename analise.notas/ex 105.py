def notas(*n, sit=False):
    """ 
     -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou maias notas dos alunos (aceitas várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma. 
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOÁVEL' 
        else:
            r['situacao'] = 'RUIM'
    return r



#programa principal
resp = notas (5.2 ,6.8 ,10, 6, sit=True) #True mostra a situação e false não mostra
print(resp)

print('\n--- Resultado da Análise ---')
print(f'Total de notas: {resp['total']}')
print(f'Maior nota: {resp['maior']}')
print(f'Menor nota: {resp['menor']}')
print(f'Média da turma: {resp['media']:.2f}')
print(f'Situação da Turma: {resp['situacao']}')

print('\033[1;35;47m --- FIM --- \033[m')
help(notas)