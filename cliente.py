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
    def ver_bikes_disponiveis(self):
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

    def alugar_bikes(self):
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

    def devolver_bikes(self):
        if self.alugueis:
            print(f'\n> > >   Aluguéis de {self.nome}:\n')
            # A data de devolução está aqui porque durante a execução do script
            # o usuário pode demorar para fazer suas escolhas e o tempo de espera pode alterar o valor do aluguel.
            # Então considero o momento em que o usuário entra na opção de devolução
            # e não quando efetivamente realiza a devolução.
            data_devolucao = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            for cod in self.alugueis:
                emprestimo = Emprestimo.emprestimos[cod]
                print(f'Código do aluguel: {cod}')
                print(f'Data do empréstimo: {emprestimo["data_do_emprestimo"]}')
                print(f'{Emprestimo.VALORES[emprestimo["tipo_do_aluguel"]]["rotulo"]}: '
                      f'R${Emprestimo.VALORES[emprestimo["tipo_do_aluguel"]]["valor"]:.2f}')
                print(f'Quantidade de bicicletas alugadas: {len(emprestimo["lista_de_bikes"])}')
                valor, periodo = Emprestimo.calcular_valor_aluguel(emprestimo, data_devolucao)
                print(f'Período: {periodo}')
                if len(emprestimo["lista_de_bikes"]) >= 3:
                    print(f'Você participou da promoção e ganhou {Emprestimo.VALORES["DESCONTO_PROMOCAO"]}% de desconto.')
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
            else:
                Emprestimo.realizar_devolucao_aluguel(codigo, data_devolucao)
                print('\n> > >   Devolução efetuada com sucesso.')
                Comando.continuar_com_enter()

        else:
            print(f'\n> > >   Não há aluguéis para {self.nome}.\n')
            print('Tente novamente.')

    @staticmethod
    def visualizar_clientes():
        print('\n*** Clientes ***\n')
        if Cliente.clientes_cadastrados:
            for c in Cliente.clientes_cadastrados:
                print(c.nome)
        else:
            print('Não há clientes cadastrados')

    @staticmethod
    def resgatar_cliente(nome_cliente):
        resultado = [x for x in Cliente.clientes_cadastrados if x.nome == nome_cliente]
        if resultado:
            return resultado[0]
        return False

    @staticmethod
    def inicializar_clientes():
        f = Cliente('f', '32 65489-5614')
        jairo = Cliente('Jairo', '41 99611-2665')
        xunda = Cliente('Xunda', '99 6523-5489')
        locha = Cliente('Locha', '98 98989-9898')



if __name__ == "__main__":
    print("Cliente")
    jairo = Cliente("Jairo", "41 99611-2665")

