import sqlite3
import pandas as pd
import numpy as np

def criar_db(df,nome_tabela,nome_db):
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
