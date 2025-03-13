from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from tipo_servico_class import TipoServico
from cliente_class import Cliente


class Agendamento(BaseModel):
    id: Optional[int] = None
    datahora_inicio: datetime   
    datahora_fim: datetime     
    tipo_servico: Optional[TipoServico] = None
    id_servico: int
    id_cliente: int
    cliente: Optional[Cliente] = None 
    obs: str
    endereco: str

