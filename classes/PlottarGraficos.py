import sys
from utils.CreateDirectory import CreateDirectory
from utils.ManipulationPandas import ManipulationPandas
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression


class PlottarGraficos(ManipulationPandas):
    def __init__(self):
        super().__init__()
        
    def plottar(self,
        nomeArquivo='', ylabel='', 
        datetimeName="date_time", title=None, 
        separador=';', separadorDecimal=",", 
        dayfirst=False, multiply=1, division=1, 
        decimals_quantity=2, includeColYlabel=False, 
        cols_to_divide=[], cols_to_multiply=[]
    ):
        print(f'\n-------------------------------------- Executando plotagens [ {nomeArquivo} ] --------------------------------------')
        
        df = ManipulationPandas().carregarLogDataframe(nomeArquivo, separador, separadorDecimal, dayfirst, datetimeName, parse_date=True)
        ManipulationPandas().verificarErrosEGravar(dataframe=df, nomeArquivo=nomeArquivo)
        
        df = ManipulationPandas().droparColunasNulasVazias(dataframe=df)
        
        # df['seconds'] = (df['seconds'] - df['seconds'][0]).dt.total_seconds() / 3600
        df = ManipulationPandas().converterTempo(dataframe=df, atualName='seconds')
        
        # df = df.set_index('seconds').replace(',', '.', regex=True).apply(lambda x: pd.to_numeric(x, errors='ignore'))
        df = ManipulationPandas().definirIndex(dataframe=df, index='seconds', indexWithReplace=True)

        # # perform data multiplication
        # cols_to_multiply = cols_to_multiply if len(cols_to_multiply) != 0 else df.columns
        # df[cols_to_multiply] = df[cols_to_multiply].mul(multiply)
        df = ManipulationPandas().multiplicarColunasDataframe(dataframe=df, colunasParaMultiplicar=cols_to_multiply, multiplicarPor=multiply)
        
        
        # if nomeArquivo == './plotagem/registros de monitoramento dos testes de envelhecimento/outros/logs/response_times.csv':
        #     df['response_time'] = df['response_time'] / 1000    
        if nomeArquivo.endswith('nginx_response.csv'):
            df = ManipulationPandas().converterTempoRespostaServico(dataframe=df)
        
        
        # # perform data division
        # cols_to_divide = cols_to_divide if len(cols_to_divide) != 0 else df.columns
        # df[cols_to_divide] = df[cols_to_divide].div(division)
        df = ManipulationPandas().dividirColunasDataframe(dataframe=df, colunasParaDividir=cols_to_divide, dividirPor=division)
            
        for col in df.columns:
            df = df.loc[df[col].drop_duplicates().index]
            col_mix = col + " " + ylabel if type(ylabel) is str and includeColYlabel else ylabel

            df[col] = df[col].fillna(0)

            x = df.index.to_numpy().reshape((-1, 1))
            y = df[col].to_numpy().reshape((-1, 1))
            
            
             # Criar scatter plot
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.scatter(df.index, df[col], color='DarkBlue', label='Data points')
            
            # Adicionar linha de regressão
            model = LinearRegression()
            model.fit(x, y.reshape((-1, 1)))
            y_pred = model.predict(x)
            
            # Configurações do gráfico
            ax.plot(df.index, y_pred, color='red', label='Linear regression')
            ax.set_xlabel('Time(h)')
            ax.set_ylabel(col_mix if type(ylabel) is str else ylabel[col] if type(ylabel) is dict and col in ylabel else col)
            ax.set_title(title if type(title) is str else title[col] if type(title) is dict and col in title else col)
            ax.legend()

            # Salvar gráfico
            ManipulationPandas().salvarFigura(ax=ax, nomeFigura=f'./imagens_plottadas/{title}-{col}.png')
            plt.close(fig)
