from userModel import User
from userDao import UserDao

opc = ''
dao = UserDao()

while opc != 'f':
    print('Sistema de cadastro de usuários')
    print('(a) inserir usuário')
    print('(b) buscar usuário')
    print('(c) deletar usuário')
    print('(d) atualizar usuário')
    print('(e) buscar todos os ussuários cadastrados')
    print('(f) Sair')
    opc = input('Escolha uma da opções: ')

    if opc == 'a':
        login = input('\nInforme o login do usuário: ')
        senha = input('Informe a senha do usuário: ')
        email = input('Informe o email do usuário: ')
        user = User(None, login, senha, email)
        dao.insert(user)

    if opc == 'b':
        print('\n')
        id = input('\nInforme o id do usuário desejado: ')
        dao.findById(id)

    if opc == 'c':
        id = input('\nInforme o id do usuário desejado: ')
        dao.deleteById(id)

    if opc == 'd':
        id = input('\nInforme o id do usuário')
        login = input('Informe o login do usuário: ')
        senha = input('Informe a senha do usuário: ')
        email = input('Informe o email do usuário: ')
        user = User(id, login, senha, email)
        dao.updateById(user)

    if opc == 'e':
        print('\n')
        dao.findAll()
dao.closeConection()