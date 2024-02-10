from ftplib import *

ftp = FTP('ftp.ibiblio.org') #Ao inves de ser 'www' é colocado no inicio 'ftp' e depois o site. Assim caracteriza transferencia de arquivos.
print(ftp.getwelcome())
ftp.quit()

