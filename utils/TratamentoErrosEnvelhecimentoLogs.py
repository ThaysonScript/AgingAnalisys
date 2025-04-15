import re
from matplotlib import pyplot as plt
import pandas as pd


file_vbox = 'VBox.log'

class TratamentoErrosEnvelhecimentoLogs:
    def __init__(self, pasta_logs, barras: bool, ponto: bool):
        self.pasta_logs = pasta_logs
        self.barras = barras
        self.ponto = ponto

        if barras:
            self.grafico_barras()

        if ponto:
            self.grafico_ponto()

    def grafico_ponto(self):
        # Lista para armazenar as linhas extraídas
        data = []

        # Abrir o arquivo e ler linha por linha
        with open(f'{self.pasta_logs}/{file_vbox}', "r") as file:
            for line in file:
                # Extração de timestamp e tipo de erro
                match = re.match(r"(\d+:\d+:\d+\.\d+)\s+(VMSetError|ERROR \[COM\]):\s+(.*)", line)

                if match:
                    timestamp = match.group(1)
                    error_type = match.group(2)
                    message = match.group(3)

                    # Adiciona os dados extraídos na lista
                    data.append([timestamp, error_type, message])

        # Criar o DataFrame
        df = pd.DataFrame(data, columns=["Timestamp", "ErrorType", "Message"])

        # Converter o timestamp para horas acumuladas
        def convert_to_hours(timestamp):
            match = re.match(r"(\d+):(\d+):(\d+\.\d+)", timestamp)
            if match:
                hours = int(match.group(1))
                minutes = int(match.group(2))
                seconds = float(match.group(3))
                return hours + minutes / 60 + seconds / 3600
            return 0

        df["Hours"] = df["Timestamp"].apply(convert_to_hours)

        # Agrupar os erros por tipo e tempo
        error_counts = df.groupby(["Hours", "ErrorType"]).size().reset_index(name="ErrorCount")

        # Filtrar os erros, considerando um limite mínimo de ocorrências
        minimum = 1
        filtered_df = error_counts[error_counts["ErrorCount"] >= minimum]

        # Verificar se a coluna 'ErrorCount' é numérica
        filtered_df['ErrorCount'] = pd.to_numeric(filtered_df['ErrorCount'], errors='coerce')

        # Calcular a soma acumulada dos erros para cada tipo de erro
        filtered_df['CumulativeErrorCount'] = filtered_df.groupby('ErrorType')['ErrorCount'].cumsum()

        # Criar o gráfico com as ocorrências acumuladas como pontos
        df_pivot = filtered_df.pivot(columns='ErrorType', values='CumulativeErrorCount')

        # Verificar se df_pivot contém dados numéricos
        if df_pivot.empty or df_pivot.isnull().all().all():
            print("Não há dados numéricos para plotar.")
        else:
            # Plotando com ponto (marker='o')
            ax = df_pivot.plot(marker='o', linestyle='None', ylabel='Número Acumulado de Ocorrências',
                               xlabel='Tempo (Horas)', figsize=(10, 6))
            plt.title("Número Acumulado de Erros por Tipo ao Longo do Tempo")
            # Salvar o gráfico
            fig = ax.get_figure()

            # Salvar o gráfico como um arquivo PNG
            plt.savefig("imagens_plottadas/erros_relacionados_envelhecimento_ponto.png")


    def grafico_barras(self):
        # Lista para armazenar as linhas extraídas
        data = []

        # Abrir o arquivo e ler linha por linha
        with open(f'{self.pasta_logs}/{file_vbox}', "r") as file:
            for line in file:
                # Extração de timestamp e tipo de erro
                match = re.match(r"(\d+:\d+:\d+\.\d+)\s+(VMSetError|ERROR \[COM\]):\s+(.*)", line)

                if match:
                    timestamp = match.group(1)
                    error_type = match.group(2)
                    message = match.group(3)

                    # Adiciona os dados extraídos na lista
                    data.append([timestamp, error_type, message])

        # Criar o DataFrame
        df = pd.DataFrame(data, columns=["Timestamp", "ErrorType", "Message"])

        # # Exibir o DataFrame
        # print(df)
        #
        # Contar as ocorrências de cada tipo de erro
        error_counts = df['ErrorType'].value_counts()

        # Plotar o gráfico de barras
        plt.figure(figsize=(10, 6))
        error_counts.plot(kind='bar', color='skyblue')
        plt.title('Acúmulo de Ocorrências de Erros', fontsize=14)
        plt.xlabel('Tipo de Erro', fontsize=12)
        plt.ylabel('Número de Ocorrências', fontsize=12)
        plt.xticks(rotation=45)
        plt.tight_layout()

        # # Salvar o gráfico como um arquivo PNG
        plt.savefig("imagens_plottadas/erros_relacionados_envelhecimento_barras.png")