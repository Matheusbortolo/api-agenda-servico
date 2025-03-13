from typing import Optional
from cliente_class import Cliente
from mysql_connection import MySQLConnection  # Importando a classe de conexão MySQL
from dotenv import load_dotenv
import os



load_dotenv()
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")


db = MySQLConnection(
    host=db_host, 
    user=db_user, 
    password=db_password, 
    database=db_name
)
db.connect()

def get_cliente(id: Optional[int] = None):
    if id is not None:
        query = "SELECT * FROM clientes where id = %s"
        res = db.fetch_one(query, (id,)) 
        if res is None:
            return {}
        return Cliente(**res)      

    if id is None:
        query = "SELECT * FROM clientes"
        res = db.fetch_all(query) 
        if res is None:
            return {}
        clientes = [Cliente(**cliente) for cliente in res]
        return clientes


def set_cliente(cliente: Cliente):
    insert_query = """
        INSERT INTO clientes (id, nome, endereco, telefone, email) 
        VALUES (%s, %s, %s, %s, %s)
    """
    ret = db.execute_query(insert_query, (
        cliente.id, 
        cliente.nome, 
        cliente.endereco, 
        cliente.telefone, 
        cliente.email
    ))
    return ret
