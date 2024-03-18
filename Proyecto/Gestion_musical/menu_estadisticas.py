import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from usergestion.abrir_datos import abrir_datos_album,abrir_datos_users_artists,abrir_datos_users_listeners
from usergestion.abrir_datos import abrir_datos_playlists, abrir_datos_album, artistas_completo_album,link_playlists
from Gestion_musical.top_functions import top_albums_list,top_artists_list,top_songs_list,top_listeners_list,graficas1,graficas2
from usergestion.abrir_datos import guardar_datos
#este archivo incluye el bono de mostrar las graficas !!!!
#estas son las funciones grafica1 y grafica2 que se realizan al pedir las estadisticas de cada top 5

def estaditica_menu(): 
    artists=artistas_completo_album(abrir_datos_users_artists(),abrir_datos_album())
    albums=abrir_datos_album() #la explicacion de como funcionan todas estas funciones de abrir datos estan en abrir_datos.py
    listeners=abrir_datos_users_listeners()
    playlists=abrir_datos_playlists(albums)
    link_playlists(playlists,listeners,albums,artists)

    for i in albums:
        i.suma_streams() #esta funcion es para vincular las reproducciones de las canciones a las reproducciones de los albums
    
    albums=top_albums_list(albums)  #suma los streams de toxas las canciones de cada album
    
    artists=artistas_completo_album(abrir_datos_users_artists(),albums) #los aritstas tienen que volver a abrirse pero con los albums ya modificados con la cantidad de reproducciones
    guardar_datos(playlists,artists,listeners,albums)
    for i in artists: #suma las reproducciones de todos los albums del artista
        i.reproducciones_suma()

    artists=top_artists_list(artists) #esto es para organizar los artistas por sus reproducciones
    
    listeners=top_listeners_list(listeners)
    
    us=True
    user=0
    si=True

    while si==True:
        while us==True:
            print("""

        1. Albums con Mayor Cantidad de Streams
        2. Musicos con Mayor Cantidad de Streams
        3. Canciones con Mayor Cantidad de Streams
        4. Listeners con Mayor Cantidad de Streams
        5. Salir""")
            x=input()

            if not x.isnumeric():
                print("Input invalido, tiene que ser numerico")
        
            else:
                x=int(x)
                us=False
                break

        if x==1:
            top_albums=albums[slice(5)] #hace lista con los primeros 5 elemetnos al estar estos organizados por los streams
            print("Top Albums con mas Reproducciones")
            for i in top_albums:
                print('--',i.name,'Streams:',i.streams)
            
            us=True
            graficas2(top_albums,"Top Albums") #muestra la grafica despues de la lista
        elif x==2:
            top_artists=artists[slice(5)]
            print("Top Artists con mas Reproducciones")
            for i in top_artists:
                print('--',i.name,'Streams:',i.reproducciones)
            graficas1(top_artists,"Top Artistas") #muestra la grafica despues de la lista
            us=True
        elif x==3:
            top_songs=top_songs_list(albums)
            print("Top Canciones con mas Reproducciones")
            for i in top_songs:
                print('--',i.name, 'Streams:',i.reproducciones)
            us=True
            graficas1(top_songs,"Top Canciones") #muestra la grafica despues de la lista
        elif x==4:
            top_listeners=listeners[slice(5)]
            print("Top Listeners con mas Reproducciones")
            for i in top_listeners:
                print('--',i.name,'Streams:',i.streams)
            graficas2(top_listeners,"Top Listeners") #muestra la grafica despues de la lista
            us=True
        elif x==5:
            return
        else:
            print("Esa no es una de las opciones numericas")
