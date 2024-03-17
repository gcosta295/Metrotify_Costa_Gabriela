import json
import string
def abrir_users(): #Esta funcion es para transformar las api en bases de datos que se puedan utiliar en el codigo
    archivo=open('api\\users.json','r',encoding='utf-8')
    datos=archivo.read()
    archivo.close()
    lista=json.loads(datos)
    return lista

def abrir_album(): #Esta funcion es para transformar las api en bases de datos que se puedan utiliar en el codigo
    archivo=open('api\\albums.json','r',encoding='cp437')
    datos=archivo.read()
    archivo.close()
    lista=json.loads(datos)
    return lista

def abrir_playlist(): #Esta funcion es para transformar las api en bases de datos que se puedan utiliar en el codigo
    archivo=open('api\\playlists.json','r',encoding='cp437')
    datos=archivo.read()
    archivo.close()
    lista=json.loads(datos)
    return lista

def guardar_datos():
    archivo=open('datos\\users.txt','w',encoding='cp437')
    x=abrir_users()
    archivo.write(str(x))
    archivo.close

def abrir_txt():
    archivo=open('datos\\users.txt','r',encoding='cp437')
    datos=archivo.read()
    lista=json.loads(datos)
    print(lista)


#Los relative paths de los api son los siguientes
#api\\users.json
#api\\playlists.json
#api\\albums.json
