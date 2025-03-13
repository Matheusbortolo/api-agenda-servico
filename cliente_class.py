from pydantic import BaseModel
from typing import Optional

class Cliente(BaseModel):
    id: Optional[int] = None
    nome: str
    endereco: str
    telefone: str
    email: str



