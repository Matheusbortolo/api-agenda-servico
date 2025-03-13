from typing import Optional
from feriado_class import Feriado
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

def get_feriado(id: Optional[int] = None):
    where = []
    where.append(' 1=1')
    if id is not None: 
        where.append(f" id = {id}")

    query = "SELECT * FROM feriados where"
    where_clause = " AND ".join(where)

    query += where_clause
    res = db.fetch_all(query)
    agendamento = [Feriado(**ag) for ag in res]
    return agendamento


def set_feriado(feriado: Feriado):
    insert_query = """
        INSERT INTO feriados (nome, datahora_inicio, datahora_fim, flag_parar) 
        VALUES ( %s, %s, %s, %s)
    """
    ret = db.execute_query(insert_query, (
        feriado.nome, 
        feriado.datahora_inicio, 
        feriado.datahora_fim, 
        feriado.flag_parar
    ))
    return ret
