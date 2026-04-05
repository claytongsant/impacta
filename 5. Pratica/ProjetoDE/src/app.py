import logging
import utils
from core import config  # refer-se ao  'config'

# Aqui eu fiz uma Configuração de logs para você acompanhar no terminal
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

if __name__ == '__main__':
    logging.info("Iniciando Pipeline da Prática 5...")
    
    try:
        # 1. Ingestão: Aqui eu Busco os dados na API
        df = utils.ingestion(config)
        logging.info(f"Sucesso: {len(df)} registros baixados da API.")
        
        # 2. neste ponto professora eu devo prepará  e gravar : e ainda Tratar os dados e CRIAr a tabela 'tb_clientes_curados'
        utils.preparation(df, config)
        logging.info("Sucesso: Dados curados e salvos em assets/database.db")
        
    except Exception as e:
        # MSG: Se der erro aqui, o Dashboard não vai funcionar!
        logging.error(f"Falha no pipeline: {e}")
'''import utils as utils
import logging
from core import configs

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    logging.info("Iniciando processo de ingestão")
    try:
        df = utils.ingestion(configs)
    except:
        logging.error("Erro de ingestão de dados")
    try:
        utils.preparation(df, configs)
        logging.info("Fim do processo de ingestão")
    except:
        logging.error("Erro de preparação")'''