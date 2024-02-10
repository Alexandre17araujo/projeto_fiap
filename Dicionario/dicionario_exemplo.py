from funcoes import perguntar, pesquisar, inserir

usuarios = {}
opcoes = perguntar()

while opcoes == 'I' or opcoes == 'P' or opcoes == 'E' or opcoes == 'L':
    if opcoes == 'I':
        inserir(usuarios)
        print(usuarios)
    if opcoes == 'P':
        pesquisar(usuarios)

    prosseguir = input('\nDigite /S/ para continuarn e /N/ para PARAR: ').upper()
    if prosseguir == 'S':
        opcoes = perguntar()
    else:
        print('Saindo')
        break

























#usuarios = {'chaves' : ['Chaves do 8', '24/12/2022', 'Recep_01'],
#            'quico' : ['Quico das flores', '20/12/2022', 'Raiox-03']
#            }
#print(usuarios)
#usuarios['florinda'] = ['Dona Florinda', '24/12/2022', 'Raiox_01']
#print(usuarios)
#print('*' * 20)
#print(usuarios.get('quico'))