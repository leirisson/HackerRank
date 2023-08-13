class Vogais:
    def __init__(self, palavra):
        self.__palavra = palavra
        
    @property
    def verificar(self):
        conta_vogais = 0
        vogais = set('aeiou')
        for letras in self.__palavra:
            if letras in vogais:
                conta_vogais +=1
        print(f"Total de vogais encontradas: {conta_vogais}")

frase = str(input('Digite uma frase: ').strip().lower())
verificarFrase = Vogais(frase)
verificarFrase.verificar