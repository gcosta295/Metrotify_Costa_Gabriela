import re
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from datetime import *
from usergestion.album_class import Album, Song

#esto tiene todas las funciones necesarias para luego en la clase de Artist crear un album

def validar_fecha(): #esta es una funcion para validar las fechas de los albunes nuevos en el formato de el resto del api de albunes
    si=True
    while si==True:
        publish_date=input("""
                           Fecha de Publicacion
                           Tiene que estar en el formato ISO-8601
                           Ejemplo: 2023-03-14T04:03:00.886Z --->""")
        try:
            datetime.fromisoformat(publish_date)
            si=False
            break
        except:
            print("No es un formato valido")
    print("Fecha Valida")

def tracklist():
    songs=[]
    x=True
    while x==True:
        print('Desea agregar otra cancion al tracklist?')
        
        y=input("""
        1. Si  
        2. No 
        (ingrese el numero)""")

        if y.isnumeric():
            y=int(y)
            if y==1:
                songs.append(crear_song())
            if y==2:
                break
        else:
            print("input no valido")
    return songs

def validar_link(link):
    regex = re.compile(
            r'^(?:http|ftp)s?://' # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
            r'localhost|' #localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    verdad=(re.match(regex, link) is not None) 
    return verdad

def crear_song():
    
    name=input('Nombre de la cancion ---->')
    idd=str(name)+"nuevo"
    duration=validar_duracion()
    likes=None
    valido="si"
    while valido=="si":
        link=input("Ingrese el link de la cancion")
        if bool(validar_link(link))==False:
            print("link invalido, asegurese que es un link lo que esta ingresando")
        else:
            break
    x=Song(idd,name,duration,link,likes)
    return x
    

def validar_duracion():
    x=True
    while x==True:
        duracion=input("""Duracion de la cancion
                   Tiene que mostrar los minutos y segundos
                   Ej: 1:22 -------->""")
        pattern =r"\d{1}\:\d{1,2}" #este es el patron para asegurarse que el formato es "min:seg"
        match = re.match(pattern, duracion) #esto se asegura que el input siga el pattern
        if match:
            print('Formato Valido')
            x=False
            break
        print("Eso no es un formato valido")

    return duracion




