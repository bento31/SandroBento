print('--------BEM-VINDO--------')

login = input('Digite seu login: ')
senha = input('Digite sua senha: ')

if login == 'admin' and senha == '619':
    print('Acesso liberado')
else:
    print('Acesso negado')