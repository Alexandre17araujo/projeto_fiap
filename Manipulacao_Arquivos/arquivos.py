import json


#dicionario = {
#    "CHAVES":["Chaves do 8", "10/10/2023", "Recep_01"],
#    "QUICO":["Quico Flores", "20/09/1996", "Raiox_01"],
#    "FLORINDA":["Dona Florinda", "30/01/2010", "Recep_03"],
#    "Alexandre":["hacker", "10/10/10", "admin"]
#}
#print(dicionario)
#with open('bd1.json', 'w') as json_file:
#    json.dump(dicionario, json_file)


#with open('bd.json', 'r') as arq_json:
#    dicionario = json.load(arq_json)
#    print(dicionario)
#
#    for chave, dados in dicionario.items():
#        print(chave + ' | ' + str(dados))



informacoes = {'Alexandre' : ['Richard', 26, 'Brasil', 'Manaus']}
informacoes2 = {'Anonymous' : ['Hacker', 25, 'Russia', 'Cremili']}

#print(informacoes)

adicionar = {'CARRO' : 'bmw',
             'AVIAO' : 'Caça'}

novo = list(informacoes)
novo2 = list(informacoes2)

novo.append(novo2)

print(novo)
