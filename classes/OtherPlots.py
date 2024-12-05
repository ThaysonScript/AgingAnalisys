import glob
import os
from pathlib import Path
import re
import sys

import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np


def plot_time_series(save_folder, file_path, title, x_label, y_label, max_labels=20):
    # Carregar os dados do arquivo CSV
    df = pd.read_csv(file_path, sep=";")

    # Converter a coluna 'date_time' para o tipo datetime
    df['date_time'] = pd.to_datetime(df['date_time'])

    # Calcular o tempo decorrido em horas
    df['elapsed_hours'] = (df['date_time'] - df['date_time'].min()).dt.total_seconds() / 3600

    # Converter valores de nanosegundos para segundos (exceto 'date_time' e 'elapsed_hours')
    for col in df.columns:
        if col not in ['date_time', 'elapsed_hours']:
            df[col] = df[col] / 1e9  # Convertendo nanosegundos para segundos

    # Para cada coluna (exceto 'date_time' e 'elapsed_hours'), plota um gráfico separado
    for col in df.columns:
        if col not in ['date_time', 'elapsed_hours']:
            plt.figure(figsize=(10, 6))

            # Plotar a série temporal com o eixo X em horas
            plt.plot(df['elapsed_hours'], df[col], label=col)

            # Adicionar título e rótulos dos eixos
            plt.title(f"{title} - {col}")
            plt.xlabel(x_label)
            plt.ylabel(y_label)

            # Adicionar legenda
            plt.legend()

            # Ajustar layout para evitar sobreposição e salvar o gráfico
            plt.tight_layout()
            plt.grid(True)
            plt.savefig(save_folder.joinpath(f"{title} - {col}.png"))

    return 1



def plot(
        folder,
        filename,
        ylabel,
        datetime="date_time",
        title=None, separator=';',
        decimal_separator=",",
        division=1,
        includeColYlabel=False,
        cols_to_divide=None
):
    if cols_to_divide is None:
        cols_to_divide = []
    print(f"Plotting {filename}")
    df = pd.read_csv(
        folder.joinpath(filename),
        sep=separator,
        decimal=decimal_separator,
        dayfirst=False,
        parse_dates=[datetime]).rename(columns={datetime: 'seconds'})

    df['seconds'] = (df['seconds'] - df['seconds'][0]).dt.total_seconds() / 3600
    df = df.set_index('seconds').replace(',', '.', regex=True).apply(lambda x: pd.to_numeric(x))
    cols_to_divide = cols_to_divide if len(cols_to_divide) != 0 else df.columns
    df[cols_to_divide] = df[cols_to_divide].div(division)

    for col in df.columns:
        col_mix = col + " " + ylabel if type(ylabel) is str and includeColYlabel else ylabel

        df[col] = df[col].fillna(0)

        x = df.index.to_numpy().reshape((-1, 1))
        y = df[col].to_numpy().reshape((-1, 1))

        model = LinearRegression()
        model.fit(x, y)

        Y_pred = model.predict(x)

        ax = df.plot(
            y=col,
            legend=0,
            xlabel='Time(h)',
            ylabel=col_mix if type(ylabel) is str else ylabel[col] if type(
                ylabel) is dict and col in ylabel else col,
            title=title if type(title) is str else title[col] if type(title) is dict and col in title else col,
            figsize=(10, 5),
            style='k',
        )

        # Adicionar a linha da regressão
        ax.plot(x, Y_pred, color='red')
        fig = ax.get_figure()
        fig.savefig(folder.joinpath('plots_img').joinpath(f"{title}-{col}.png"))
        plt.close('all')
    return 1



def plot_jmeter(folder, file_name, ignore_chunck=False, chunk_size=10000000, throughput_interval=60):
    if not ignore_chunck:
        chunks = pd.read_csv(folder.joinpath(file_name), chunksize=chunk_size, low_memory=False, sep=",")

        # DataFrame acumulativo para todas as chunks
        df_total = pd.DataFrame()
        for i, chunk in enumerate(chunks):
            print(f'Processing chunk {i}')
            # Acumula os dados do chunk no dataframe total
            df_total = pd.concat([df_total, chunk], ignore_index=True)
    else:
        df_total = pd.read_csv(folder.joinpath(file_name), low_memory=False, sep=",")


    print(df_total)

    # Converter 'timeStamp' para segundos (relativos ao início)
    df_total['timeStamp'] = (df_total['timeStamp'] - df_total['timeStamp'].min()) / 1000  # Em segundos

    # Gerar as métricas gerais
    metricas_geral = calcular_metricas(df_total)
    print("General metrics (considering all chunks):")
    for key, value in metricas_geral.items():
        print(f"{key}: {value}")

    # Obter os labels únicos da coluna 'label'
    unique_labels = df_total['label'].unique()

    # Gerar gráficos de série temporal para cada label
    for label in unique_labels:
        df_label = df_total[df_total['label'] == label]

        # Gerar o gráfico de série temporal para o label específico
        plt.figure(figsize=(10, 6))
        plt.plot(df_label['timeStamp'] / 3600, df_label['elapsed'], label=f'Response Time (ms) - {label}', color='blue')

        # Configurações do gráfico
        plt.title(f'Time Series of Response Time - {label}')
        plt.xlabel('Time (hours)')
        plt.ylabel('Response Time (seconds)')
        plt.grid(True)
        plt.legend()

        # Exibir o gráfico
        plt.tight_layout()
        plt.savefig(folder.joinpath('plots_img/jmeter').joinpath(f"Time Series of Response Time - {label}.png"))
        plt.show()

    # Gerar o gráfico de série temporal geral (todos os labels juntos)
    plt.figure(figsize=(10, 6))
    plt.plot(df_total['timeStamp'] / 3600, df_total['elapsed'], label='Overall Response Time (ms)', color='red')

    # Configurações do gráfico geral
    plt.title('Time Series of Overall Response Time')
    plt.xlabel('Time (hours)')
    plt.ylabel('Response Time (seconds)')
    plt.grid(True)
    plt.legend()

    # Exibir o gráfico geral
    plt.tight_layout()
    plt.savefig(folder.joinpath('plots_img/jmeter').joinpath('Time Series of Overall Response Time.png'))
    plt.show()

    # Adiciona a coluna de intervalo de tempo em minutos
    df_total['timeBucket'] = (df_total['timeStamp'] // throughput_interval) * throughput_interval

    # Calcular a vazão em cada intervalo de tempo
    throughput_df = df_total.groupby('timeBucket').size().reset_index(name='Throughput')

    # Gerar o gráfico de série temporal da vazão
    plt.figure(figsize=(10, 6))
    plt.plot(throughput_df['timeBucket'] / 3600, throughput_df['Throughput'], label='Throughput (requests/interval)', color='green')

    # Configurações do gráfico de vazão
    plt.title('Time Series of Throughput')
    plt.xlabel('Time (hours)')
    plt.ylabel(f'Throughput (requests per {throughput_interval} seconds)')
    plt.grid(True)
    plt.legend()

    # Exibir o gráfico de vazão
    plt.tight_layout()
    plt.savefig(folder.joinpath('plots_img/jmeter').joinpath('Time Series of Throughput.png'))
    plt.show()
    return 1

def calcular_metricas(df):
    metricas = {}

    # Amostras (# Samples)
    metricas['# Samples'] = df.shape[0]

    # Média (Mean)
    metricas['Mean'] = df['elapsed'].mean() / 1000  # Converte para segundos

    # Min (Minimum)
    metricas['Min'] = df['elapsed'].min() / 1000  # Converte para segundos

    # Max (Maximum)
    metricas['Max'] = df['elapsed'].max() / 1000  # Converte para segundos

    # Desvio Padrão (Standard Deviation)
    metricas['Standard Deviation'] = df['elapsed'].std() / 1000  # Converte para segundos

    # Contagem de Erros (Number of Errors)
    metricas['Error Count'] = df[df['success'] == False].shape[0]

    # % de Erro (Percentage of Errors)
    metricas['Error Percentage'] = (metricas['Error Count'] / metricas['# Samples']) * 100

    # Vazão (Throughput)
    total_time = (df['timeStamp'].max() - df['timeStamp'].min())  # Em segundos
    metricas['Throughput'] = metricas['# Samples'] / total_time if total_time > 0 else 0

    return metricas


def plot_fragmentation(folder, merge_equals=True, process_per_plot=20, relevant_maximum=200,
                       time_threshold=None, name_filter=None, adjust_x_limits=False):
    
    folder = Path(folder)
    
    # Processar todos os arquivos sem ignorar partes do processo
    final_dataset = process_all_files(folder)

    # Converter 'process_occurrences' para numérico
    final_dataset['process_occurrences'] = pd.to_numeric(final_dataset['process_occurrences'], errors='coerce').fillna(0).astype(int)
    

    if merge_equals:
        lastFounds = {}
        for index, row in final_dataset.iterrows():
            name, pid = extract_name_pid(row['process'])
            value = row['process_occurrences']

            # Atualiza a coluna 'process' com o 'name'
            final_dataset.loc[index, 'process'] = name

            # Atualiza 'process_occurrences' se 'name' estiver em lastFounds
            if name in lastFounds:
                final_dataset.loc[index, 'process_occurrences'] += lastFounds[name]

            # Atualiza lastFounds com o novo valor de 'process_occurrences'
            lastFounds[name] = final_dataset.loc[index, 'process_occurrences']

    # 1. Agrupar os dados pelo processo
    grouped = final_dataset.groupby('process')

    # 2. Criar um subdataset para cada processo
    subdatasets = {process: group for process, group in grouped}

    # 3. Filtrar os subdatasets onde o valor da última ocorrência é maior que o limite
    subdatasets_filtrados = {
        process: data for process, data in subdatasets.items()
        if data['process_occurrences'].iloc[-1] > relevant_maximum
    }

    # Filtro adicional por tempo, se 'time_threshold' for especificado
    if time_threshold is not None:
        subdatasets_filtrados = {
            process: data for process, data in subdatasets_filtrados.items()
            if (data['datetime'].max() - data['datetime'].min()).total_seconds() / 3600 <= time_threshold
        }

    # Filtro adicional por nome de processo, se 'name_filter' for especificado
    if name_filter is not None:
        subdatasets_filtrados = {
            process: data for process, data in subdatasets_filtrados.items()
            if any(f in process for f in name_filter)
        }

    # 4. Ordenar os subdatasets filtrados pelo último valor de 'process_occurrences' (do menor para o maior)
    subdatasets_ordenados = dict(
        sorted(
            subdatasets_filtrados.items(),
            key=lambda item: item[1]['process_occurrences'].iloc[-1],
        )
    )

    # 5. Definir o tempo máximo entre todos os subdatasets filtrados, se o ajuste do eixo X estiver ativado
    if adjust_x_limits:
        max_time = max(
            (data['datetime'].max() - data['datetime'].min()).total_seconds() / 3600
            for data in subdatasets_ordenados.values()
        )

    # 6. Plotar os gráficos apenas com os processos que atendem ao critério e já estão ordenados
    process_list = list(subdatasets_ordenados.keys())
    num_plots = len(process_list) // process_per_plot + 1

    for i in range(num_plots):
        fig, ax = plt.subplots(figsize=(12, 8))
        processes_to_plot = process_list[i * process_per_plot:(i + 1) * process_per_plot]

        for process in processes_to_plot:
            subset = subdatasets_ordenados[process]
            # Calcular o tempo decorrido em horas a partir do primeiro timestamp
            subset['time_in_hours'] = (subset['datetime'] - subset['datetime'].min()).dt.total_seconds() / 3600
            # Plotando o gráfico com linhas retas entre os pontos, sem suavização
            ax.step(subset['time_in_hours'], subset['process_occurrences'], where='post', label=f'{process}')

        ax.legend(loc='best', fontsize='small', title='Process')
        ax.set_title(
            f'Time Series of memory fragmentation - Proccess {i * process_per_plot + 1} a {(i + 1) * process_per_plot}')
        ax.set_xlabel('Time (hours)')
        ax.set_ylabel('Process occurences')

        # Ajustar o intervalo de tempo no eixo X de 0 até o tempo máximo encontrado, se a opção estiver ativada
        if adjust_x_limits:
            ax.set_xlim([0, max_time])

        # Aumentar a densidade de rótulos no eixo X e Y
        ax.locator_params(axis='x', nbins=20)  # Dobrar a quantidade de labels no eixo X
        ax.locator_params(axis='y', nbins=20)  # Dobrar a quantidade de labels no eixo Y

        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.grid(True)
        
        folder = Path('./imagens_plottadas/')
        plt.savefig(folder.joinpath(f"Time Series of memory fragmentation - Proccess {i * process_per_plot + 1} a {(i + 1) * process_per_plot}.png"))
        #plt.show()
    return 1


def extract_name_pid(process_str):
    """Extrai o nome do processo e o PID da string 'nome_do_processo(pid)'."""
    match = re.match(r"(.*)\((\d+)\)", process_str)
    if match:
        return match.groups()  # Retorna (nome_do_processo, pid)
    return process_str, None


def load_and_split_dataset(file_path):
    # Load the dataset
    df = pd.read_csv(file_path, sep=';')
    df['process_occurrences'] = pd.to_numeric(df['process_occurrences'], errors='coerce').fillna(0).astype(int)

    # Create a group identifier that increments each time 'process' is 'EMPTIED'
    df['group'] = (df['process'] == 'EMPTIED').cumsum()

    # Remove 'EMPTIED' rows
    df = df[df['process'] != 'EMPTIED']

    # Split the DataFrame into subdatasets based on the group identifier
    subdatasets = [group_df.reset_index(drop=True) for _, group_df in df.groupby('group')]

    return subdatasets


def process_subdatasets(subdatasets, process_counts):
    # Iterar sobre cada subdataset
    for i, subdataset in enumerate(subdatasets):
        # Converter a coluna 'datetime' para um objeto datetime
        subdataset['datetime'] = pd.to_datetime(subdataset['datetime'], format='%a %b %d %H:%M:%S %Y')

        for index, row in subdataset.iterrows():
            # Extrair nome e pid da coluna 'process'
            process_name, pid = extract_name_pid(row['process'])
            parent_name, ppid = extract_name_pid(row['parent'])

            # Chave que identifica o processo
            process_key = (process_name, parent_name, row['UID'], pid, ppid)

            # Verificar se o processo já foi visto antes
            if process_key in process_counts:
                # Incrementar o valor de 'process_occurrences' com base na última vez que o processo foi encontrado
                subdataset.at[index, 'process_occurrences'] += process_counts[process_key]

            # Atualizar o contador com o valor atual de 'process_occurrences'
            process_counts[process_key] = subdataset.at[index, 'process_occurrences']

        # Substitui o subdataset processado pelo novo
        subdatasets[i] = subdataset

    return subdatasets, process_counts


def process_all_files(directory):
    # Encontrar todos os arquivos que começam com 'fragmentation_'
    
    pattern = os.path.join(directory, '*fragmentation.csv')
    files = glob.glob(pattern)

    all_datasets = []
    process_counts = {}  # Armazenará os processos do último subdataset processado

    for file_path in files:
        print(f"Processando arquivo: {file_path}")
        # Carregar e dividir o dataset em subdatasets
        subdatasets = load_and_split_dataset(file_path)

        # Processar cada subdataset e atualizar as contagens de processos
        processed_subdatasets, process_counts = process_subdatasets(
            subdatasets,
            process_counts
        )

        # Unir todos os subdatasets processados
        merged_dataset = pd.concat(processed_subdatasets, ignore_index=True)

        # Adicionar ao conjunto de todos os datasets
        all_datasets.append(merged_dataset)

    # Concatenar todos os datasets em um só
    final_dataset = pd.concat(all_datasets, ignore_index=True)
    return final_dataset
