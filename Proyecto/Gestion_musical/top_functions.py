import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

#eestas funciones son  todas las realcionadas con el modulo de estadisticas

#las primeras se encargan de ordenar las listas de artists,listeners y albums por sus streams
def top_albums_list(albums):
    albums=sorted(albums, key=lambda album:album.streams, reverse=True)
    
    return albums

def top_artists_list(artists):
    artists=sorted(artists, key=lambda artist:artist.reproducciones, reverse=True)
    return artists

def top_songs_list(albums):
    songs=[]
    for i in albums:
        for j in i.tracklist:
            songs.append(j)
    songs=sorted(songs, key=lambda song:song.reproducciones, reverse=True)
    top_songs=songs[slice(5)]
    return top_songs

def top_listeners_list(listeners):
    listeners=sorted(listeners, key=lambda listener:listener.streams, reverse=True)
    
    return listeners


# toda esta parte es para hacer las graficas en BAR con matplotlib para 
from matplotlib import pyplot as plt

def graficas1(lista,texto): #esta funcion es para hacer las graficas de las estadisticas
    names = []
    values = []
    for i in lista:
        names.append(i.name)
        values.append(i.reproducciones)
    
    plt.rcParams.update({'figure.autolayout': True}) #hace que no se corte la figura
    fig, ax = plt.subplots()
    bar_container = ax.bar(names, values)
    ax.set(ylabel='streams', title=texto)
    plt.xticks(rotation=30, ha='right') #es para que quepa el texto de los nombres de las barras abajo
    ax.bar_label(bar_container, fmt='{:,.0f}')
    plt.show()

def graficas2(lista,texto): #esta funcion es para hacer las graficas de las estadisticas
    names = []
    values = []
    for i in lista:
        names.append(i.name)
        values.append(i.streams)
    
    plt.rcParams.update({'figure.autolayout': True})
    fig, ax = plt.subplots()
    bar_container = ax.bar(names, values)
    ax.set(ylabel='streams', title=texto)
    plt.xticks(rotation=30, ha='right')
    ax.bar_label(bar_container, fmt='{:,.0f}')
  
    plt.show()


