import sys
import os
import re

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from usergestion.funciones_user import create_own_username, create_user_mail,create_user_name
from Gestion_musical.funcion_crear_albun import validar_fecha,tracklist, validar_link
from usergestion.album_class import Album
from datetime import datetime
# from Gestion_musical.reproduccion_likes import ReproduceSong
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
    
    def crear_album(self):
        idd=str(datetime.now())
        al_name=input("Nombre del Album")
        al_desc=input("Descripcion del Album")
        pattern = r'^(http|https):\/\/([\w.-]+)(\.[\w.-]+)+([\/\w\.-]*)*\/?$' 
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
        self.albums.append(Album(idd,al_name,al_desc,al_portada,date,genre,self.name,self.idd,tracklists,0))

    def reproducciones_suma(self):
        for i in self.albums:
            self.reproducciones+=i.streams

    def show_top_10(self):
        tops=[]
        for i in self.albums:
            for j in i.tracklist:
                tops.append(j)
        top10=sorted(tops, key=lambda song:song.reproducciones, reverse=True)
        top10_songs=top10[slice(5)]
        self.top_songs=top10_songs
        print("""
             Top Songs:""")
        for i in self.top_songs:
            print(f'''
             -- {i.name}''')