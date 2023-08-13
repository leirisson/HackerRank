#lista_valores = [20,50,68,45,15,30,98,100]
lista = []
while True:
    valor = int(input('informe um valor: '))
    lista.append(valor)
    op = input('Deseja continuar: [S/N]').lower()
    if op in 'n':
        break
    else:
        continue
tamanho_lista = len(lista)
soma_valores = sum(lista)
media = soma_valores / len(lista)
print(f'A media dos valores é: {media}')
