from apoio import Comando
from emprestimo import Emprestimo


class Menu:

    @staticmethod
    def __final_do_menu(msg="0 - Voltar ao menu anterior"):
        """
        O final dos menus

        :return: Printa o final dos menus.
        """
        print(f'\n{msg}')
        print("\nEscolha uma opção do menu: ", end='')

    @staticmethod
    def lojista_ou_cliente():
        """
        Primeiro menu do sistema\n
        1 - Lojista\n
        2 - Cliente\n
        3 - Listar todas as lojas\n
        4 - Listar todos os clientes

        :return: Exibe primeiro menu do script
        """
        print('\n')
        Comando.imprimir_divisor('_', 30)
        print('> > >   Quem você é   < < <\n\n'
              '1 - Lojista\n'
              '2 - Cliente\n\n'
              '3 - Listar todas as lojas\n'
              '4 - Listar todos os clientes\n')
        Menu.__final_do_menu('0 - Finalizar programa')

    @staticmethod
    def lojista_principal(nome):
        """
        Menu do lojista\n
        1 - Ver estoque de bicicletas não alugadas\n
        2 - Ver bicicletas alugadas\n
        3 - Adquirir bicicletas\n
        4 - Cliente quer fazer uma devolução

        :param nome: Nome da loja
        :return: Printa na tela as opções do menu do lojista.
        """
        print('\n')
        Comando.imprimir_divisor('_', 30)
        print(f'> > >   {nome}   < < <\n')
        print('1 - Ver estoque de bicicletas não alugadas\n'
              '2 - Ver bicicletas alugadas\n'
              '3 - Adquirir bicicletas\n'
              '4 - Cliente quer fazer uma devolução')
        Menu.__final_do_menu()

    @staticmethod
    def cliente_principal(nome):
        """
        Menu do cliente\n
        1 - Ver bicicletas disponíveis\n
        2 - Alugar bicicleta\n
        3 - Devolver bicicleta

        :return: Printa na tela o menu do cliente
        """
        print('\n')
        Comando.imprimir_divisor('_', 30)
        print(f'> > >   {nome}   < < <\n\n'
              '1 - Ver bicicletas disponíveis\n'
              '2 - Alugar bicicleta\n'
              '3 - Devolver bicicleta')
        Menu.__final_do_menu()

    @staticmethod
    def precos_aluguel():
        """
        Menu de Preços\n
        1 - Preço por hora\n
        2 - Preço por dia\n
        3 - Preço por semana

        :return: Exibe na tela o menu de preços.
        """
        print('\n')
        Comando.imprimir_divisor('_', 25)
        print(f'> > >   Preços   < < <\n\n'
              f'1 - {Emprestimo.VALORES[1]["rotulo"]} (R${Emprestimo.VALORES[1]["valor"]:.2f})\n'  # hora
              f'2 - {Emprestimo.VALORES[2]["rotulo"]} (R${Emprestimo.VALORES[2]["valor"]:.2f})\n'  # dia
              f'3 - {Emprestimo.VALORES[3]["rotulo"]} (R${Emprestimo.VALORES[3]["valor"]:.2f})')  # semana
        Menu.__final_do_menu('0 - Desistir do aluguel')
