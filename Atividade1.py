nUm = int(input('Digite um número inteiro: '))
nDois = int(input('Digite um número inteiro'))

operacao = input('Qual operação matemática realizar?: ')

if operacao == 'soma':
    print(nUm+nDois)
elif operacao == 'subtração':
    print(nUm-nDois)
elif operacao == 'multiplicação':
    print(nUm*nDois)
elif operacao == 'divisão':
    print(nUm/nDois)
else:
    print('Erro')
