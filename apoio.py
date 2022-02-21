from excecoes import Excecao


class Comando:

    # @staticmethod
    # def limpar_terminal():
    #     os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def imprimir_divisor(simbolo, quantidade):
        """
        Imprime um divisor de linha

        :param simbolo: Caracter que será o divisor
        :param quantidade: Quantidade de impressão do símbolo
        :return: Imprime um divisor de linha na tela
        """
        print(simbolo * quantidade)

    @staticmethod
    def continuar_com_enter():
        """
        Pausa o script até o usuário apertar a tecla <Enter>
        """
        input("Tecle <Enter> para continuar: ")

    @staticmethod
    def __validar_opcao(opcao, limite):
        """
        Valida uma opção, normalmente do menu

        :param opcao: O valor digitado
        :param limite: Range do valor
        :return: Lança exceção se a opção for inválida.
        """
        if 0 < opcao > limite:
            raise Excecao("### Erro: Opção inválida. Tente novamente.")

    @staticmethod
    def digitar_inteiro(limite, eh_menu=True):
        """
        Verifica se o valor digitado é um inteiro

        :param limite: Range do valor
        :param eh_menu: Booleano para verificar se o valor verificado é para um menu.
        :return: opção validade ou -1 em caso de insucesso.
        """
        try:
            opcao = int(input())
            if eh_menu:
                Comando.__validar_opcao(opcao, limite)
            return opcao
        except ValueError:
            print("\n### Erro: Você deve digitar um número inteiro. Tente novamente.")
            Comando.continuar_com_enter()
            return -1
        except Excecao as excecao:
            print(excecao.mensagem)
            Comando.continuar_com_enter()
            return -1

    @staticmethod
    def digitar_texto():
        """
        Verifica se o valor digitado não está vazio.

        :return: a string digitada pelo usuário.
        """
        texto = input().strip()
        while texto == '':
            print("\nVocê deve digitar algo. Tente novamente.")
            texto = input().strip()
        return texto