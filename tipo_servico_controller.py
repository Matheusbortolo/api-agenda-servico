from typing import Optional
from tipo_servico_class import TipoServico
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

def get_tipo_servico(id: Optional[int] = None):
    where = []
    where.append(' 1=1')
    if id is not None: 
        where.append(f" id = {id}")

    query = "SELECT * FROM tipo_servico where"
    where_clause = " AND ".join(where)

    query += where_clause
    res = db.fetch_all(query)
    agendamento = [TipoServico(**ag) for ag in res]
    return agendamento


def set_tipo_servico(tipo_servico: TipoServico):
    insert_query = """
        INSERT INTO tipo_servico (nome, obs) 
        VALUES (%s, %s)
    """
    ret = db.execute_query(insert_query, (
        tipo_servico.nome, 
        tipo_servico.obs, 
    ))
    return ret
