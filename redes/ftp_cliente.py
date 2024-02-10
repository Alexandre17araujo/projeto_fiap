from ftplib import *

#Transferir arquivos grandes se utiliza o protocolo FTP.

ftp = FTP('ftp.ibiblio.org')
print(ftp.getwelcome())
usuario = input ('Digite o usuario: ')
senha = input ('Digite a senha: ')
ftp.login(usuario, senha)
print ('Diretorio atual de trabalho: {}'.format(ftp.pwd()))
ftp.cwd('pub')
print('Diretorio corrente: {}'.format(ftp.pwd()))
print(ftp.retrlines('LIST'))
ftp.quit()