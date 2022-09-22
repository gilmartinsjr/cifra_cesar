from fastapi import FastAPI
import requests
import random
from pydantic import BaseModel



app=FastAPI()



@app.get("/getCifra")
def getCifra():
    frase = requests.get("https://dog-api.kinduff.com/api/facts")
    frase = frase.json()
    frase = frase.get('facts')
    frase = frase[0]
    frase = frase.upper()



   chave = random.randrange(1,25)
    frase_encriptada = ""



   alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H",
                "I", "J", "K", "L", "M", "N", "O", "P",
                "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]



   alfabeto_cesar = []



   for letra in alfabeto[chave:len(alfabeto)+1]:
        alfabeto_cesar.append(letra)



   for letra in alfabeto[0:chave]:
        alfabeto_cesar.append(letra)



   for caractere in frase:
        if caractere in alfabeto:
            posicao = alfabeto.index(caractere)
            caractere = alfabeto_cesar[posicao]
            frase_encriptada = frase_encriptada + caractere
        else:
            frase_encriptada = frase_encriptada + caractere
    frase_encriptada = frase_encriptada.capitalize()
    return(f"frase encriptada: {frase_encriptada}",f"chave: {chave}")



class f_encriptada(BaseModel):
    fr_encriptada: str
    chave: int



@app.post("/resolveCifra")
def resolveCifra(fr_encriptada: f_encriptada):



   frase_encriptada = fr_encriptada.fr_encriptada
    frase_encriptada = frase_encriptada.upper()
    chave = fr_encriptada.chave
    frase_decriptada = ""



   alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H",
                "I", "J", "K", "L", "M", "N", "O", "P",
                "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]



   alfabeto_cesar = []



   for letra in alfabeto[chave:len(alfabeto)+1]:
        alfabeto_cesar.append(letra)



   for letra in alfabeto[0:chave]:
        alfabeto_cesar.append(letra)



   for caractere in frase_encriptada:
        if caractere in alfabeto_cesar:
            posicao = alfabeto_cesar.index(caractere)
            caractere = alfabeto[posicao]
            frase_decriptada = frase_decriptada + caractere
        else:
            frase_decriptada = frase_decriptada + caractere
    frase_decriptada = frase_decriptada.capitalize()
    return(frase_decriptada)
