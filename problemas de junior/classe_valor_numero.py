class Verificar:
    def __init__(self, valor):
        self.valor = valor

    def verificar_valor(self):
        if self.valor % 2 != 0:
            print("Valor informado é ímpar!")
            print(f"Valor: {self.valor}")
        else:
            print("Valor informado é par!")
            print(f"Valor: {self.valor}")


numero = int(input("Digite um número: "))
verificador = Verificar(numero)
verificador.verificar_valor()
