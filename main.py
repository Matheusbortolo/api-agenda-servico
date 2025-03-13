from fastapi import FastAPI, Request, Depends
from typing import Optional
from cliente_controller import get_cliente, set_cliente
from cliente_class import Cliente
from feriado_controller import get_feriado, set_feriado
from feriado_class import Feriado
from tipo_servico_controller import get_tipo_servico, set_tipo_servico
from tipo_servico_class import TipoServico
from agendamento_controller import get_agendamento, set_agendamento
from agendamento_class import Agendamento
from datetime import date, timedelta
from auth import create_access_token, get_current_user, verify_password, get_user
from fastapi.security import OAuth2PasswordRequestForm

app = FastAPI()

# 🔹 Rota de Login para gerar um Token JWT
@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        return {"error": "Usuário ou senha incorretos"}

    access_token = create_access_token(data={"sub": user["username"]}, expires_delta=timedelta(minutes=30))
    return {"access_token": access_token, "token_type": "bearer"}

# 🔹 Rota pública
@app.get("/")
def read_root():
    return {"message": "Olá, Mundo!"}

# 🔹 Rotas protegidas por autenticação JWT
@app.get("/feriados/")
def read_feriado(id: Optional[int] = None, user: dict = Depends(get_current_user)):
    return {"message": get_feriado(id=id)}

@app.post("/feriados/")
async def set_feriados(request: Request, user: dict = Depends(get_current_user)):
    body = await request.json()
    return {"message": set_feriado(feriado=Feriado(**body))}

@app.get("/clientes/")
def read_clientes(id: Optional[int] = None, user: dict = Depends(get_current_user)):    
    return {"message": get_cliente(id=id)}

@app.post("/clientes/")
async def set_clientes(request: Request, user: dict = Depends(get_current_user)):
    body = await request.json()
    return {"message": set_cliente(cliente=Cliente(**body))}

@app.get("/tipo-servico/")
def read_tipo_servico(id: Optional[int] = None, user: dict = Depends(get_current_user)):
    return {"message": get_tipo_servico(id=id)}

@app.post("/tipo-servico/")
async def set_tipo_servicos(request: Request, user: dict = Depends(get_current_user)):
    body = await request.json()
    return {"message": set_tipo_servico(tipo_servico=TipoServico(**body))}

@app.get("/agenda/")
def read_agenda(id: Optional[int] = None, datahora_inicio: Optional[date] = None, datahora_fim: Optional[date] = None,user: dict = Depends(get_current_user)): 
    return {"message": get_agendamento(id=id, data=datahora_inicio,data_fim=datahora_fim )}

@app.post("/agenda/")
async def set_agenda(request: Request, user: dict = Depends(get_current_user)):
    body = await request.json()
    return {"message": set_agendamento(agendamento=Agendamento(**body))}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
