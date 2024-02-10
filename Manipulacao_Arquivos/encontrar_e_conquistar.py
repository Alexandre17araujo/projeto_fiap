basedados = []
with open('iris.data', 'r') as arquivo:
    for registro in arquivo.readlines():
        basedados.append(registro.split(','))
#print(basedados)

print(float (basedados[0][0]) + float (basedados[0][1]))























#texto = 'Eu amo python'
#print(texto.split(' '))
#print(texto.find('u'))

