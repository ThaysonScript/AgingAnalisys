import sys
import pandas as pd

class ManipulationPandas:
    def __init__(self):
        pass
    
    
    def carregarLogDataframe(self, nomeArquivo='', separador=';', separadorDecimal=',', dayfirst=False, datetimeName='date_time', parse_date=False):
        if parse_date == True:
            try:
                return pd.read_csv(nomeArquivo, delimiter=separador, decimal=separadorDecimal, dayfirst=dayfirst, parse_dates=[datetimeName]).rename(columns={datetimeName: 'seconds'})
            
            except ValueError:
                try:
                    return pd.read_csv(nomeArquivo, delimiter=separador, decimal=separadorDecimal, dayfirst=dayfirst, parse_dates=['time']).rename(columns={'time': 'seconds'})        

                except Exception as e:
                    return f'Erro ao ler o arquivo CSV: {e}'
                
                finally:
                    sys.exit(1)
        
        return pd.read_csv(nomeArquivo, delimiter=';')
    
    
    def droparColunasNulasVazias(self, dataframe: pd):
        return dataframe.dropna()
    
    
    def converterColunaDatetime(self, dataframe: pd, column):
        dataframe[f'{column}'] = pd.to_datetime(dataframe[f'{column}'])
        return dataframe
    
    
    def definirIndex(self, dataframe: pd, index: str, indexWithReplace=False):
        if indexWithReplace == True:
            return dataframe.set_index(index).replace(',', '.', regex=True).apply(lambda x: pd.to_numeric(x, errors='ignore'))
        return dataframe.set_index(index)
    
    
    def converterTempo(self, dataframe, newName='', atualName=None, returnNewColumn=False):
        if returnNewColumn == True:
            dataframe[f'{newName}'] = (dataframe.index - dataframe.index[0]).total_seconds() / 3600
            return dataframe
        
        elif returnNewColumn == False and atualName != None:
            dataframe[f'{atualName}'] = (dataframe[f'{atualName}'] - dataframe[f'{atualName}'][0]).dt.total_seconds() / 3600
            return dataframe
            
        else:
            print('\n\nErro em converter tempo no modulo de manipular dataframe no pandas\n\n')
            sys.exit(1)
    
    
    def filtrarDados(self, dataframe, column, condicao, ocorrencia):
        return dataframe[f'{dataframe[column]} {condicao} {ocorrencia}']
    
    
    def salvarFigura(self, ax, nomeFigura):
        fig = ax.get_figure()
        fig.savefig(f'{nomeFigura}')
        
        
    def fixarValoresInteirosGrafico(self, ax):
        # transformar decimais em inteiros
        ax.set_yticks(ax.get_yticks())
        ax.set_yticklabels(ax.get_yticks().astype(int))
        
        
    def plotarGrafico(self, dataframe: pd, yLabel, xLabel, figureSize):
        return dataframe.plot(ylabel=yLabel, xlabel=xLabel, figsize=figureSize)
    
    
    def pivotarValoresDataframe(self, dataframe: pd, column, value):
        return dataframe.pivot(columns=column, values=value)
    
    
    def multiplicarColunasDataframe(self, dataframe: pd, colunasParaMultiplicar, multiplicarPor=1):
        # perform data multiplication
        cols_to_multiply = cols_to_multiply if len(colunasParaMultiplicar) != 0 else dataframe.columns
        dataframe[cols_to_multiply] = dataframe[cols_to_multiply].mul(multiplicarPor)
        
        
    def dividirColunasDataframe(dataframe: pd, colunasParaDividir, dividirPor):
        cols_to_divide = cols_to_divide if len(colunasParaDividir) != 0 else dataframe.columns
        dataframe[cols_to_divide] = dataframe[cols_to_divide].div(dividirPor)
        
        
    def converterTempoRespostaServico(self, dataframe: pd, nomeArquivo):
        if nomeArquivo == './plotagem/registros de monitoramento dos testes de envelhecimento/outros/logs/response_times.csv':
            return dataframe['response_time'] / 1000  