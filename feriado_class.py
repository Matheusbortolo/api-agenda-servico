from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class Feriado(BaseModel):
    id: Optional[int] = None
    nome: str
    datahora_inicio: datetime
    datahora_fim: datetime
    flag_parar: bool

