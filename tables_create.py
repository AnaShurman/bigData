# Criar as tabelas:

import sqlite3

# Função para criar a tabela se ela não existir
def criar_tabela():
    conn = sqlite3.connect("meu_banco.db")
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
            data date,
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
            data date,
            semanaEpi TEXT,
            populacaoTCU2019 TEXT,
            casosAcumulado TEXT,
            obitosAcumulado TEXT,
            Recuperadosnovos TEXT,
            emAcompanhamntoNovos TEXT,
            interior_metropolitana TEXT  
        )
            ''')

         
        conn.commit()
        conn.close()

            
    
