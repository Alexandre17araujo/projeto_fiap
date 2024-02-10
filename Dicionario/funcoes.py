def perguntar():
    return input ('\n  O que deseja realizar ?\n '
                  '<I> - Para Inserir um usuário\n '
                  '<P> - Para Pesquisar um usuário\n'
                  ' <E> - Para Excluir um usuário\n'
                  ' <L> - Para Listar um usuário\n').upper()

def inserir(dicionario):
    dicionario [input ('Digite o login: ').upper()] = [input ('Digite o nome: ').upper(),
                                                         input ('Digite a ultima data de acesso: '),
                                                         input ('Qual a ultima estação acessada: ').upper()]
    salvar(dicionario)

def salvar(dicionario):
    with open('bd.txt', 'a') as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ':' + str(valor))




def pesquisar(dicionario):
    nome = input('Informe o nome que deseja buscar: ')
    for usuario in dicionario:
        #if nome == usuario[0]:    
        print('Nome.......:', usuario [0])



