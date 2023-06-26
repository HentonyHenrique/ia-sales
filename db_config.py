import mysql.connector

# Função para obter a conexão com o banco de dados
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="",
        port=
    )
