import listas2

minha_lista = []
print('Preenchendo')
listas2.preencherInventario(minha_lista)
print('Exibindo')
listas2.exibirInventario(minha_lista)


print('Pesquisando')
listas2.localizarPorNome(minha_lista)
print('Alterando')
listas2.depreciarPorNome(minha_lista, 20)


print('Excluindo')
print(listas2.excluirPorSerial(minha_lista))

print('Resulmindo')
listas2.mostrarResultados(minha_lista)
