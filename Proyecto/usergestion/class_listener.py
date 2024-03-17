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
              Liked Songs: {self.l_songs}
              Liked Albums: {self.l_albums}
              Playlists:""")

    def cambios_cuenta(self, lista):
        return super().cambios_cuenta(lista)
    
    def buscar_cancion(albums,artistas):
       si=True
       while si==True:
        while us==True:
            print("""

        1. Albums
        2. Cancion
        3.Artista""")
            x=input()

            if not x.isnumeric():
                print("Input invalido, tiene que ser numerico")
        
            else:
                x=int(x)
                us=False
                break
        if x==1:
           pass 

    def reproducir_dar_like(self,playlists,artists,albums): #al ser una funcion extremadamente larga ya que permite reproducir y dar likes esta en otra archivo
        ReproduceSong(self,playlists,artists,albums)

    def crear_playlist(self,albums):
        idd=str(datetime.now())
        play_name=input("Nombre de la Playlist--->")
        play_desc=input("Descripcion de la Playlist --->")
        tracklists=tracks(albums)
        self.playlists.append(Playlist(idd,play_name,play_desc,self.name,self.idd,tracklists,0))

