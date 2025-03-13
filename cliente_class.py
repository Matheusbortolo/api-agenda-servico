from pydantic import BaseModel

class Cliente(BaseModel):
    id: int
    nome: str
    endereco: str
    telefone: str
    email: str



