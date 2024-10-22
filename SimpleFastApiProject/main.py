## on va créer notre API , api hello word
from fastapi import FastAPI 


app = FastAPI()
##on définit les requetes et les chemins d'accès
#la fonction get permet de récupérer des infos 
@app.get("/") #page principale

def root(): 
    #chose très simple , elle va retourner le message hello world
    return {"message : Welcome to this deployment project :D"}

@app.get("/data/")

def root():
    return {"La base de données "}
#on va rendre se message accessible , on va utiliser docker 
