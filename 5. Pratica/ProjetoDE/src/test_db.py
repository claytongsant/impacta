import sqlite3
import pandas as pd
from pathlib import Path

# Caminho para o banco
db_path = Path(__file__).resolve().parent.parent / "assets" / "database.db"

def check_data():
    conn = sqlite3.connect(db_path)
    # Lista as tabelas existentes
    tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table';", conn)
    print("Tabelas no banco:", tables.values)
    
    # Lê os primeiros 5 registros da tabela que criamos
    df = pd.read_sql("SELECT * FROM tb_clientes LIMIT 5", conn)
    print("\nPrimeiros 5 registros:")
    print(df)
    conn.close()

if __name__ == "__main__":
    check_data()