import socket

resposta = 'S'
while resposta == 'S':
    url = input ('Digite uma URL: ')
    ip = socket.gethostbyname (url)
    print ('O endereço IP do site informado é, {} !!!'.format(ip))
    resposta = input ('\nDigite /S/, para continuar: ').upper()