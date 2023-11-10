Povoar as tabelas:

import sqlite3 as conector
from modelos import covid_brasil, covid_estados

conexao = None
cursor = None
try:
    conexao = conector.connect("meu_banco.db")
    conexao.execute("PRAGMA foreign_keys = on")
    cursor = conexao.cursor()

    with open("Covid_Brasil.csv") as covid_brasil:
        covid_brasil.readline() #descarta o cabeçalho
        for linha in covid_brasil:
            regiao, estado, municipio, coduf, codmun, codRegiaoSaude, nomeRegiaoSaude, data,
            semanaEpi, populacaoTCU2019, casosAcumulado, casosNovos, obitosAcumulado, obitosNovos,
            Recuperadosnovos, emAcompanhamentoNovos, interior_metropolitana = linha.strip().split(';')
            print(regiao, estado, municipio, coduf, codmun, codRegiaoSaude, nomeRegiaoSaude, data,
            semanaEpi, populacaoTCU2019, casosAcumulado, casosNovos, obitosAcumulado, obitosNovos,
            Recuperadosnovos, emAcompanhamentoNovos, interior_metropolitana)

            comando = '''INSERT INTO Municipio VALUES (:regiao, :estado, :municipio, :coduf, 
            :codmun, :codRegiaoSaude, :nomeRegiaoSaude, :data,
            :semanaEpi, :populacaoTCU2019, :casosAcumulado, :casosNovos, :obitosAcumulado, :obitosNovos,
            :Recuperadosnovos, :emAcompanhamentoNovos, :interior_metropolitana);''' #parametros nomeados
            cursor.execute(comando, vars(dengue))

    conexao.commit()

except conector.OperationalError as erro:
    print("Erro Operacional", erro)
except conector.IntegrityError as erro:
    print("Erro de integridade", erro)
