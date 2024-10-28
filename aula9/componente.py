import sqlite3
import pandas as pd
import numpy as np

def criar_tabela(df,nome_tabela,nome_db):
    conn = sqlite3.connect(nome_db)
    df.to_sql(nome_tabela,conn,if_exists='replace',index=False)
    conn.close()
    return True

def consultar_db(nome_tabela,nome_db):
    conn = sqlite3.connect(nome_db)
    query = f'SELECT * FROM {nome_tabela}'
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def mostrar_tabela(nome_db):
    conn = sqlite3.connect(nome_db)
    query='SELECT name FROM sqlite_master WHERE type="table"'
    schema = pd.read_sql_query(query,conn)

    conn.close()
    return schema