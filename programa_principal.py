from cliente import Cliente
from loja import Loja
from menus import Menu

from apoio import Comando

# Para não criar instâncias de lojas e clientes comente as duas linhas abaixo
Loja.inicializar_lojas()
Cliente.inicializar_clientes()

print('*'*77)
print('**  S I S T E M A   D E   E M P R É S T I M O   D E   B I C I C L E T A S  **')
print('*'*77)

opcao = 1
while opcao != 0:
    Menu.lojista_ou_cliente()
    opcao = Comando.digitar_inteiro(4)

    # Entrou no perfil de LOGISTA
    if opcao == 1:
        opcao_lojista = 1
        nome_loja = ''
        while opcao_lojista != 0:
            # Antes de mostrar o menu de opções para o lojista,
            # verifica se a loja existe.
            # Se não existir há a possibilidade de criá-la
            if not nome_loja:
                print("\nQual o nome da sua loja?")
                nome_loja = Comando.digitar_texto()
                if not Loja.resgatar_loja(nome_loja):
                    print(f'\nA loja {nome_loja} não existe.')
                    criar_loja = input('Deseja criá-la? (S para Sim / Qualquer outro valor para Não) ').upper()
                    if criar_loja == 'S':
                        loja = Loja(nome_loja)  # Cria a loja. O nome dela será usado para o próximo menu.
                        print(f'\nLoja {nome_loja} criada com sucesso.\n')
                        Comando.imprimir_divisor('_', 25)
                    else:
                        print('\nLoja não criada. Voltaremos ao menu anterior.')
                        Comando.continuar_com_enter()
                        break
                else:
                    loja = Loja.resgatar_loja(nome_loja)
            Menu.lojista_principal(nome_loja)
            opcao_lojista = Comando.digitar_inteiro(4)
            if opcao_lojista == 1:
                loja.mostrar_estoque_bikes()
            elif opcao_lojista == 2:
                loja.mostrar_bikes_alugadas()
            elif opcao_lojista == 3:
                loja.adquirir_bikes()
            elif opcao_lojista == 4:
                loja.devolucao_cliente()

    # Entrou no perfil de CLIENTE
    elif opcao == 2:
        opcao_cliente = 1
        nome_cliente = ''
        while opcao_cliente != 0:
            # Antes de mostrar o menu de opções para o cliente,
            # verifica se o cliente existe.
            # Se não existir há a possibilidade de criá-lo.
            if not nome_cliente:
                print("\nQual o seu nome?")
                nome_cliente = Comando.digitar_texto()
                if not Cliente.resgatar_cliente(nome_cliente):
                    print(f'\nO cliente {nome_cliente} não existe.')
                    criar_cliente = input('Deseja criar um cadastro? '
                                          '(S para Sim / Qualquer outro valor para Não) ').upper()
                    if criar_cliente == 'S':
                        print('Digite seu telefone.')
                        telefone = Comando.digitar_texto()
                        # Cria o cliente. O nome dele será usado para o próximo menu.
                        cliente = Cliente(nome_cliente, telefone)
                        print(f'\nCadastro do cliente {nome_cliente} criado com sucesso.\n')
                        Comando.imprimir_divisor('_', 35)
                    else:
                        print('\nCadastro não criado. Voltaremos ao menu anterior.')
                        Comando.continuar_com_enter()
                        break
                else:
                    cliente = Cliente.resgatar_cliente(nome_cliente)
            Menu.cliente_principal(nome_cliente)
            opcao_cliente = Comando.digitar_inteiro(3)
            if opcao_cliente == 1:
                cliente.ver_bikes_disponiveis()
            elif opcao_cliente == 2:
                cliente.alugar_bikes()
            elif opcao_cliente == 3:
                cliente.devolver_bikes()
    elif opcao == 3:
        Loja.visualizar_lojas()
    elif opcao == 4:
        Cliente.visualizar_clientes()

print('\n\n+++ PROGRAMA FINALIZADO +++')
