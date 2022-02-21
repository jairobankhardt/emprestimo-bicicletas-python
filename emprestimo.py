from datetime import datetime
import random


class Emprestimo:
    
    VALORES = {
        1: {
            "valor": 5.0,
            "rotulo": "Valor por hora"
        },
        2: {
            "valor": 25.0,
            "rotulo": "Valor por dia"
        },
        3: {
            "valor": 100.0,
            "rotulo": "Valor por semana"
        },
        'DESCONTO_PROMOCAO': 30  # porcentagem
    }

    emprestimos = {}

    @staticmethod
    def realizar_aluguel_bikes(loja, cliente, num_bikes, tipo_aluguel):
        """
        Efetua o aluguel das bicicletas pelo Cliente.

        :param loja: Objeto Loja
        :param cliente: Objeto Cliente
        :param num_bikes: Quantidade de bicicletas
        :param tipo_aluguel: Tipo (período) do aluguel
        """
        data_emprestimo = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        lista_bikes = []
        for i in range(num_bikes):
            lista_bikes.append(loja.estoque_bikes[i])
        codigo_do_aluguel = random.randint(1000, 9999)
        dic_valores = {'cliente': cliente,
                       'loja': loja,
                       'lista_de_bikes': lista_bikes,
                       'tipo_do_aluguel': tipo_aluguel,
                       'data_do_emprestimo': data_emprestimo}
        novo_dicionario_emprestimo = {codigo_do_aluguel: dic_valores}
        Emprestimo.emprestimos.update(novo_dicionario_emprestimo)
        loja.adicionar_bikes_alugadas(codigo_do_aluguel, lista_bikes)
        cliente.alugueis.append(codigo_do_aluguel)

    @staticmethod
    def realizar_devolucao_aluguel(codigo, data_devolucao):
        """
        Efetua a devolução do aluguel.

        :param codigo: Código do aluguel
        :param data_devolucao: Data de devolução
        """
        emprestimo = Emprestimo.emprestimos[codigo]
        valor, periodo = Emprestimo.calcular_valor_aluguel(emprestimo, data_devolucao)
        Emprestimo.emprestimos.pop(codigo)
        emprestimo['cliente'].alugueis.remove(codigo)
        emprestimo['loja'].retirar_bikes_alugadas(codigo, data_devolucao, valor, emprestimo['lista_de_bikes'])

    @staticmethod
    def calcular_valor_aluguel(emprestimo, data_devolucao):
        """
        Cálculo do valor a ser pago pelo aluguel das bicicletas.

        :param emprestimo: Objeto Emprestimo
        :param data_devolucao: Data de devolução
        :return: Valor calculado e o período que ficou alugado.
        """
        data_emprestimo = datetime.strptime(emprestimo['data_do_emprestimo'], "%d/%m/%Y %H:%M:%S")
        data_devolucao = datetime.strptime(data_devolucao, "%d/%m/%Y %H:%M:%S")
        diferenca_em_segundos = (data_devolucao - data_emprestimo).total_seconds()
        numero_bikes_alugadas = len(emprestimo['lista_de_bikes'])
        tipo_aluguel = emprestimo['tipo_do_aluguel']
        valor_unitario = Emprestimo.VALORES[emprestimo['tipo_do_aluguel']]['valor']

        # Cálculo considerando, para fins didáticos e de teste
        # 2s para 1 hora (1h -> 3600s)
        # Proporcionalmente temos
        # 48s para um dia (1 dia -> 24 horas -> 86400s)
        # 336s para uma semana (1 semana -> 604800)
        # Para o cálculo real basta substituir o valor das variáveis abaixo.
        hora_em_segundos = 2.0
        dia_em_segundos = 48.0
        semana_em_segundos = 336.0

        if tipo_aluguel == 1:  # por dia
            quantidade_aluguel = (diferenca_em_segundos // hora_em_segundos) \
                                 + (1 if diferenca_em_segundos % hora_em_segundos else 0)
            periodo_cobrado = f'{quantidade_aluguel:.0f} hora(s)'
        elif tipo_aluguel == 2:
            quantidade_aluguel = (diferenca_em_segundos // dia_em_segundos) \
                                 + (1 if diferenca_em_segundos % dia_em_segundos else 0)
            periodo_cobrado = f'{quantidade_aluguel:.0f} dia(s)'
        else:
            quantidade_aluguel = (diferenca_em_segundos // semana_em_segundos) \
                                 + (1 if diferenca_em_segundos % semana_em_segundos else 0)
            periodo_cobrado = f'{quantidade_aluguel:.0f} semana(s)'

        # valor = 0
        if numero_bikes_alugadas >= 3:
            valor = numero_bikes_alugadas * quantidade_aluguel * valor_unitario \
                    * ((100 - Emprestimo.VALORES['DESCONTO_PROMOCAO']) / 100)
        else:
            valor = numero_bikes_alugadas * quantidade_aluguel * valor_unitario

        return valor, periodo_cobrado
