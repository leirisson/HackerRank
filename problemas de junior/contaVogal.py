palavra = str(input('Informe o seu nome completo: ')).lower().strip()
vogais = set("aeiou")
lista_vogais = []
contta_vogais = 0
for letra in palavra:
    if letra in vogais:
        lista_vogais.append(letra)
        contta_vogais +=1
print(f'Vogais que estão no seu nome: {lista_vogais}')
print(contta_vogais)
