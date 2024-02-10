#import platform
import getpass
#from datetime import datetime

#print('Nome da Maquina............: ',platform.node())
#print('Arquitetura................:', platform.architecture())
#print('Sistema Operacional........:',platform.system())
#print('Versão do SO...............:', platform.release())
#print('Processador................:',platform.processor())
#print('Versão do Python...........:',platform.python_version())
#
#print(datetime.now())
#print(datetime.now().year)
#print(datetime.now().hour)


usuario = (getpass.getuser())
senha = (getpass.getpass('Digite sua senha: '))

if usuario == 'alexbeze' and senha == 'mundo':
    print('Bem vindo {} !!!'.format(usuario))
else:
    print('Acesso Negado !!!')