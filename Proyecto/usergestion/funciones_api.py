import json

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



#Los relative paths de los api son los siguientes
#Proyecto\\api\\users.json
#Proyecto\\api\\playlists.json
#Proyecto\\api\\albums.json
