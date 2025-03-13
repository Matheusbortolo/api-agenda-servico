from pydantic import BaseModel
from typing import Optional

class TipoServico(BaseModel):
    id: Optional[int] = None
    nome: str
    obs: str   

