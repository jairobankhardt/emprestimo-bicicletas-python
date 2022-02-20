from excecoes import Excecao

class Comando:

    # @staticmethod
    # def limpar_terminal():
    #     os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def imprimir_divisor(simbolo, quantidade):
        print(simbolo * quantidade)

    @staticmethod
    def continuar_com_enter():
        """
        Pausa o script até o usuário apertar a tecla <Enter>
        """
        input("Tecle <Enter> para continuar: ")
        Comando.imprimir_divisor("-", 30)

    @staticmethod
    def __validar_opcao(opcao, limite):
        if 0 < opcao > limite:
            raise Excecao("### Erro: Opção inválida. Tente novamente.")

    @staticmethod
    def digitar_inteiro(limite, eh_menu=True):
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
        texto = input().strip()
        while texto == '':
            print("\nVocê deve digitar algo. Tente novamente.")
            texto = input().strip()
        return texto