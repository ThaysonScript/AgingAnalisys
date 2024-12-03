import threading
import sys
from utils.CarregarPlottarGraficos import CarregarPlottarGraficos
from utils.CreateDirectory import CreateDirectory

class Main:
    def __init__(self):
        CreateDirectory()
                
        
    def print_usage(self):
        print('---------------- VIRTUALIZADORES ----------------')
        print('Digite [1] para vbox')
        print('Digite [2] para kvm')
        print('Digite [3] para xen')
        print('Digite [4] para lxc')
        print('\n----------------- CONTAINERS --------------------')
        print('Digite [5] para docker antigo')
        print('Digite [6] para docker novo')
        print('Digite [7] para podman')
        
        return int(input('Escolha: '))
    
    
    def startPlots(self, typePlot):
        if typePlot == 1:
            CarregarPlottarGraficos().vbox_plotttar()
        
        elif typePlot == 2:
            CarregarPlottarGraficos().kvm_plottar()
            
        elif typePlot == 3:
            CarregarPlottarGraficos().xen_plottar()
            
        elif typePlot == 4:
            CarregarPlottarGraficos().lxc_plottar()
            
        elif typePlot == 5:
            CarregarPlottarGraficos().docker_antigo()
            
        elif typePlot == 6:
            CarregarPlottarGraficos().docker_novo()
            
        elif typePlot == 7:
            CarregarPlottarGraficos().podman()
            
        else:
            print('Escolha uma opção válida!')
            sys.exit(1)
        

if __name__ == '__main__':
    Main().startPlots(
        Main().print_usage()
    )
