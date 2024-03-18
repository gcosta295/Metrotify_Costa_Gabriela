import sys
import os
import re

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from usergestion.playlist_class import Playlist
from Gestion_musical.funcion_crear_playlist import tracks
from usergestion.album_class import Album
from datetime import datetime
# from Gestion_musical.reproduccion_likes import ReproduceSong
from usergestion.usuarios import User

class Listener(User):
    def __init__(self, idd, name, email, type_user,username,l_artists,l_playlists,l_albums,l_songs,playlists,streams): #l_albums y l_songs es una abreviatura para liked albums y liked songs
        super().__init__(idd,name, email, type_user,username)
        self.l_albums=l_albums
        self.l_songs=l_songs
        self.playlists=playlists
        self.l_playlists=l_playlists
        self.l_artists=l_artists
        self.streams=streams
    
    def show_attr(self):
        print(f"""
              Nombre: {self.name}
              Email: {self.email}
             """)
        return " "
    
    def cambios_cuenta(self, lista): #funcion que permite hacerle cambios a los datos personales del user
        return super().cambios_cuenta(lista)
    
    def show_likes(self,l_albums,l_songs): #imprime la lista de liked songs y liked albums
        print(f"""
              Liked Albums:""")
        for i in l_albums:
            print(f"""
              -- {i.name}""")
        print()  
        print(f"""
              Liked Songs:""")
        for i in l_songs:
            print(f"""
              -- {i.name}""")
        return ""
    
    def show_playlists(self,playlists): #imprime la lista de las playlists del escucha
        print(f"""
              Playlists:""")
        for i in playlists:
            print(f"""
              -- {i.name}""")
        return ""
    
    def show_all_likes(self,l_albums,l_songs,l_artists,l_playlists): #esta funcion es solo para la opcion de que el escucha quiera ver su lista de likes
        print('-------------------')
        print(" Esto es solo para ver sus likes, aca no se puede modificar")
        print("Tiene que reproducir los elementos en la opcion de reproducir para agregar o quitar los likes")
        print('-------------------')
        print(f"""
              Liked Albums:""")
        for i in l_albums:
            print(f"""
              -- {i.name}""")
        print()  
        print(f"""
              Liked Songs:""")
        for i in l_songs:
            print(f"""
              -- {i.name}""")
        print(f"""
              Liked Artists:""")
        for i in l_artists:
            print(f"""
              -- {i.name}""")
        print(f"""
              Liked Playlists:""")
        for i in l_playlists:
            print(f"""
              -- {i.name}""")
        return ""
    def crear_playlist(self,albums,playlists): #crea una nueva playlist con los argumentos
        si=True
        while si==True:
            print("Escriba 1 para cancelar")
            print('Escriba cualquier otra cosa para continuar')
            x=input()
            if x=="1":
                break
            else:
                idd=str(datetime.now())
                play_name=input("Nombre de la Playlist--->")
                play_desc=input("Descripcion de la Playlist --->")
                tracklists=tracks(albums)
                ele=Playlist(idd,play_name,play_desc,self.name,self.idd,tracklists,0)
                self.playlists.append(ele)
                playlists.append(ele)
                return playlists
        return playlists    #se devuelve playlists para que se guarde la nueva playlist en la base de datos

