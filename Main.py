from classes.PlottarGraficos import PlottarGraficos
from classes.PlottarFragmentado import PlottarFragmentado
from utils.CreateDirectory import CreateDirectory

class Main:
    def __init__(self):
        CreateDirectory()
        PlottarFragmentado().analisar()
        PlottarGraficos(pastaLogs='').plottar()
        
        
Main()