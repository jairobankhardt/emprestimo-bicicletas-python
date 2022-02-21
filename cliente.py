from datetime import datetime

from loja import Loja
from apoio import Comando
from menus import Menu
from emprestimo import Emprestimo


class Cliente:

    clientes_cadastrados = []

    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
        self.alugueis = []
        self.clientes_cadastrados.append(self)

    # Getters and Setters
    def __get_nome(self):
        return self.__nome

    def __set_nome(self, nome):
        self.__nome = nome

    nome = property(__get_nome, __set_nome)

    def __get_telefone(self):
        return self.__telefone

    def __set_telefone(self, telefone):
        self.__telefone = telefone

    telefone = property(__get_telefone, __set_telefone)

    # Métodos
    def alugar_bikes(self):
        """
        Cliente faz a reserva de uma quantidade de bicicletas que desejar dentro do estoque da loja escolhida.
        """
        if Loja.lojas_cadastradas:
            Loja.visualizar_lojas()
            print('\nDe qual loja você quer alugar?')
            nome_loja = Comando.digitar_texto()
            loja = Loja.resgatar_loja(nome_loja)
            while not loja:
                print('Loja não cadastrada. Escolha uma loja da lista acima.')
                nome_loja = Comando.digitar_texto()
                loja = Loja.resgatar_loja(nome_loja)
            estoque_loja = len(loja.estoque_bikes)
            if estoque_loja > 0:
                Comando.imprimir_divisor('*', 60)
                print(f'{"P R O M O Ç Ã O   F A M Í L I A":^60}')
                print(f'{"Alugue 3 ou mais bicicletas e ganhe, automaticamente":^60}')
                print(f'{str(Emprestimo.VALORES["DESCONTO_PROMOCAO"])+"% DE DESCONTO!!!":^60}')
                print()
                print('-> desconto aplicado na devolução.')
                Comando.imprimir_divisor('*', 60)
                print()
                print(f'Estoque disponível: {estoque_loja}\n')
                print('Quantas bicicletas vocês quer alugar? ', end='')
                quantidade = Comando.digitar_inteiro(1, False)
                while quantidade < 1 or quantidade > len(loja.estoque_bikes):
                    print(f'\n### Erro: Você deve digitar um número inteiro positivo'
                          f'e menor ou igual ao estoque disponível ({estoque_loja}).'
                          f'Tente novamente.\n')
                    print('Quantas bicicletas vocês quer alugar? ', end='')
                    quantidade = Comando.digitar_inteiro(1, False)
                opcao_preco = -1
                while opcao_preco < 0 or opcao_preco > 3:
                    Menu.precos_aluguel()
                    opcao_preco = Comando.digitar_inteiro(3)
                if opcao_preco == 0:
                    print('\n### Aluguel desconsiderado.\n')
                else:
                    Emprestimo.realizar_aluguel_bikes(loja, self, quantidade, opcao_preco)
                    print('\n> > >   Aluguel efetuado.\n'
                          '> > >   Aproveite suas pedaladas.')
            else:
                print('Não há bicicletas disponíveis para alugar nesta loja. Tente em outra loja.')
                Comando.continuar_com_enter()
        else:
            print('Não há lojas cadastradas.')

    def devolver_bikes(self, nome_loja=False):
        """
        Cliente devolve para a loja as bicicletas alugadas anteriomente.
        """
        alugueis = []
        if not nome_loja:
            alugueis = self.alugueis
        else:
            if self.alugueis:
                for cod in self.alugueis:
                    emprestimo = Emprestimo.emprestimos[cod]
                    if emprestimo['loja'].nome == nome_loja:
                        alugueis.append(cod)
        if alugueis:
            print(f'\n> > >   Aluguéis de {self.nome}:\n')
            # A data de devolução está neste ponto do código porque durante a execução do script
            # o usuário pode demorar para fazer suas escolhas e o tempo de espera pode alterar o valor do aluguel.
            # Então considero o momento em que o usuário entra na opção de devolução
            # e não quando efetivamente realiza a devolução.
            data_devolucao = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            for cod in alugueis:
                emprestimo = Emprestimo.emprestimos[cod]
                print(f'Código do aluguel: {cod}')
                print(f'Loja: {emprestimo["loja"].nome}')
                print(f'Data do empréstimo: {emprestimo["data_do_emprestimo"]}')
                print(f'Data da devolução: {data_devolucao}')
                print(f'{Emprestimo.VALORES[emprestimo["tipo_do_aluguel"]]["rotulo"]}: '
                      f'R${Emprestimo.VALORES[emprestimo["tipo_do_aluguel"]]["valor"]:.2f}')
                print(f'Quantidade de bicicletas alugadas: {len(emprestimo["lista_de_bikes"])}')
                valor, periodo = Emprestimo.calcular_valor_aluguel(emprestimo, data_devolucao)
                print(f'Período: {periodo}')
                if len(emprestimo["lista_de_bikes"]) >= 3:
                    print(f'Você participou da promoção '
                          f'e ganhou {Emprestimo.VALORES["DESCONTO_PROMOCAO"]}% de desconto.')
                print(f'Valor do aluguel: R${valor:.2f}')
                print()
            print('Digite o código do aluguel que você deseja realizar a devolução '
                  '(0 para desistir da devolução): ', end='')
            codigo = Comando.digitar_inteiro(1, False)
            while codigo not in self.alugueis and codigo != 0:
                print('Código inválido. Tente novamente.')
                print('Digite o código do aluguel que você deseja realizar a devolução '
                      '(0 para desistir da devolução): ', end='')
                codigo = Comando.digitar_inteiro(1, False)
            if codigo == 0:
                print('\nDevolução não efetuada.')
                Comando.continuar_com_enter()
            else:
                Emprestimo.realizar_devolucao_aluguel(codigo, data_devolucao)
                print('\n> > >   Devolução efetuada com sucesso.')
                Comando.continuar_com_enter()

        else:
            print(f'\n> > >   Não há aluguéis para {self.nome}.')
            Comando.continuar_com_enter()

    # Métodos estáticos
    @staticmethod
    def ver_bikes_disponiveis():
        """
        Lista bicicletas disponíveis da loja escolhida.
        """
        if Loja.lojas_cadastradas:
            Loja.visualizar_lojas()
            print('\nDe qual loja você quer visualizar as bikes disponíveis?')
            nome_loja = Comando.digitar_texto()
            loja = Loja.resgatar_loja(nome_loja)
            while not loja:
                print('Loja não cadastrada. Escolha uma loja da lista acima.')
                nome_loja = Comando.digitar_texto()
                loja = Loja.resgatar_loja(nome_loja)
            loja.mostrar_estoque_bikes()
        else:
            print('Não há lojas cadastradas.')

    @staticmethod
    def visualizar_clientes():
        """
        Lista todos os clientes cadastrados.
        """
        print('\n*** Clientes ***\n')
        if Cliente.clientes_cadastrados:
            for c in Cliente.clientes_cadastrados:
                print(c.nome)
        else:
            print('Não há clientes cadastrados')

    @staticmethod
    def resgatar_cliente(nome_cliente):
        """
        Busca um cliente cadastrado.

        :param nome_cliente: Nome do cliente
        :return: A instância do cliente ou False para não encontrado.
        """
        resultado = [x for x in Cliente.clientes_cadastrados if x.nome == nome_cliente]
        if resultado:
            return resultado[0]
        return False

    # Método para popular o script, pode ser removido
    @staticmethod
    def inicializar_clientes():
        """
        Somente para popular o script. Pode ser removido.
        """
        Cliente('Jairo', '41 99611-2665')
        Cliente('Xunda', '99 96523-5489')
        Cliente('Locha', '98 98989-9898')
        Cliente('Loque', '87 96385-2741')
