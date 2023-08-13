class Media:
    def __init__(self,lista=[]):
        self.lista = lista

    def calcularMedia(self):
        tamanho = len(self.lista)
        soma = sum(lista)
        divisor = soma / tamanho       
        print(f'Amedia dos valores é {divisor}')

lista = []
while True:
    valor = int(input("iinforme um valor: "))
    lista.append(valor)
    op = input("deseja conyinuar [S/N]").lower()
    if op in 'n':
        break
    else:
        continue
calcular = Media(lista)
calcular.calcularMedia()