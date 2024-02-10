def preencherInventario (lista):
    inventario = []
    resposta = 'S'
    while resposta == 'S':
        equipamento = [input('Equipamento: '),
                       float(input('Valor: ')),
                       int(input('Numero Serial: ')),
                       input('Departamento: ')]
        inventario.append(equipamento)
        resposta = input('Digite /{}/ para continuar: '.format('S')).upper()

def exibirInventario (lista):
    for elemento in lista:
        print('\nNome................:', elemento[0])
        print('Valor...............:', elemento[1])
        print('Numero Serial.......:', elemento[2])
        print('Departamento........:', elemento[3])


def localizarPorNome(lista):
    buscar = input('Digite o nome do equipamento que deseja buscar: ')
    for elemento in lista:
        if buscar == elemento[0]:
            print('\nValor..............:', elemento[1])
            print('Numero serial......:', elemento[2])

def depreciarPorNome(lista, porc):
    depreciacao = input('Digite o nome do equipamento que será depreciado: ')
    for elemento in lista:
        if depreciacao == elemento[0]:
            print('\nValor antigo', elemento[1])
            elemento[1] = elemento[1] * 0.9
            print('Novo valor....: ', elemento[1])

def excluirPorSerial (lista):
    serial = int(input('Digite o número do serial do equipamento que sera excluido: '))
    for elemento in lista:
        if elemento[2] == serial:
            lista.remove(elemento)

def mostrarRestoDoInventario (lista):
    for elemento in lista:
        print('\nNome............:', elemento[0])
        print('Valor...........:', elemento[1])
        print('Serial..........:', elemento[2])
        print('Departamento....:', elemento[3])

def mostrarResultados (lista):
    valores = []
    for elemento in lista:
        valores.append(elemento[1])
    if len(valores) > 0:
        print('\nO equipamento mais caro custa: ',max(valores))
        print('O equipamento mais barato custa: ', min(valores))
        print('O total de equipamentos é de :', sum(valores))







#equipamentos = []
#valores = []
#seriais = []
#departamentos = []
#
#resposta = 'S'
#
#while resposta == 'S':
#    equipamentos.append(input('Equipamento: '))
#    valores.append(float(input('Valor: ')))
#    seriais.append(int(input('Número Serial: ')))
#    departamentos.append(input('Departamento: '))
#    resposta = input('Digite a letra /{}/ para continuar: '.format('S')).upper()
#
#
#buscar = input('\nDigite o nome do equipamento que deseja buscar: ')
#for indice in range(0, len(equipamentos)):
#    if buscar == equipamentos [indice]:
#        print('Valor.....:', valores[indice])
#        print('Serial....:', seriais[indice])
#


#for indice in range(0, len(equipamentos)):
#    print('\nEquipamentos.......:', (indice + 1))
#    print('Nome...............:', equipamentos[indice])
#    print('Valor..............:', valores [indice])
#    print('Serial.............:', seriais [indice])
#    print('Departamento.......:', departamentos[indice])

