import json
import string
import sys
import os
def abrir_users(): #Esta funcion es para transformar las api en bases de datos que se puedan utiliar en el codigo
    archivo=open('Proyecto\\api\\users.json','r',encoding='utf-8')
    datos=archivo.read()
    archivo.close()
    lista=json.loads(datos)
    return lista

def abrir_album(): #Esta funcion es para transformar las api en bases de datos que se puedan utiliar en el codigo
    archivo=open('Proyecto\\api\\albums.json','r',encoding='cp437')
    datos=archivo.read()
    archivo.close()
    lista=json.loads(datos)
    return lista

def abrir_playlist(): #Esta funcion es para transformar las api en bases de datos que se puedan utiliar en el codigo
    archivo=open('Proyecto\\api\\playlists.json','r',encoding='cp437')
    datos=archivo.read()
    archivo.close()
    lista=json.loads(datos)
    return lista

def guardar_datos():
    archivo=open('Proyecto\\datos\\users.txt','w',encoding='cp437')
    x=abrir_users()
    archivo.write(str(x))
    archivo.close

def abrir_txt():
    archivo=open('Proyecto\\datos\\users.txt','r',encoding='cp437')
    datos=archivo.read()
    lista=json.loads(datos)
    print(lista)


#Los relative paths de los api son los siguientes
#api\\users.json
#api\\playlists.json
#api\\albums.json
