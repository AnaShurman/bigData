# Big Data
import sqlite3
def criar_tabela():
    conn = sqlite3.connect("dados_clima.db")
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS covid_brasil (
        regiao TEXT,
        estado TEXT,
        municipio TEXT,
        coduf TEXT,
        codmun TEXT,
        codRegiaoSaude TEXT,
        nomeRegiaoSaude TEXT,
        data data,
        semanaEpi TEXT,
        populacaoTCU2019 TEXT,
        casosAcumulado TEXT,
        obitosAcumulado TEXT,
        Recuperadosnovos TEXT,
        emAcompanhamntoNovos TEXT,
        interior_metropolitana TEXT  
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS covid_estados (
        regiao TEXT,
        estado TEXT,
        municipio TEXT,
        coduf TEXT,
        codmun TEXT,
        codRegiaoSaude TEXT,
        nomeRegiaoSaude TEXT,
        data data,
        semanaEpi TEXT,
        populacaoTCU2019 TEXT,
        casosAcumulado TEXT,
        obitosAcumulado TEXT,
        Recuperadosnovos TEXT,
        emAcompanhamntoNovos TEXT,
        interior_metropolitana TEXT 
    )
    ''')
    

