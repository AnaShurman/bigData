# Criar o banco de dados:

import sqlite3 as conector

conexao = None
cursor = None
try:
    conexao = conector.connect("meu_banco")
except conector.DatabaseError as erro:
    print("Erro de Banco de Dados", erro)

finally:
    # Fechamento das conexoes e cursores
    if cursor:
        cursor.close()
    if conexao:
        conexao.close()
