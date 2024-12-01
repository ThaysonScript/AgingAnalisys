from utils.ManipulationPandas import ManipulationPandas

class PlottarFragmentado:
    def __init__(self):
        pass
    
    
    def analisar(self, minimum_process_occurrences=1):
        objeto = ManipulationPandas(pastaLogs="")
        
        df = objeto.carregarLogDataframe('./fragmentation.csv')
        
        df = objeto.converterColunaDatetime(df, 'datetime')
        
        df = objeto.definirIndex(df, 'datetime')
        
        df = objeto.converterTempo(df, 'time_passed', returnNewColumn=True)
        
        # Resetting the index 'datetime' to use 'time_passed' as index
        df = objeto.definirIndex(df, 'time_passed')
        
        df_filtered = df[df['process_occurrences'] >= minimum_process_occurrences]

        df_pivot = objeto.pivotarValoresDataframe(dataframe=df_filtered, column='process', value='process_occurrences')
        
        ax = objeto.plotarGrafico(dataframe=df_pivot, yLabel='Process occurrences (qtt)', xLabel='Time(H)', figureSize=(10, 6))
        
        objeto.fixarValoresInteirosGrafico(ax=ax)
        
        # Save the figure
        objeto.salvarFigura(ax=ax, nomeFigura='./fragmentação.png')
