from fastapi import FastAPI

# REALIZAR PIP INSTALL DO fastapi E DO uvicorn

# PARA EXECUTAR DE FORMA LOCAL DEVE SER UTILIZADO O UVICORN, NO TERMINAL DIGITE O COMANDO "uvicorn {nome do arquivo}:{nome da api criada}"

app = FastAPI()

clientes = {
    1:{"nome": "", "idade": "", "setor": "", "Anos de contribuição": ""},
    2:{"nome": "", "idade": "", "setor": "", "Anos de contribuição": ""},
    3:{"nome": "", "idade": "", "setor": "", "Anos de contribuição": ""},
    4:{"nome": "", "idade": "", "setor": "", "Anos de contribuição": ""},
    5:{"nome": "", "idade": "", "setor": "", "Anos de contribuição": ""},
    6:{"nome": "", "idade": "", "setor": "", "Anos de contribuição": ""},
    7:{"nome": "", "idade": "", "setor": "", "Anos de contribuição": ""},
    8:{"nome": "", "idade": "", "setor": "", "Anos de contribuição": ""},
}

@app.get("/")
def home():
    return {'Clientes': len(clientes)}


@app.get("/clientes/{id_clientes}")
def analisa_clientes(id_clientes: int):
    return clientes[id_clientes]