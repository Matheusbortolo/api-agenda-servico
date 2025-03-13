from fastapi import FastAPI, Request
from typing import Optional
from cliente_controller import get_cliente, set_cliente
from cliente_class import Cliente

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Olá, Mundo!"}

@app.get("/feriados/")
def read_feriado(id: Optional[int] = None):
    return {"message": "feriados!"}

@app.post("/feriados")
async def set_feriado(request: Request):
    body = await request.json()
    return {"message": "feriados!"}

@app.get("/clientes/")
def read_clientes(id: Optional[int] = None):    
    return {"message": get_cliente(id= id)}

@app.post("/clientes")
async def set_cliente(request: Request):
    body = await request.json()
    cliente = Cliente.parse_raw(body)
    return  {"message": set_cliente(cliente = cliente)}

@app.get("/tipo-servico/")
def read_tipo_servico(id: Optional[int] = None):
    return {"message": "tipo-servico!"}

@app.post("/tipo-servico")
async def set_tipo_servico(request: Request):
    body = await request.json()
    return {"message": "tipo-servico!"}

@app.get("/agenda/")
def read_agenda(id: Optional[int] = None): 
    return {"message": "agenda!"}

@app.post("/agenda")
async def set_agenda(request: Request):
    body = await request.json()
    return {"message": "agenda!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
