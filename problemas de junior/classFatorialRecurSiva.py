class Fatorial:
    def __init__(self,valor):
        self.__valor = valor


    @property
    def cal_ftr(self):
        soma_ftr = 0 
        for numero in range(self.__valor, 0, -1):
            soma_ftr += numero
        print(f"Resultado do fatorial recursiva: {soma_ftr}")



valor = int(input('Informe um valor: '))
calc_ftr = Fatorial(valor)
calc_ftr.cal_ftr