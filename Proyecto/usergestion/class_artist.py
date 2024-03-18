import sys
import os
import re

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Gestion_musical.funcion_crear_albun import validar_fecha,tracklist, validar_link
from usergestion.album_class import Album
from datetime import datetime
from usergestion.usuarios import User


class Artist(User):
    def __init__(self,idd, name, email, type_user,username,albums,top_songs,reproducciones): 
        super().__init__(idd,name, email, type_user,username)
        self.albums=albums
        self.top_songs=top_songs
        self.reproducciones=reproducciones

    def show_attr(self):
        print(f"""
              Nombre: {self.name}
              Email: {self.email}
              Total listens: {self.reproducciones}""")
        return ""
    
    def crear_album(self,albums): #permite crear un album, las funciones llamadas estan en Gestion_musical.funcion_crear_album
        idd=str(datetime.now())
        al_name=input("Nombre del Album")
        al_desc=input("Descripcion del Album")
        valido="si"
        while valido=="si":
            al_portada=input("link de la portada del album  ")
            if validar_link(al_portada)==False:
                print("link invalido, asegurese que es un link lo que esta ingresando")
            else:
                break
        date=validar_fecha()
        genre=input("Ingrese el genero predominante del album ----->")
        tracklists=tracklist()
        ele=Album(idd,al_name,al_desc,al_portada,date,genre,self.name,self.idd,tracklists,0,0)
        self.albums.append(ele)
        albums.append(ele) #se agrega a la lista de albums y se devuelve albums para que se pueda guaradr luego en la base de datos
        return albums
    
    def reproducciones_suma(self): #suma los streams de todos sus albums
        streams=0
        for i in self.albums:
            streams+=i.streams
        self.reproducciones=streams
        return ""
    def show_top_10(self): #muestra las top 10 canciones del artisa
        tops=[]
        for i in self.albums:
            for j in i.tracklist:
                tops.append(j)
        top10=sorted(tops, key=lambda song:song.reproducciones, reverse=True) #organiza las canciones por sus streams y luego solo agarra las 10 primeras
        top10_songs=top10[slice(5)]
        self.top_songs=top10_songs
        print("""
             Top Songs:""")
        for i in self.top_songs:
            print(f'''
             -- {i.name}''')
        return ""