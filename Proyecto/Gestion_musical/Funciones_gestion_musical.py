from pathlib import Path
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import re
from datetime import *


from usergestion.album_class import Album, Song
from usergestion.funciones_api import abrir_album,abrir_users





def viewalbumandsongs(): #esto permite visualizar todos los albumes y las canciones que contiene el album
    for i in albums:
      i.show_attr()
      for j in i.tracklist:
        j.show_attr()


def viewsongs(x): #Esta funcion permite ver los datos de las canciones en un album
    for i in x:
      for j in i.tracklist:
        j.show_attr()

    


