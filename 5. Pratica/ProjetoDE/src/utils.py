import pandas as pd
import requests
import sqlite3
import logging
from pathlib import Path

# aqui está  o caminho da assets 
ASSETS_PATH = Path(__file__).resolve().parent.parent / "assets"

def ingestion(configs):
    """Busca dados da API"""
    url = "https://randomuser.me/api/?results=10"
    response = requests.get(url)
    if response.status_code == 200:
        # Aqui Normalizei o JSON para um DataFrame .
        return pd.json_normalize(response.json()['results'])
    else:
        raise Exception(f"Erro na API: {response.status_code}")

def preparation(df, configs):
    """Trata os dados e salva no SQLite"""
    try:
        logging.info("Iniciando tratamento de dados...")
        
        # Aqui está aSeleção e Renomeação 
        df_treated = df[[
            'name.first', 'name.last', 'email', 'location.city', 
            'dob.age', 'registered.date'
        ]].copy()
        
        df_treated.columns = ['nome', 'sobrenome', 'email', 'cidade', 'idade', 'data_registro']
        
        #  (Feature Engineering)
        df_treated['nome_completo'] = df_treated['nome'] + " " + df_treated['sobrenome']
        
        # Limpeza básica
        df_treated['email'] = df_treated['email'].str.lower()
        
        # Aqui vai para Salvar no banco SQLite dentro da pasta assets
        db_path = ASSETS_PATH / "database.db"
        conn = sqlite3.connect(db_path)
        df_treated.to_sql("tb_clientes_curados", conn, if_exists="replace", index=False)
        conn.close()
        
        logging.info("Dados curados salvos na tabela 'tb_clientes_curados'.")
        return True
    except Exception as e:
        logging.error(f"Erro na preparação: {e}")
        raise
    
'''import pandas as pd
import requests
import utils as utils

def ingestion(configs):
    """
    Função de ingestão dos dados.
    Consome dados da api: https://randomuser.me, 10 resultados por página pelo menos
    Outputs: Retorna dataframe
    """
    return True


def validation_inputs(df, configs):
    """
    Função de validação dos dados antes de salvar no banco de dados
    Output: Se não estiver no padrão correto interrompe o processo e salva alerta em 
    um arquivo de logs. Se estiver correto, salva log com mensagem: 'Dados corretos'
    """
    return True


def preparation(df, configs):
    """
    Função de preparação dos dados: 
        - Renomeia colunas
        - Ajusta tipo dos dados
        - Remove caracter especial
    Outputs: Salva dados tratados em base sqlite no diretorio assets
    """

    #data = validate_inputs(df)

    return True'''