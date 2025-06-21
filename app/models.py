from pydantic import BaseModel
from typing import Optional

class ClienteBase(BaseModel):
    nombre: str
    correo: str

class ClienteCreate(ClienteBase):
    pass

class ClienteUpdate(BaseModel):
    nombre: Optional[str] = None
    correo: Optional[str] = None

class Cliente(ClienteBase):
    id: int
