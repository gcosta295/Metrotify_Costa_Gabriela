import re
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


def agregar_cancion(albums):
    si=True
    while si==True: 
        print("Escriba el nombre de la cancion que desea agregar")
        print('Escruba 1 si desea salir')
        x=input()
        if x=="1":
            return
        else:
            for i in albums:
                for j in i.tracklist:
                    if x==j.name:
                        return j
        print("Cancion no encontrada,revise que este bien escrita")
        print('-------------')

def tracks(albums):
    x=True
    songs=[]
    while x==True:
        print('Desea agregar otra cancion al tracklist?')
        
        y=input("""
        1. Si  
        2. No 
        (ingrese el numero)""")

        if y.isnumeric():
            y=int(y)
            if y==1:
                songs.append(agregar_cancion(albums))
            if y==2:
                break
        else:
            print("input no valido")
    return songs         