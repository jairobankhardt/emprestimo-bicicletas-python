from bicicleta import Bicicleta
from apoio import Comando

class Loja:

    lojas_cadastradas = []

    def __init__(self, nome):
        self.nome = nome
        self.estoque_bikes = []
        self.bikes_alugadas = []
        self.historico_alugueis = {}
        Loja.lojas_cadastradas.append(self)

    # Getters and Setters
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def estoque_bikes(self):
        return self.__estoque_bikes

    @estoque_bikes.setter
    def estoque_bikes(self, estoque_bikes):
        self.__estoque_bikes = estoque_bikes

    @property
    def bikes_alugadas(self):
        return self.__bikes_alugadas

    @bikes_alugadas.setter
    def bikes_alugadas(self, bikes_alugadas):
        self.__bikes_alugadas = bikes_alugadas

    @property
    def historico_bikes_alugadas(self):
        return self.__historico_bikes_alugadas

    @historico_bikes_alugadas.setter
    def historico_bikes_alugadas(self, historico_bikes_alugadas):
        self.__historico_bikes_alugadas = historico_bikes_alugadas




    # Métodos Mágicos

    def __str__(self):
        return f'> {self.__nome} <'
        
    # Métodos

    def __adicionar_bikes_estoque(self, cor, quantidade):
        lista = [Bicicleta(cor) for i in range(quantidade)]
        self.__estoque_bikes.extend(lista)

    def adquirir_bikes(self):
        print(f'\n=-=-=-=-= {self.__nome} =-=-=-=-=')
        print('\n*** ADQUIRIR BICICLETAS ***\n')
        print('De qual cor você quer suas bicicletas?')
        cor = Comando.digitar_texto()
        print('Quantas bicicletas você deseja adquirir? ', end='')
        quantidade = Comando.digitar_inteiro(1, False)
        while quantidade < 1:
            print('\n### Erro: Você deve digitar um número inteiro positivo. Tente novamente.\n')
            print('Quantas bicicletas você deseja adquirir? ', end='')
            quantidade = Comando.digitar_inteiro(1, False)
        self.__adicionar_bikes_estoque(cor, quantidade)
        print(f'\nSucesso. Foram adicionadas {quantidade} bicicletas ao estoque.\n')
        Comando.imprimir_divisor('_', 40)

    def adicionar_bikes_alugadas(self, cod_aluguel, lista_bikes):
        for bike in lista_bikes:
            self.__bikes_alugadas.append(bike)
            self.__estoque_bikes.remove(bike)
            self.historico_alugueis.update({cod_aluguel: ''})


    def retirar_bikes_alugadas(self, lista_bikes):
        for bike in lista_bikes:
            self.__bikes_alugadas.remove(bike)
            self.__estoque_bikes.append(bike)

    def calcular_conta(self):
        pass

    def mostrar_estoque_bikes(self):
        print(f'\n=-=-=-=-= {self.__nome} =-=-=-=-=')
        print('\n*** ESTE É O ESTOQUE DISPONÍVEL PARA ALUGUEL ***\n')
        for bike in self.__estoque_bikes:
            print(bike)
        print(f'\nTotal de bikes em estoque: {len(self.__estoque_bikes)}')
        Comando.imprimir_divisor('_', 32)

    def mostrar_bikes_alugadas(self):
        print(f'\n=-=-=-=-= {self.__nome} =-=-=-=-=')
        print('\n*** ESTAS SÃO AS BICICLETAS ALUGADAS ***\n')
        for bike in self.__bikes_alugadas:
            print(bike)
        print(f'\nTotal de bikes alugadas: {len(self.__bikes_alugadas)}')
        Comando.imprimir_divisor('_', 32)

    def receber_pedido_aluguel(self):
        pass

    @staticmethod
    def visualizar_lojas():
        print('\n*** Lojas ***\n')
        if Loja.lojas_cadastradas:
            for l in Loja.lojas_cadastradas:
                print(l.nome)
        else:
            print('Não há lojas cadastradas')

    @staticmethod
    def resgatar_loja(nome_loja):
        resultado = [x for x in Loja.lojas_cadastradas if x.nome == nome_loja]
        if resultado:
            return resultado[0]
        return False

    @staticmethod
    def inicializar_lojas():
        a = Loja('a')
        power = Loja('Power Bikes')
        super = Loja('Super Bikes')
        legal = Loja('Bike Legal')

        a.__adicionar_bikes_estoque('azul', 5)


if __name__ == "__main__":
    l = Loja('a')
    o = Loja('b')
    Loja.visualizar_lojas()
    nome_loja = 'a'
    teste = [x for x in Loja.lojas_cadastradas if x.nome == nome_loja]
    print(teste[0])