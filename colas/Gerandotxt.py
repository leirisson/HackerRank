# COMO CRIAR E MODIFICAR ARQUIVOS DE TEXTO:
"""
r  -> Usado somente para ler algo
w  -> Usado somente para escrever algo
r+ -> Usado para ler e escrever algo
a  -> Usado para acrecentar algo

"""

valores = [15,100,655,1000,25,65,12]

with open('novoarquivo.txt', 'w') as arquivo:
    for valor in valores:
        arquivo.write(str(valor) + '\n')

# adcionando outros valores com (a)
with open('novoarquivo.txt', 'a') as arquivo:
    arquivo.write("Adcionando novas informações com (a)")

with open('novoarquivo.txt', 'a') as arquivo:
    for valor in valores:
        arquivo.write(str(valor) + '\n')

# lendo informações com o (r)
with open('novoarquivo.txt','r') as arquivo:
    for valor in valores:
        print(valor)

# percorrendo o arquivo
with open('novoarquivo.txt','r') as arquivo:
    for valor in arquivo:
        print(valor)

# lendo e escrevendo valores 
with open('novoarquivo.txt', 'r+') as arquivo:
    for valor in valores:
        print(valor)
    arquivo.write("nova informação")