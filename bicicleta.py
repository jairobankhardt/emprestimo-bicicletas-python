import random

class Bicicleta:

    # Cada bicicleta terá uma cor e um código gerado aleatoriamente.
    def __init__(self, cor):
        self.cor = cor
        self.codigo = None

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = random.randint(100000, 999999)

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    def __str__(self):
        return f'(cód: {self.codigo}) Bicicleta {self.cor}'
