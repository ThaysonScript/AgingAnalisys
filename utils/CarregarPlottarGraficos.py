import sys
from classes.PlottarFragmentado import PlottarFragmentado
from classes.PlottarGraficos import PlottarGraficos
from classes.OtherPlots import plot_fragmentation
from utils.TratamentoErrosEnvelhecimentoLogs import TratamentoErrosEnvelhecimentoLogs
from utils.Logs import Logs


class CarregarPlottarGraficos():
    def __init__(self, tipo_virtualizador):
        self.virtualizador = tipo_virtualizador
        
        
    def _common_ylabels(self):
        return {
            'cpu': 'CPU Usage (percentage)',
            'mem': 'Memory Usage (percentage)',
            'vmrss': 'Resident Set Size Memory Usage (MB)',
            'vsz': 'Virtual Memory Size Usage (MB)',
            'threads': 'Number of Threads (QTT)',
            'swap': 'Used Swap Memory (MB)'
        }
        
    
    def _common_cpu_labels(self):
        return {
            '%usr': 'CPU time running processes in user space.',
            '%nice': 'CPU running processes in user space (low priority).',
            '%sys': 'CPU running in kernel space, such as system calls.',
            '%iowait': 'CPU idle, waiting for input/output (I/O).',
            '%soft': 'CPU processing software interrupts.'
        }
    
    
    # ------------------------------------------------ VIRTUALIZADORES ------------------------------------------- #
    def vbox_plotttar(self):
        # PlottarGraficos().plottar(
        #     title="JMETER",
        #     filename=jmeter['jmeter_log'],
        #     ylabel='(none)',
        #     dayfirst=True, includeColYlabel=True
        # )
        
        vbox = Logs(self.virtualizador)
        # TratamentoErrosEnvelhecimentoLogs(pasta_logs=vbox.vboxMonitoringFolder, barras=True, ponto=True)

        # PlottarFragmentado().analisar(arquivo=vbox.vboxLogs['fragmentation'])
        # plot_fragmentation(vbox.vboxMonitoringFolder)
        
        PlottarGraficos().plottar(
            title="CPU - Sum All Cores", 
            nomeArquivo=vbox.vboxLogs['cpu_sum_all_cores'], 
            cols_to_divide=[
                '%usr', '%nice', '%sys', '%iowait', '%soft',
            ],
            ylabel={
                **self._common_cpu_labels()
            },
            dayfirst=True
        )
        
        PlottarGraficos().plottar(
            nomeArquivo=vbox.vboxLogs['monitoring_cpu'], 
            title="CPU",
            ylabel='(percentage)', 
            dayfirst=True, includeColYlabel=True
        )

        PlottarGraficos().plottar(
            title="Disk", 
            nomeArquivo=vbox.vboxLogs['monitoring_disks'], 
            ylabel='Disk Usage (GB)', 
            dayfirst=True, division=(1024**2)
        )

        PlottarGraficos().plottar(
            title="Zombie", 
            nomeArquivo=vbox.vboxLogs['monitoring_zumbies'], 
            ylabel='Zombie Processes (QTT)', 
            dayfirst=True
        )

        PlottarGraficos().plottar(
            title="Memory", 
            nomeArquivo=vbox.vboxLogs['monitoring_mem'], 
            ylabel='(MB)', 
            dayfirst=True, 
            division=1024, includeColYlabel=True
        )

        PlottarGraficos().plottar(
            title="Process - VBoxHeadless", 
            nomeArquivo=vbox.vboxLogs['monitoring_VboxHeadless'], 
            cols_to_divide=["vmrss","vsz", "swap"],
            ylabel={
                **self._common_ylabels()
            },
            division=1024, dayfirst=True
        )

        PlottarGraficos().plottar(
            title="Process - VBoxSVC", 
            nomeArquivo=vbox.vboxLogs['monitoring_VboxSvc'], 
            cols_to_divide=["vmrss","vsz","swap"],
            ylabel={
                **self._common_ylabels()
            },
            division=1024, dayfirst=True
        )

        PlottarGraficos().plottar(
            title="Process - VBoxXPCOMIPCD", 
            nomeArquivo=vbox.vboxLogs['monitoring_VboxXPCOMIPCD'], 
            cols_to_divide=["vmrss", "vsz", "swap"],
            ylabel={
                **self._common_ylabels()
            },
            division=1024, dayfirst=True
        )

        PlottarGraficos().plottar(
            title="Nginx Response Time", 
            nomeArquivo=vbox.vboxLogs['server_response_time_monitoring'], 
            ylabel='Response Time (seconds)', 
            multiply=1, dayfirst=True
        )
        
        
    def lxd_plottar(self):   
        lxd = Logs(self.virtualizador)
        # fragmentacao(MINIMUM_PROCESS_OCCURRENCES)
        # PlottarGraficos().plottar_fragmentation(PASTA_LOGS)
        # PlottarFragmentado().analisar(arquivo=lxd.lxdLogs['fragmentation'])
        plot_fragmentation(lxd.lxdMonitoringFolder)
        
        PlottarGraficos().plottar(
            title="CPU - Sum All Cores", 
            nomeArquivo=lxd.lxdLogs['cpu_sum_all_cores'], 
            cols_to_divide=[
                '%usr', '%nice', '%sys', '%iowait', '%soft',
            ],
            ylabel={
                **self._common_cpu_labels()
            },
            dayfirst=True
        )
        
        PlottarGraficos().plottar(
        title="CPU",
        nomeArquivo=lxd.lxdLogs['monitoring_cpu'], 
        ylabel='(percentage)', 
        dayfirst=True, includeColYlabel=True
        )

        PlottarGraficos().plottar(
            title="Disk", 
            nomeArquivo=lxd.lxdLogs['monitoring_disks'], 
            ylabel='Disk Usage (GB)', 
            dayfirst=True, division=(1024**2)
        )

        PlottarGraficos().plottar(
            title="Zombie", 
            nomeArquivo=lxd.lxdLogs['monitoring_zumbies'], 
            ylabel='Zombie Processes (QTT)', 
            dayfirst=True
        )

        PlottarGraficos().plottar(
            title="Memory", 
            nomeArquivo=lxd.lxdLogs['monitoring_mem'], 
            ylabel='(MB)', 
            dayfirst=True, 
            division=1000,
            includeColYlabel=True
        )
        
        PlottarGraficos().plottar(
            title="Process - lxdHeadless", 
            nomeArquivo=lxd.lxdLogs['lxd_Headless'], 
            cols_to_divide=["vmrss","vsz","swap"],
            ylabel={
                **self._common_ylabels()
            },
            division=1024, dayfirst=True
        )

        PlottarGraficos().plottar(
            title="Process - lxd_libvirt_service", 
            nomeArquivo=lxd.lxdLogs['lxd_libvirtd_service'], 
            cols_to_divide=["rss","vsz","swap"],
            ylabel={
                **self._common_ylabels()
            },
            division=1024, dayfirst=True
        )
    
        PlottarGraficos().plottar(
            title="Nginx Response Time", 
            nomeArquivo=lxd.lxdLogs['server_response_time_monitoring'], 
            ylabel='Response Time (seconds)', 
            multiply=1000, dayfirst=True
        )


    def xen_plottar(self):
        xen = Logs(self.virtualizador)
        # fragmentacao(MINIMUM_PROCESS_OCCURRENCES)
        # PlottarGraficos().plottar_fragmentation(PASTA_LOGS)
        # plot_fragmentation(xen.xenMonitoringFolder)
        
        PlottarGraficos().plottar(
            title="CPU - Sum All Cores", 
            nomeArquivo=xen.xenLogs['cpu_sum_all_cores'], 
            cols_to_divide=[
                '%usr', '%nice', '%sys', '%iowait', '%soft',
            ],
            ylabel={
                **self._common_cpu_labels()
            },
            dayfirst=True
        )
        
        PlottarGraficos().plottar(
            title="CPU",
            nomeArquivo=xen.xenLogs['monitoring_cpu'], 
            ylabel='(percentage)', 
            dayfirst=True, includeColYlabel=True
        )

        PlottarGraficos().plottar(
            title="Disk", 
            nomeArquivo=xen.xenLogs['monitoring_disks'], 
            ylabel='Disk Usage (GB)', 
            dayfirst=True, division=(1024**2)
        )

        PlottarGraficos().plottar(
            title="Zombie", 
            nomeArquivo=xen.xenLogs['monitoring_zumbies'], 
            ylabel='Zombie Processes (QTT)', 
            dayfirst=True
        )

        PlottarGraficos().plottar(
            title="Memory", 
            nomeArquivo=xen.xenLogs['monitoring_mem'], 
            ylabel='(MB)', 
            dayfirst=True, 
            division=1024, includeColYlabel=True
        )

        
        PlottarGraficos().plottar(
            title="Process - xen_monitoring_oxenstored", 
            nomeArquivo=xen.xenLogs['xen_monitoring_oxenstored'], 
            cols_to_divide=["vmrss","vsz","swap"],
            ylabel={
                **self._common_ylabels()
            },
            division=1024, dayfirst=True
        )

        PlottarGraficos().plottar(
            title="Process - xen_monitoring_xen_balloon", 
            nomeArquivo=xen.xenLogs['xen_monitoring_xen_balloon'], 
            cols_to_divide=["vmrss","vsz","swap"],
            ylabel={
                **self._common_ylabels()
            },
            division=1024, dayfirst=True
        )
        
        PlottarGraficos().plottar(
            title="Process - xen_monitoring_xenbus", 
            nomeArquivo=xen.xenLogs['xen_monitoring_xenbus'], 
            cols_to_divide=["vmrss","vsz","swap"],
            ylabel={
                **self._common_ylabels()
            },
            division=1024, dayfirst=True
        )

        PlottarGraficos().plottar(
            title="Process - xen_monitoring_xenconsoled", 
            nomeArquivo=xen.xenLogs['xen_monitoring_xenconsoled'], 
            cols_to_divide=["vmrss","vsz","swap"],
            ylabel={
                **self._common_ylabels()
            },
            division=1024, dayfirst=True
        )

        PlottarGraficos().plottar(
            title="Nginx Response Time", 
            nomeArquivo=xen.xenLogs['server_response_time_monitoring'], 
            ylabel='Response Time (seconds)', 
            multiply=1, dayfirst=True
        )


    def lxd_plottar(self):
        lxd = Logs(self.virtualizador)
        # fragmentacao(MINIMUM_PROCESS_OCCURRENCES)
        # PlottarGraficos().plottar_fragmentation(PASTA_LOGS)
        # PlottarFragmentado().analisar(arquivo=lxd.lxdLogs['fragmentation'])
        # plot_fragmentation(lxd.lxdMonitoringFolder)
        
        PlottarGraficos().plottar(
            title="CPU - Sum All Cores", 
            nomeArquivo=lxd.lxdLogs['cpu_sum_all_cores'], 
            cols_to_divide=[
                '%usr', '%nice', '%sys', '%iowait', '%soft',
            ],
            ylabel={
                **self._common_cpu_labels()
            },
            dayfirst=True
        )
        
        PlottarGraficos().plottar(
        title="CPU",
        nomeArquivo=lxd.lxdLogs['monitoring_cpu'], 
        ylabel='(percentage)', 
        dayfirst=True, includeColYlabel=True
        )

        PlottarGraficos().plottar(
            title="Disk", 
            nomeArquivo=lxd.lxdLogs['monitoring_disks'], 
            ylabel='Disk Usage (GB)', 
            dayfirst=True, division=(1024**2)
        )

        PlottarGraficos().plottar(
            title="Zombie", 
            nomeArquivo=lxd.lxdLogs['monitoring_zumbies'], 
            ylabel='Zombie Processes (QTT)', 
            dayfirst=True
        )

        PlottarGraficos().plottar(
            title="Memory", 
            nomeArquivo=lxd.lxdLogs['monitoring_mem'], 
            ylabel='(MB)', 
            dayfirst=True, 
            division=1000,
            includeColYlabel=True
        )
        
        PlottarGraficos().plottar(
            title="Process - lxd_vm_qemu_process", 
            nomeArquivo=lxd.lxdLogs['lxd_vm_qemu_process'], 
            cols_to_divide=["vmrss","vsz","swap"],
            ylabel={
                **self._common_ylabels()
            },
            division=1024, dayfirst=True
        )

        PlottarGraficos().plottar(
            title="Process - lxd_group_process_monitoring", 
            nomeArquivo=lxd.lxdLogs['lxd_group_process_monitoring'], 
            cols_to_divide=["rss","vsz","swap"],
            ylabel={
                **self._common_ylabels()
            },
            division=1024, dayfirst=True
        )
    
        PlottarGraficos().plottar(
            title="Nginx Response Time", 
            nomeArquivo=lxd.lxdLogs['server_response_time_monitoring'], 
            ylabel='Response Time (seconds)', 
            multiply=1000, dayfirst=True
        )


    # ------------------------------------------------ CONTAINERS ------------------------------------------- #
    def docker_antigo(self):
        dock_antigo = Logs()
        # fragmentacao(MINIMUM_PROCESS_OCCURRENCES)
        # PlottarGraficos().plottar_fragmentation(PASTA_LOGS)
        
        # sys.exit(0)    
        # PlottarGraficos().plottar(
        #     title="runs",
        #     filename=dock_novo['runs'], 
        #     ylabel='(percentage)', 
        #     dayfirst=True, includeColYlabel=True
        # )
        
        # --------------------- MACHINE RESOURCES
        PlottarGraficos().plottar(
            title="CPU",
            filename=dock_antigo['cpu'], 
            ylabel='(percentage)', 
            dayfirst=True, includeColYlabel=True
        )

        PlottarGraficos().plottar(
            title="Memory", 
            filename=dock_antigo['memory'], 
            ylabel='(MB)', 
            dayfirst=True, 
            division=1024, includeColYlabel=True
        )
        
        PlottarGraficos().plottar(
            title="Disk", 
            filename=dock_antigo['disk'], 
            ylabel='Disk usage (GB)', 
            dayfirst=True, division=(1024**2)
        )

        PlottarGraficos().plottar(
            title="Zumbis", 
            filename=dock_antigo['process'], 
            ylabel='Zumbis processes(qtt)', 
            dayfirst=True
        )

        # -------------------------- CONTAINER PROCESS
        PlottarGraficos().plottar(
            title="nginx",
            filename=dock_antigo['nginx'], 
            ylabel='(seconds)', 
            dayfirst=True, includeColYlabel=True,
            division=1e+9
        )
        
        # PlottarGraficos().plottar(
        #     title="postgres",
        #     filename=dock_antigo['postgres'], 
        #     ylabel='(seconds)', 
        #     dayfirst=True, includeColYlabel=True,
        #     division=1e+9
        # )
        
        PlottarGraficos().plottar(
            title="rabbitmq",
            filename=dock_antigo['rabbitmq'], 
            ylabel='(seconds)', 
            dayfirst=True, includeColYlabel=True,
            division=1e+9
        )
        
        PlottarGraficos().plottar(
            title="redis",
            filename=dock_antigo['redis'], 
            ylabel='(seconds)', 
            dayfirst=True, includeColYlabel=True,
            division=1e+9
        )
        
        # ----------------------------- DOCKER PROCESS
        PlottarGraficos().plottar(
            title="docker_antigo - process",
            filename=dock_antigo['docker'], 
            ylabel={
                'cpu': 'CPU usage (percentage)',
                'mem': 'Memory usage (percentage)',
                'rss': 'Physical memory usage(MB)',
                'vsz': 'Virtual memory usage (MB)',
                'threads': 'Number of threads(qtt)',
                'swap': 'Swap used(MB)',
            },
            dayfirst=True, includeColYlabel=True,
            cols_to_divide=['rss', 'vsz', 'swap'],
            division=1024
        )
        
        PlottarGraficos().plottar(
            title="dockerd_antigo - process",
            filename=dock_antigo['dockerd'], 
            ylabel={
                'cpu': 'CPU usage (percentage)',
                'mem': 'Memory usage (percentage)',
                'rss': 'Physical memory usage(MB)',
                'vsz': 'Virtual memory usage (MB)',
                'threads': 'Number of threads(qtt)',
                'swap': 'Swap used(MB)',
            },
            dayfirst=True, includeColYlabel=True,
            cols_to_divide=['rss', 'vsz', 'swap'],
            division=1024
        )
        
        PlottarGraficos().plottar(
            title="containerd_antigo - process",
            filename=dock_antigo['containerd'], 
            ylabel={
                'cpu': 'CPU usage (percentage)',
                'mem': 'Memory usage (percentage)',
                'rss': 'Physical memory usage(MB)',
                'vsz': 'Virtual memory usage (MB)',
                'threads': 'Number of threads(qtt)',
                'swap': 'Swap used(MB)',
            },
            dayfirst=True, includeColYlabel=True,
            cols_to_divide=['rss', 'vsz', 'swap'],
            division=1024
        )
        
        PlottarGraficos().plottar(
            title="containerd-shim_antigo - process",
            filename=dock_antigo['containerd-shim'], 
            ylabel={
                'cpu': 'CPU usage (percentage)',
                'mem': 'Memory usage (percentage)',
                'rss': 'Physical memory usage(MB)',
                'vsz': 'Virtual memory usage (MB)',
                'threads': 'Number of threads(qtt)',
                'swap': 'Swap used(MB)',
            },
            dayfirst=True, includeColYlabel=True,
            cols_to_divide=['rss', 'vsz', 'swap'],
            division=1024
        )
        
        PlottarGraficos().plottar(
            title="docker-proxy_antigo - process",
            filename=dock_antigo['docker-proxy'], 
            ylabel={
                'cpu': 'CPU usage (percentage)',
                'mem': 'Memory usage (percentage)',
                'rss': 'Physical memory usage(MB)',
                'vsz': 'Virtual memory usage (MB)',
                'threads': 'Number of threads(qtt)',
                'swap': 'Swap used(MB)',
            },
            dayfirst=True, includeColYlabel=True,
            cols_to_divide=['rss', 'vsz', 'swap'],
            division=1024
        )
        
        PlottarGraficos().plottar(
            title="runc_novo - process",
            filename=dock_antigo['runc'], 
            ylabel={
                'cpu': 'CPU usage (percentage)',
                'mem': 'Memory usage (percentage)',
                'rss': 'Physical memory usage(MB)',
                'vsz': 'Virtual memory usage (MB)',
                'threads': 'Number of threads(qtt)',
                'swap': 'Swap used(MB)',
            },
            dayfirst=True, includeColYlabel=True,
            cols_to_divide=['rss', 'vsz', 'swap'],
            division=1024
        )
        
        # -------------------------- IMAGE PROCESS
        PlottarGraficos().plottar(
            title="java",
            filename=dock_antigo['java'], 
            ylabel={
                'cpu': 'CPU usage (percentage)',
                'mem': 'Memory usage (percentage)',
                'rss': 'Physical memory usage(MB)',
                'vsz': 'Virtual memory usage (MB)',
                'threads': 'Number of threads(qtt)',
                'swap': 'Swap used(MB)',
            },
            dayfirst=True, includeColYlabel=True,
            cols_to_divide=['rss', 'vsz', 'swap'],
            division=1024
        )
        
        # PlottarGraficos().plottar(
        #     title="postgres_process",
        #     filename=dock_antigo['postgres_process'], 
        #     ylabel=labels(L_name=GRAPH_NAMES['postgres_process'], metrics='MB'),
        #     dayfirst=True, includeColYlabel=True,
        #     cols_to_divide=['rss', 'vsz', 'swap'],
        #     division=1024
        # )
        
        PlottarGraficos().plottar(
            title="beam.smp",
            filename=dock_antigo['beam.smp'], 
            ylabel={
                'cpu': 'CPU usage (percentage)',
                'mem': 'Memory usage (percentage)',
                'rss': 'Physical memory usage(MB)',
                'vsz': 'Virtual memory usage (MB)',
                'threads': 'Number of threads(qtt)',
                'swap': 'Swap used(MB)',
            },
            dayfirst=True, includeColYlabel=True,
            cols_to_divide=['rss', 'vsz', 'swap'],
            division=1024
        )
        
        PlottarGraficos().plottar(
            title="mysqld",
            filename=dock_antigo['mysqld'], 
            ylabel={
                'cpu': 'CPU usage (percentage)',
                'mem': 'Memory usage (percentage)',
                'rss': 'Physical memory usage(MB)',
                'vsz': 'Virtual memory usage (MB)',
                'threads': 'Number of threads(qtt)',
                'swap': 'Swap used(MB)',
            },
            dayfirst=True, includeColYlabel=True,
            cols_to_divide=['rss', 'vsz', 'swap'],
            division=1024
        )
        
        # PlottarGraficos().plottar(
        #     title="initdb",
        #     filename=dock_antigo['initdb'], 
        #     ylabel=labels(L_name=GRAPH_NAMES['initdb'], metrics='MB'),
        #     dayfirst=True, includeColYlabel=True,
        #     cols_to_divide=['rss', 'vsz', 'swap'],
        #     division=1024
        # )


    def docker_novo(self):
        dock_novo = Logs()
        # fragmentacao(MINIMUM_PROCESS_OCCURRENCES)
        # PlottarGraficos().plottar_fragmentation(PASTA_LOGS)
        
        # sys.exit(0)
        
        # PlottarGraficos().plottar(
        #     title="runs",
        #     filename=dock_novo['runs'], 
        #     ylabel='(percentage)', 
        #     dayfirst=True, includeColYlabel=True
        # )
        
        # --------------------- MACHINE RESOURCES
        PlottarGraficos().plottar(
            title="CPU",
            filename=dock_novo['cpu'], 
            ylabel='(percentage)', 
            dayfirst=True, includeColYlabel=True
        )

        PlottarGraficos().plottar(
            title="Memory", 
            filename=dock_novo['memory'], 
            ylabel='(MB)', 
            dayfirst=True, 
            division=1024, includeColYlabel=True
        )
        
        PlottarGraficos().plottar(
            title="Disk", 
            filename=dock_novo['disk'], 
            ylabel='Disk usage (GB)', 
            dayfirst=True, division=(1024**2)
        )

        PlottarGraficos().plottar(
            title="Zumbis", 
            filename=dock_novo['process'], 
            ylabel='Zumbis processes(qtt)', 
            dayfirst=True
        )

        # -------------------------- CONTAINER PROCESS
        PlottarGraficos().plottar(
            title="nginx",
            filename=dock_novo['nginx'], 
            ylabel='(seconds)', 
            dayfirst=True, includeColYlabel=True,
            division=1e+9
        )
        
        # PlottarGraficos().plottar(
        #     title="postgres",
        #     filename=dock_novo['postgres'], 
        #     ylabel='(seconds)', 
        #     dayfirst=True, includeColYlabel=True,
        #     division=1e+9
        # )
        
        PlottarGraficos().plottar(
            title="rabbitmq",
            filename=dock_novo['rabbitmq'], 
            ylabel='(seconds)', 
            dayfirst=True, includeColYlabel=True,
            division=1e+9
        )
        
        PlottarGraficos().plottar(
            title="redis",
            filename=dock_novo['redis'], 
            ylabel='(seconds)', 
            dayfirst=True, includeColYlabel=True,
            division=1e+9
        )
        
        # ----------------------------- DOCKER PROCESS
        PlottarGraficos().plottar(
            title="docker_novo - process",
            filename=dock_novo['docker'], 
            ylabel={
                'cpu': 'CPU usage (percentage)',
                'mem': 'Memory usage (percentage)',
                'rss': 'Physical memory usage(MB)',
                'vsz': 'Virtual memory usage (MB)',
                'threads': 'Number of threads(qtt)',
                'swap': 'Swap used(MB)',
            },
            dayfirst=True, includeColYlabel=True,
            cols_to_divide=['rss', 'vsz', 'swap'],
            division=1024
        )
        
        PlottarGraficos().plottar(
            title="dockerd_novo - process",
            filename=dock_novo['dockerd'], 
            ylabel={
                'cpu': 'CPU usage (percentage)',
                'mem': 'Memory usage (percentage)',
                'rss': 'Physical memory usage(MB)',
                'vsz': 'Virtual memory usage (MB)',
                'threads': 'Number of threads(qtt)',
                'swap': 'Swap used(MB)',
            },
            dayfirst=True, includeColYlabel=True,
            cols_to_divide=['rss', 'vsz', 'swap'],
            division=1024
        )
        
        PlottarGraficos().plottar(
            title="containerd_novo - process",
            filename=dock_novo['containerd'], 
            ylabel={
                'cpu': 'CPU usage (percentage)',
                'mem': 'Memory usage (percentage)',
                'rss': 'Physical memory usage(MB)',
                'vsz': 'Virtual memory usage (MB)',
                'threads': 'Number of threads(qtt)',
                'swap': 'Swap used(MB)',
            },
            dayfirst=True, includeColYlabel=True,
            cols_to_divide=['rss', 'vsz', 'swap'],
            division=1024
        )
        
        PlottarGraficos().plottar(
            title="containerd-shim_novo - process",
            filename=dock_novo['containerd-shim'], 
            ylabel={
                'cpu': 'CPU usage (percentage)',
                'mem': 'Memory usage (percentage)',
                'rss': 'Physical memory usage(MB)',
                'vsz': 'Virtual memory usage (MB)',
                'threads': 'Number of threads(qtt)',
                'swap': 'Swap used(MB)',
            },
            dayfirst=True, includeColYlabel=True,
            cols_to_divide=['rss', 'vsz', 'swap'],
            division=1024
        )
        
        PlottarGraficos().plottar(
            title="docker-proxy_novo - process",
            filename=dock_novo['docker-proxy'], 
            ylabel={
                'cpu': 'CPU usage (percentage)',
                'mem': 'Memory usage (percentage)',
                'rss': 'Physical memory usage(MB)',
                'vsz': 'Virtual memory usage (MB)',
                'threads': 'Number of threads(qtt)',
                'swap': 'Swap used(MB)',
            },
            dayfirst=True, includeColYlabel=True,
            cols_to_divide=['rss', 'vsz', 'swap'],
            division=1024
        )
        
        PlottarGraficos().plottar(
            title="runc_novo - process",
            filename=dock_novo['runc'], 
            ylabel={
                'cpu': 'CPU usage (percentage)',
                'mem': 'Memory usage (percentage)',
                'rss': 'Physical memory usage(MB)',
                'vsz': 'Virtual memory usage (MB)',
                'threads': 'Number of threads(qtt)',
                'swap': 'Swap used(MB)',
            },
            dayfirst=True, includeColYlabel=True,
            cols_to_divide=['rss', 'vsz', 'swap'],
            division=1024
        )
        
        # -------------------------- IMAGE PROCESS
        PlottarGraficos().plottar(
            title="java",
            filename=dock_novo['java'], 
            ylabel={
                'cpu': 'CPU usage (percentage)',
                'mem': 'Memory usage (percentage)',
                'rss': 'Physical memory usage(MB)',
                'vsz': 'Virtual memory usage (MB)',
                'threads': 'Number of threads(qtt)',
                'swap': 'Swap used(MB)',
            },
            dayfirst=True, includeColYlabel=True,
            cols_to_divide=['rss', 'vsz', 'swap'],
            division=1024
        )
        
        # PlottarGraficos().plottar(
        #     title="postgres_process",
        #     filename=dock_novo['postgres_process'], 
        #     ylabel=labels(L_name=GRAPH_NAMES['postgres_process'], metrics='MB'),
        #     dayfirst=True, includeColYlabel=True,
        #     cols_to_divide=['rss', 'vsz', 'swap'],
        #     division=1024
        # )
        
        PlottarGraficos().plottar(
            title="beam.smp",
            filename=dock_novo['beam.smp'], 
            ylabel={
                'cpu': 'CPU usage (percentage)',
                'mem': 'Memory usage (percentage)',
                'rss': 'Physical memory usage(MB)',
                'vsz': 'Virtual memory usage (MB)',
                'threads': 'Number of threads(qtt)',
                'swap': 'Swap used(MB)',
            },
            dayfirst=True, includeColYlabel=True,
            cols_to_divide=['rss', 'vsz', 'swap'],
            division=1024
        )
        
        PlottarGraficos().plottar(
            title="mysqld",
            filename=dock_novo['mysqld'], 
            ylabel={
                'cpu': 'CPU usage (percentage)',
                'mem': 'Memory usage (percentage)',
                'rss': 'Physical memory usage(MB)',
                'vsz': 'Virtual memory usage (MB)',
                'threads': 'Number of threads(qtt)',
                'swap': 'Swap used(MB)',
            },
            dayfirst=True, includeColYlabel=True,
            cols_to_divide=['rss', 'vsz', 'swap'],
            division=1024
        )
        
        # PlottarGraficos().plottar(
        #     title="initdb",
        #     filename=dock_novo['initdb'], 
        #     ylabel=labels(L_name=GRAPH_NAMES['initdb'], metrics='MB'),
        #     dayfirst=True, includeColYlabel=True,
        #     cols_to_divide=['rss', 'vsz', 'swap'],
        #     division=1024
        # )


    def podman(self):
        pod = Logs()
        # fragmentacao(MINIMUM_PROCESS_OCCURRENCES)
        # PlottarGraficos().plottar_fragmentation(PASTA_LOGS)
        
        # sys.exit(0)
        
        # PlottarGraficos().plottar(
        #     title="runs",
        #     filename=pod['runs'], 
        #     ylabel='(percentage)', 
        #     dayfirst=True, includeColYlabel=True
        # )
        
        # --------------------- MACHINE RESOURCES
        PlottarGraficos().plottar(
            title="CPU",
            filename=pod['cpu'], 
            ylabel='(percentage)', 
            dayfirst=True, includeColYlabel=True
        )

        PlottarGraficos().plottar(
            title="Memory", 
            filename=pod['memory'], 
            ylabel='(GB)',
            dayfirst=True, 
            division=(1024**2), includeColYlabel=True
        )
        
        PlottarGraficos().plottar(
            title="Disk", 
            filename=pod['disk'], 
            ylabel='Disk usage (GB)', 
            dayfirst=True, division=(1024**2)
        )
        
        PlottarGraficos().plottar(
            title="Zumbis", 
            filename=pod['process'], 
            ylabel='Zumbis processes(qtt)', 
            dayfirst=True
        )
        
        # -------------------------- CONTAINER PROCESS
        PlottarGraficos().plottar(
            title="nginx",
            filename=pod['nginx'], 
            ylabel='(seconds)', 
            dayfirst=True, includeColYlabel=True,
            division=1e+9
        )
        
        # PlottarGraficos().plottar(
        #     title="postgres",
        #     filename=pod['postgres'], 
        #     ylabel='(seconds)', 
        #     dayfirst=True, includeColYlabel=True,
        #     division=1e+9
        # )
        
        PlottarGraficos().plottar(
            title="rabbitmq",
            filename=pod['rabbitmq'], 
            ylabel='(seconds)', 
            dayfirst=True, includeColYlabel=True,
            division=1e+9
        )
        
        PlottarGraficos().plottar(
            title="redis",
            filename=pod['redis'], 
            ylabel='(seconds)', 
            dayfirst=True, includeColYlabel=True,
            division=1e+9
        )
        
        # ----------------------------- PODMAN PROCESS
        PlottarGraficos().plottar(
            title="podman",
            filename=pod['podman'], 
            ylabel={
                'cpu': 'CPU usage (percentage)',
                'mem': 'Memory usage (percentage)',
                'rss': 'Physical memory usage(MB)',
                'vsz': 'Virtual memory usage (MB)',
                'threads': 'Number of threads(qtt)',
                'swap': 'Swap used(MB)',
            },
            dayfirst=True, includeColYlabel=True,
            cols_to_divide=['rss', 'vsz', 'swap'],
            division=1024
        )
        
        PlottarGraficos().plottar(
            title="conmon",
            filename=pod['conmon'], 
            ylabel={
                'cpu': 'CPU usage (percentage)',
                'mem': 'Memory usage (percentage)',
                'rss': 'Physical memory usage(MB)',
                'vsz': 'Virtual memory usage (MB)',
                'threads': 'Number of threads(qtt)',
                'swap': 'Swap used(MB)',
            },
            dayfirst=True, includeColYlabel=True,
            cols_to_divide=['rss', 'vsz', 'swap'],
            division=1024
        )
        
        # PlottarGraficos().plottar(
        #     title="cron",
        #     filename=pod['cron'], 
        #     ylabel=labels(L_name=GRAPH_NAMES['cron'], metrics='MB'),
        #     dayfirst=True, includeColYlabel=True,
        #     cols_to_divide=['rss', 'vsz', 'swap'],
        #     division=1024
        # )
        
        PlottarGraficos().plottar(
            title="crun",
            filename=pod['crun'], 
            ylabel={
                'cpu': 'CPU usage (percentage)',
                'mem': 'Memory usage (percentage)',
                'rss': 'Physical memory usage(MB)',
                'vsz': 'Virtual memory usage (MB)',
                'threads': 'Number of threads(qtt)',
                'swap': 'Swap used(MB)',
            },
            dayfirst=True, includeColYlabel=True,
            cols_to_divide=['rss', 'vsz', 'swap'],
            division=1024
        )
        
        PlottarGraficos().plottar(
            title="systemd",
            filename=pod['systemd'], 
            ylabel={
                'cpu': 'CPU usage (percentage)',
                'mem': 'Memory usage (percentage)',
                'rss': 'Physical memory usage(MB)',
                'vsz': 'Virtual memory usage (MB)',
                'threads': 'Number of threads(qtt)',
                'swap': 'Swap used(MB)',
            },
            dayfirst=True, includeColYlabel=True,
            cols_to_divide=['rss', 'vsz', 'swap'],
            division=1024
        )
        
        # -------------------------- IMAGE PROCESS
        PlottarGraficos().plottar(
            title="java",
            filename=pod['java'], 
            ylabel={
                'cpu': 'CPU usage (percentage)',
                'mem': 'Memory usage (percentage)',
                'rss': 'Physical memory usage(MB)',
                'vsz': 'Virtual memory usage (MB)',
                'threads': 'Number of threads(qtt)',
                'swap': 'Swap used(MB)',
            },
            dayfirst=True, includeColYlabel=True,
            cols_to_divide=['rss', 'vsz', 'swap'],
            division=1024
        )
        
        # PlottarGraficos().plottar(
        #     title="postgres_process",
        #     filename=pod['postgres_process'], 
        #     ylabel=labels(L_name=GRAPH_NAMES['postgres_process'], metrics='MB'),
        #     dayfirst=True, includeColYlabel=True,
        #     cols_to_divide=['rss', 'vsz', 'swap'],
        #     division=1024
        # )
        
        PlottarGraficos().plottar(
            title="beam.smp",
            filename=pod['beam.smp'], 
            ylabel={
                'cpu': 'CPU usage (percentage)',
                'mem': 'Memory usage (percentage)',
                'rss': 'Physical memory usage(MB)',
                'vsz': 'Virtual memory usage (MB)',
                'threads': 'Number of threads(qtt)',
                'swap': 'Swap used(MB)',
            },
            dayfirst=True, includeColYlabel=True,
            cols_to_divide=['rss', 'vsz', 'swap'],
            division=1024
        )
        
        PlottarGraficos().plottar(
            title="mysqld",
            filename=pod['mysqld'], 
            ylabel={
                'cpu': 'CPU usage (percentage)',
                'mem': 'Memory usage (percentage)',
                'rss': 'Physical memory usage(MB)',
                'vsz': 'Virtual memory usage (MB)',
                'threads': 'Number of threads(qtt)',
                'swap': 'Swap used(MB)',
            },
            dayfirst=True, includeColYlabel=True,
            cols_to_divide=['rss', 'vsz', 'swap'],
            division=1024
        )
        
        # PlottarGraficos().plottar(
        #     title="initdb",
        #     filename=pod['initdb'], 
        #     ylabel=labels(L_name=GRAPH_NAMES['initdb'], metrics='MB'),
        #     dayfirst=True, includeColYlabel=True,
        #     cols_to_divide=['rss', 'vsz', 'swap'],
        #     division=1024
        # )