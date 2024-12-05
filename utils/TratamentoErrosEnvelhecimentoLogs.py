

import re
from matplotlib import pyplot as plt
import pandas as pd


class TratamentoErrosEnvelhecimentoLogs():
    def __init__(self, pasta_logs):
        pass
    
        # Lista para armazenar as linhas extraídas
        data = []

        # Abrir o arquivo e ler linha por linha
        with open(f'{pasta_logs}/VBox_log_2', "r") as file:
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

        # Exibir o DataFrame
        print(df)

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

        # Salvar o gráfico como um arquivo PNG
        plt.savefig("imagens_plottadas/erros_relacionados_envelhecimento.png")