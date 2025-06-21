from fastapi import FastAPI, HTTPException
from app.models import Cliente, ClienteCreate, ClienteUpdate
from app import crud

app = FastAPI()

@app.post("/clientes", response_model=Cliente)
def crear_cliente(cliente: ClienteCreate):
    return crud.crear_cliente(cliente)

@app.get("/clientes", response_model=list[Cliente])
def listar_clientes():
    return crud.listar_clientes()

@app.get("/clientes/{cliente_id}", response_model=Cliente)
def obtener_cliente(cliente_id: int):
    cliente = crud.obtener_cliente(cliente_id)
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente

@app.put("/clientes/{cliente_id}", response_model=Cliente)
def actualizar_cliente(cliente_id: int, cliente: ClienteUpdate):
    actualizado = crud.actualizar_cliente(cliente_id, cliente)
    if actualizado is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return actualizado

@app.delete("/clientes/{cliente_id}")
def eliminar_cliente(cliente_id: int):
    eliminado = crud.eliminar_cliente(cliente_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return {"mensaje": "Cliente eliminado"}
