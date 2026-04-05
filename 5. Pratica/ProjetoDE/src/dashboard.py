import streamlit as st
import pandas as pd
import sqlite3
from pathlib import Path

# Caminho para o banco (subindo um nível a partir da src)
DB_PATH = Path(__file__).resolve().parent.parent / "assets" / "database.db"

def load_data():
    conn = sqlite3.connect(DB_PATH)
    # Note que agora lemos a tabela 'curada' que o utils criou
    df = pd.read_sql("SELECT * FROM tb_clientes_curados", conn)
    conn.close()
    return df

st.title("📊 Painel de Controle de Clientes")

try:
    df = load_data()
    
    # Métricas rápidas
    m1, m2 = st.columns(2)
    m1.metric("Total de Usuários", len(df))
    m2.metric("Média de Idade", f"{df['idade'].mean():.1f} anos")
    
    # Exibição da tabela tratada
    st.dataframe(df)
    
    # Gráfico simples
    st.bar_chart(df['idade'])
    
except Exception as e:
    st.error(f"Aguardando dados... Rode o app.py primeiro! Erro: {e}")