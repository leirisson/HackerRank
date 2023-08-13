class Temp:
    def __init__(self, temp_c):
        self.__temp_c = temp_c

    def calc_temp(self):
        f = (self.__temp_c * (9/5)) + 32
        print(f'Temp em Fahrenheit: {f}')


temperatura = float(input('informe a temperatura para conversão: '))

termometro = Temp(temperatura)
termometro.calc_temp()

