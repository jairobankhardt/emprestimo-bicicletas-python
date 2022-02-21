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
    def historico_alugueis(self):
        return self.__historico_alugueis

    @historico_alugueis.setter
    def historico_alugueis(self, historico_alugueis):
        self.__historico_alugueis = historico_alugueis

    # Métodos Mágicos
    def __str__(self):
        return f'> {self.__nome} <'
        
    # Métodos
    def __adicionar_bikes_estoque(self, cor, quantidade):
        """
        Método para uso da classe. Adiciona bicicletas ao estoque.

        :param cor: Cor da bicicleta
        :param quantidade: Quantidade de bicicletas para adicionar ao estoque.
        """
        lista = [Bicicleta(cor) for i in range(quantidade)]
        self.__estoque_bikes.extend(lista)

    def adquirir_bikes(self):
        """
        Adiciona bicicletas ao estoque da loja.
        """
        print(f'\n> > >   {self.__nome}   < < <')
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
        print(f'\nSucesso. Foram adicionadas {quantidade} bicicletas ao estoque.')

    def adicionar_bikes_alugadas(self, cod_aluguel, lista_bikes):
        """
        Adiciona bicicletas a lista de alugadas e as tira do estoque.
        Também inicializa o histórico deste aluguel.

        :param cod_aluguel: Código do aluguel
        :param lista_bikes: Lista de bicicletas
        """
        for bike in lista_bikes:
            self.__bikes_alugadas.append(bike)
            self.__estoque_bikes.remove(bike)
            self.__historico_alugueis.update({cod_aluguel: ''})

    def retirar_bikes_alugadas(self, cod_aluguel, data_devolucao, valor, lista_bikes):
        """
        Retira as bicicletas da lista de alugadas e as coloca de novo no estoque para aluguel.
        Atualiza o histórico deste aluguel.

        :param cod_aluguel: Código do aluguel
        :param data_devolucao: A data da devolução
        :param valor: Valor total do aluguel
        :param lista_bikes: Lista de bicicletas
        """
        for bike in lista_bikes:
            self.__bikes_alugadas.remove(bike)
            self.__estoque_bikes.append(bike)
            self.__historico_alugueis.update({cod_aluguel: {'valor_recebido': valor,
                                                            'data_de_devolucao': data_devolucao}})

    def mostrar_estoque_bikes(self):
        """
        Exibe as bicicletas que estão no estoque para aluguel.
        """
        print(f'\n> > >   {self.__nome}   < < <')
        print('\n*** ESTE É O ESTOQUE DISPONÍVEL PARA ALUGUEL ***\n')
        for bike in self.__estoque_bikes:
            print(bike)
        print(f'\nTotal de bikes em estoque: {len(self.__estoque_bikes)}')

    def mostrar_bikes_alugadas(self):
        """
        Exibe as bicicletas que estão alugadas.
        """
        print(f'\n> > >   {self.__nome}   < < <')
        print('\n*** ESTAS SÃO AS BICICLETAS ALUGADAS ***\n')
        for bike in self.__bikes_alugadas:
            print(bike)
        print(f'\nTotal de bikes alugadas: {len(self.__bikes_alugadas)}')

    def devolucao_cliente(self):
        """
        Simula a devolução de aluguéis.
        """
        from cliente import Cliente
        print(f'\n> > >   {self.__nome}   < < <')
        print('\n*** CLIENTE ESTÁ NA LOJA PARA DEVOLVER BICICLETAS ***\n')
        Cliente.visualizar_clientes()
        print('\nQual cliente quer devolver as bicicletas?')
        nome_cliente = Comando.digitar_texto()
        cliente = Cliente.resgatar_cliente(nome_cliente)
        while not cliente:
            print('Cliente não cadastrado. Digite o nome de um cliente da lista acima.')
            nome_cliente = Comando.digitar_texto()
            cliente = Cliente.resgatar_cliente(nome_cliente)
        cliente.devolver_bikes(self.nome)

    # Métodos estáticos
    @staticmethod
    def visualizar_lojas():
        """
        Lista todas as lojas cadastradas.
        """
        print('\n* * *   Lojas   * * *\n')
        if Loja.lojas_cadastradas:
            for lj in Loja.lojas_cadastradas:
                print(lj.nome)
        else:
            print('Não há lojas cadastradas')

    @staticmethod
    def resgatar_loja(nome_loja):
        """
        Busca uma loja existente

        :param nome_loja: Nome da loja.
        :return: A instância da loja ou False para não encontrado
        """
        resultado = [x for x in Loja.lojas_cadastradas if x.nome == nome_loja]
        if resultado:
            return resultado[0]
        return False

    # Método para popular o script, pode ser removido
    @staticmethod
    def inicializar_lojas():
        """
        Somente para popular o script. Pode ser removido.
        """
        power = Loja('Power Bikes')
        super = Loja('Super Bikes')
        legal = Loja('Bike Legal')
        cool = Loja('Bike Cool')

        power.__adicionar_bikes_estoque('azul', 5)
        power.__adicionar_bikes_estoque('amarela', 3)
        super.__adicionar_bikes_estoque('verde', 8)
        legal.__adicionar_bikes_estoque('vermelha', 10)
        legal.__adicionar_bikes_estoque('verde', 4)
        cool.__adicionar_bikes_estoque('cinza', 5)
        cool.__adicionar_bikes_estoque('branca', 7)
        cool.__adicionar_bikes_estoque('amarela', 9)
