import sys


class CommonLogs():
    def __init__(self, PASTA_LOGS=''):
        return {
            'monitoring_cpu':
                f'{PASTA_LOGS}/machine_monitoring-cpu.csv',
                
            'monitoring_disks':
                f'{PASTA_LOGS}/machine_monitoring-disk.csv',
            
            'monitoring_zumbies':
                f'{PASTA_LOGS}/machine_monitoring-zombies.csv',
            
            'monitoring_mem':
                f'{PASTA_LOGS}/machine_monitoring-mem.csv',
                
            'machineHost_server_status':
                f'{PASTA_LOGS}/machineHost_server_status.csv',
                
            'reset_times':
                f'{PASTA_LOGS}/reset_times.csv',
                
            'server_response_time_monitoring':
                f'{PASTA_LOGS}/nginx_response.csv'
        }


class LogsVbox():
    def __init__(self, PASTA_LOGS='', viewCommonLogs=False):
        if viewCommonLogs == True:
            CommonLogs(PASTA_LOGS=PASTA_LOGS)
        else:
            pass
        
        
    def vboxLogsProcess(self, PASTA_LOGS=''):
        return {
            'monitoring_VboxHeadless':
                f'{PASTA_LOGS}/vbox_monitoring-VBoxHeadless.csv',
            
            'monitoring_VboxSvc':
                f'{PASTA_LOGS}/vbox_monitoring-VBoxSVC.csv',
            
            'monitoring_VboxXPCOMIPCD':
                f'{PASTA_LOGS}/vbox_monitoring-VBoxXPCOMIPCD.csv'
        }
    
    
class LogsKvm():
    def __init__(self, PASTA_LOGS='', viewCommonLogs=False):
        if viewCommonLogs == True:
            CommonLogs(PASTA_LOGS=PASTA_LOGS)
        else:
            pass


    def KvmLogsProcess(self, PASTA_LOGS=''):
        return {
            'kvm_Headless':
                f'{PASTA_LOGS}/kvm_Headless_monitoring.csv',
            
            'kvm_libvirtd_service':
                f'{PASTA_LOGS}/kvm_libvirtd_service_monitoring.csv'
        }
    
    
class LogsXen():
    def __init__(self, PASTA_LOGS='', viewCommonLogs=False):
        if viewCommonLogs == True:
            CommonLogs(PASTA_LOGS=PASTA_LOGS)
        else:
            pass


    def XenLogsProcess(self, PASTA_LOGS=''):
        return {
            'xen_monitoring_oxenstored':
                f'{PASTA_LOGS}/xen_monitoring-oxenstored.csv',
            
            'xen_monitoring_xen_balloon':
                f'{PASTA_LOGS}/xen_monitoring-xen-balloon.csv',
                
            'xen_monitoring_xenbus':
                f'{PASTA_LOGS}/xen_monitoring-xenbus.csv',
            
            'xen_monitoring_xenconsoled':
                f'{PASTA_LOGS}/xen_monitoring-xenconsoled.csv'
        }
    
    
class LogsDocker():
    def __init__(self, PASTA_LOGS='', viewCommonLogs=False):
        if viewCommonLogs == True:
            CommonLogs(PASTA_LOGS=PASTA_LOGS)
        else:
            pass


    def dockerOlderLogs(self, PASTA_LOGS=''):
        # vs 20
        return {
            # RUNS
            'runs':
                f'{PASTA_LOGS}/runs.csv',
                
            # --------------------- MACHINE PROCESS
            'cpu':
                f'{PASTA_LOGS}/cpu.csv',
                
            'memory':
                f'{PASTA_LOGS}/memory.csv',
                
            'disk':
                f'{PASTA_LOGS}/disk.csv',
                
            'process':
                f'{PASTA_LOGS}/process.csv',
                
            # ------------------- IMAGE PROCESS
            'nginx':
                f'{PASTA_LOGS}/nginx.csv',
                
            'postgres':
                f'{PASTA_LOGS}/postgres.csv',
                
            'rabbitmq':
                f'{PASTA_LOGS}/rabbitmq.csv',
                
            'redis':
                f'{PASTA_LOGS}/redis.csv',
                
            # ------------------- CONTAINER PROCESS
            'docker': 
                f'{PASTA_LOGS}/docker.csv',
                
            'dockerd': 
                f'{PASTA_LOGS}/dockerd.csv',
                
            'containerd': 
                f'{PASTA_LOGS}/containerd.csv',
                
            'containerd-shim': 
                f'{PASTA_LOGS}/containerd-shim.csv',
                
            'docker-proxy': 
                f'{PASTA_LOGS}/docker-proxy.csv',
                
            'runc': 
                f'{PASTA_LOGS}/runc.csv',
                
            'containerd': 
                f'{PASTA_LOGS}/containerd.csv',
                
            'containerd-shim': 
                f'{PASTA_LOGS}/containerd-shim.csv',
                
            'runc': 
                f'{PASTA_LOGS}/runc.csv',
                
            # -------------------- SERVICE PROCESS
            'java': 
                f'{PASTA_LOGS}/java.csv',
                
            'beam.smp': 
                f'{PASTA_LOGS}/beam.smp.csv',
                
            'initdb': 
                f'{PASTA_LOGS}/initdb.csv',
                
            'mysqld': 
                f'{PASTA_LOGS}/mysqld.csv',
                
            'postgres_process': 
                f'{PASTA_LOGS}/postgres_process.csv'
        }
        
        
    def dockerLatestRealeseLogs(self, PASTA_LOGS=''):
        # vs 26
        return {
            # RUNS
            'runs':
                f'{PASTA_LOGS}/runs.csv',
                
            # --------------------- MACHINE PROCESS
            'cpu':
                f'{PASTA_LOGS}/cpu.csv',
                
            'memory':
                f'{PASTA_LOGS}/memory.csv',
                
            'disk':
                f'{PASTA_LOGS}/disk.csv',
                
            'process':
                f'{PASTA_LOGS}/process.csv',
                
            # ------------------- IMAGE PROCESS
            'nginx':
                f'{PASTA_LOGS}/nginx.csv',
                
            'postgres':
                f'{PASTA_LOGS}/postgres.csv',
                
            'rabbitmq':
                f'{PASTA_LOGS}/rabbitmq.csv',
                
            'redis':
                f'{PASTA_LOGS}/redis.csv',
                
            # ------------------- CONTAINER PROCESS
            'docker': 
                f'{PASTA_LOGS}/docker.csv',
                
            'dockerd': 
                f'{PASTA_LOGS}/dockerd.csv',
                
            'containerd': 
                f'{PASTA_LOGS}/containerd.csv',
                
            'containerd-shim': 
                f'{PASTA_LOGS}/containerd-shim.csv',
                
            'docker-proxy': 
                f'{PASTA_LOGS}/docker-proxy.csv',
                
            'runc': 
                f'{PASTA_LOGS}/runc.csv',
                
            'containerd': 
                f'{PASTA_LOGS}/containerd.csv',
                
            'containerd-shim': 
                f'{PASTA_LOGS}/containerd-shim.csv',
                
            'runc': 
                f'{PASTA_LOGS}/runc.csv',
                
            # -------------------- SERVICE PROCESS
            'java': 
                f'{PASTA_LOGS}/java.csv',
                
            'beam.smp': 
                f'{PASTA_LOGS}/beam.smp.csv',
                
            'initdb': 
                f'{PASTA_LOGS}/initdb.csv',
                
            'mysqld': 
                f'{PASTA_LOGS}/mysqld.csv',
                
            'postgres_process': 
                f'{PASTA_LOGS}/postgres_process.csv'
        }
    
    
class LogsPodman():
    def __init__(self, PASTA_LOGS='', viewCommonLogs=False):
        if viewCommonLogs == True:
            CommonLogs(PASTA_LOGS=PASTA_LOGS)
        else:
            pass


    def PodmanLogsProcess(self, PASTA_LOGS=''):
        # vs 4.9
        return {
            # RUNS
            'runs':
                f'{PASTA_LOGS}/runs.csv',
                
            # --------------------- MACHINE PROCESS
            'cpu':
                f'{PASTA_LOGS}/cpu.csv',
                
            'disk':
                f'{PASTA_LOGS}/disk.csv',
                
            'memory':
                f'{PASTA_LOGS}/memory.csv',
                
            'process':
                f'{PASTA_LOGS}/process.csv',
                
            # ------------------- IMAGE PROCESS
            'nginx':
                f'{PASTA_LOGS}/nginx.csv',
                
            'postgres':
                f'{PASTA_LOGS}/postgres.csv',
                
            'rabbitmq':
                f'{PASTA_LOGS}/rabbitmq.csv',
                
            'redis':
                f'{PASTA_LOGS}/redis.csv',
                
            # ------------------- CONTAINER PROCESS
            'podman':
                f'{PASTA_LOGS}/podman.csv',
                
            'conmon':
                f'{PASTA_LOGS}/conmon.csv',
                
            'cron':
                f'{PASTA_LOGS}/cron.csv',
                
            'crun':
                f'{PASTA_LOGS}/crun.csv',
                
            'systemd':
                f'{PASTA_LOGS}/systemd.csv',
            
            # -------------------- SERVICE PROCESS
            'java':
                f'{PASTA_LOGS}/java.csv',
                
            'postgres_process':
                f'{PASTA_LOGS}/postgres_process.csv',
                
            'mysqld':
                f'{PASTA_LOGS}/mysqld.csv',
                
            'initdb':
                f'{PASTA_LOGS}/initdb.csv',
                
            'beam.smp':
                f'{PASTA_LOGS}/beam.smp.csv'
        }


class LogsJmeter():
    def __init__(self, PASTA_LOGS='', viewCommonLogs=False):
        if viewCommonLogs == True:
            CommonLogs(PASTA_LOGS=PASTA_LOGS)
        else:
            pass
        
    
    def jmeterLogs(self, PASTA_LOGS=''):
        return {
        'jmeter_log':
            f'{PASTA_LOGS}/jmeter.log'
        }

class Logs():
    def __init__(self):
        nomePasta = str(
            input('''
            Digite a pasta de logs a partir do seu diretorio atual ou caminho completo: 
            ''')
        )
        
        print('''
              [1] - VBOX
              [2] - KVM
              [3] - XEN
              [4] - DOCKER
              [5] - PODMAM
              [6] - JMETER
        ''')
        tipoVirtualizador = int(input('Digite o Virtualizador de Escolha: '))
        ativarCommonLogs = bool(input('[True] - ativar logs communs\n[False] - não ativar logs communs\n\n'))
        
        if tipoVirtualizador == 1:
            LogsVbox(PASTA_LOGS=nomePasta, viewCommonLogs=ativarCommonLogs)
            LogsVbox(viewCommonLogs=ativarCommonLogs).vboxLogsProcess()
            
            
        elif tipoVirtualizador == 2:
            LogsKvm(PASTA_LOGS=nomePasta, viewCommonLogs=ativarCommonLogs)
            LogsKvm().KvmLogsProcess()
            
            
        elif tipoVirtualizador == 3:
            LogsXen(PASTA_LOGS=nomePasta, viewCommonLogs=ativarCommonLogs)
            LogsXen().XenLogsProcess()
          
            
        elif tipoVirtualizador == 4:
            LogsDocker(PASTA_LOGS=nomePasta, viewCommonLogs=ativarCommonLogs)
            
            dockerType = int(input('[1] - Docker antigo\n[2] - Docker atual: '))
            if dockerType == 1:
                LogsDocker().dockerOlderLogs()
            elif dockerType == 2:
                LogsDocker().dockerLatestRealeseLogs()
            else:
                print('valor invalido, saindo.....')
                sys.exit(1)
            
            
        elif tipoVirtualizador == 5:
            LogsPodman(PASTA_LOGS=nomePasta, viewCommonLogs=ativarCommonLogs)
            LogsPodman().PodmanLogsProcess()
            
            
        elif tipoVirtualizador == 6:
            LogsJmeter(PASTA_LOGS=nomePasta, viewCommonLogs=ativarCommonLogs)
            LogsJmeter(viewCommonLogs=ativarCommonLogs).jmeterLogs(PASTA_LOGS=nomePasta)
            
            
        else:
            print('Digite Numero entre 1 a 6')
            sys.exit(1)