import logging
from pathlib import Path


class CreateDirectory:
    def __init__(self, images_folder='imagens_plottadas', 
        logs_folder='logs_monitoramento_envelhecimento'
    ):
        if not Path(images_folder).exists():
            Path(images_folder).mkdir()
            logging.log(msg='Diretório 1 criado com sucesso.', level=3)
        else:
            logging.log(msg='verificação de diretorio 1 feita', level=3)
            
        if not Path(logs_folder).exists():
            Path(logs_folder).mkdir()
            logging.log(msg='Diretório 2 criado com sucesso.', level=3)
            
        else:
            logging.log(msg='verificação de diretorio 2 feita\n', level=3)
