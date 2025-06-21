from app.models import Cliente, ClienteCreate, ClienteUpdate
from app.database import clientes, contador_id

def crear_cliente(cliente: ClienteCreate) -> Cliente:
    global contador_id
    nuevo = Cliente(id=contador_id, **cliente.dict())
    clientes[contador_id] = nuevo
    contador_id += 1
    return nuevo

def listar_clientes() -> list[Cliente]:
    return list(clientes.values())

def obtener_cliente(cliente_id: int) -> Cliente:
    return clientes.get(cliente_id)

def actualizar_cliente(cliente_id: int, cliente_data: ClienteUpdate) -> Cliente:
    cliente = clientes.get(cliente_id)
    if cliente is None:
        return None
    actualizado = cliente.copy(update=cliente_data.dict(exclude_unset=True))
    clientes[cliente_id] = actualizado
    return actualizado

def eliminar_cliente(cliente_id: int) -> bool:
    return clientes.pop(cliente_id, None) is not None
