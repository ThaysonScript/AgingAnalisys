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
        print('Digite [4] para lxd')
        print('\n----------------- CONTAINERS --------------------')
        print('Digite [5] para docker antigo')
        print('Digite [6] para docker novo')
        print('Digite [7] para podman')
        
        return int(input('Escolha: '))
    
    
    def startPlots(self, typePlot):
        if typePlot == 1:
            CarregarPlottarGraficos(typePlot).vbox_plotttar()
        
        elif typePlot == 2:
            CarregarPlottarGraficos(typePlot).kvm_plottar()
            
        elif typePlot == 3:
            CarregarPlottarGraficos(typePlot).xen_plottar()
            
        elif typePlot == 4:
            CarregarPlottarGraficos(typePlot).lxd_plottar()
            
        elif typePlot == 5:
            CarregarPlottarGraficos(typePlot).docker_antigo()
            
        elif typePlot == 6:
            CarregarPlottarGraficos(typePlot).docker_novo()
            
        elif typePlot == 7:
            CarregarPlottarGraficos(typePlot).podman()
            
        else:
            print('Escolha uma opção válida!')
            sys.exit(1)
        

if __name__ == '__main__':
    Main().startPlots(
        Main().print_usage()
    )
