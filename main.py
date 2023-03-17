from fastapi import FastAPI 

app = FastAPI() 

@app.get("/") #el raiz de mi app (end point)

def hello_word():
    return {"message" : "Servidor ejecutando..."}


usuario = [
    {'id':1,
     'username' : 'reinel',
     'password': 'quiz'},
     {'id':2, 
      'username' : 'James',
     'password': 'jajajaj'},
     {'id':3, 
      'username' : 'jai',
     'password': 'lol'}
]

@app.get("/user/all/")
def listar_allUser():
    return usuario

@app.get("/user/unique/{id_usuario}")
def listar_justOne(id_usuario: int):
    #buscar el usuaros en la lista
    for user in usuario:
        #user.id
        if user['id'] == id_usuario:
            return user
    return {"mensaje": "No se encontro ususario"}

