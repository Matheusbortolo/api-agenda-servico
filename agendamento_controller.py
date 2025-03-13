from typing import Optional
from agendamento_class import Agendamento
from mysql_connection import MySQLConnection  # Importando a classe de conexão MySQL
from dotenv import load_dotenv
import os
from datetime import date
from cliente_controller import get_cliente
from tipo_servico_controller import get_tipo_servico


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

def get_agendamento(id: Optional[int] = None, data: Optional[date] = None, data_fim: Optional[date] = None):
    agendamento = []
    where = []
    where.append(' 1=1')
    if data is not None:
        where.append(f" datahora_inicio>= '{data} 00:00:00'")
    if data_fim is not None:
        where.append(f" datahora_inicio<= '{data} 23:59:59'")
    if id is not None: 
        where.append(f" id = {id}")

    query = "SELECT * FROM agendamentos where"
    where_clause = " AND ".join(where)

    query += where_clause
    res = db.fetch_all(query)
    for ag in res:
        agenda = Agendamento(**ag)
        cliente = get_cliente(agenda.id_cliente)
        agenda.cliente = get_cliente(agenda.id_cliente)[0]
        agenda.tipo_servico = get_tipo_servico(agenda.id_servico)[0]
        agendamento.append(agenda)
    # agendamento = [Agendamento(**ag) for ag in res]
    return agendamento
    

def set_agendamento(agendamento: Agendamento):
    insert_query = """
        INSERT INTO agendamentos ( datahora_inicio, datahora_fim, id_servico, obs, id_cliente, endereco) 
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    print(insert_query)
    ret = db.execute_query(insert_query, (
        agendamento.datahora_inicio, 
        agendamento.datahora_fim, 
        agendamento.id_servico, 
        agendamento.obs,
        agendamento.id_servico,
        agendamento.endereco,
    ))
    return ret
