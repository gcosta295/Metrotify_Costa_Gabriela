import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from usergestion.abrir_datos import abrir_datos_album,abrir_datos_users_artists,abrir_datos_users_listeners
from usergestion.abrir_datos import abrir_datos_playlists, abrir_datos_album, artistas_completo_album,link_playlists,guardar_datos,guardar_users
from usergestion.usermain import user_menu
from Gestion_musical.top_functions import top_albums_list
from Gestion_musical.menu_estadisticas import estaditica_menu
from Gestion_musical.reproduccion_likes import ReproduceSong

def music_menu(): #esta funcion es para realizar un menu de todas las opciones del menu principal
    
    us=True
    user=0
    si=True
    
    while us==True:
            artists=artistas_completo_album(abrir_datos_users_artists(),abrir_datos_album())
            albums=abrir_datos_album() #la explicacion de como funcionan todas estas funciones de abrir datos estan en abrir_datos.py
            listeners=abrir_datos_users_listeners()
            playlists=abrir_datos_playlists(albums)
            link_playlists(playlists,listeners,albums,artists)
            albums=top_albums_list(albums)
            
             #esto es para que se muestre en los atributos de las playlists el nombre del creador de esta
            #los datos estan dentro del loop para que se actualicen si se cambio algo en la gestion del perfil
             #esto ordena la lista de albums por los que tienen mas streams
            for i in artists:
                i.reproducciones_suma

            if type(user)==int:
                 print()
                 print("Tiene que iniciar sesion para usar el programa")
                 print()
                 print("Se le va a enviar al menu de gestion de perfil")
                 user=user_menu(None) #esto es para obligar a quien usa el programa a tener que iniciar sesion para usarlo

                
            else:
                for i in listeners:
                     if i.name==user.name: #esto es para vincular el user y las listas con el 
                                    #ue se esoge en la gestion de perfil, sino los cambios no se ven reflejados en las bases de datos
                         user=i
                     
                for i in artists:
                     if i.name==user.name:
                         user=i
                if user.type_user=="listener": #muestra dos menu dependiendo de que es el user que inicio sesion
                    print("""

                
                1. Reproducir Cancion
                2. Crear Playlist
                3. Gestion Perfil
                4. Ver estadisticas
                5. Ver Likes
                6. Cerrar Programa """)
                    x=input()

                    if not x.isnumeric():
                        print("Input invalido, tiene que ser numerico")
                
                    else:
                        x=int(x)
                        us=True
                        if x==2:
                    
                            playlists=user.crear_playlist(albums,playlists) #siempre se tiene que volver a especificar que se devuelve porque si no no se guardan los cambios en las bases de datos principales
                            guardar_datos(playlists,artists,listeners,albums)
                            us=True
                        
                        elif x==1:
                            ReproduceSong(user,playlists,artists,albums,listeners) #esta es una funcion para reproducir las canciones, no la pude meter dentro del listener porque no se me guardaban los cambios
                            guardar_users(listeners,artists) #siempre se pone guardar_users() para que cuando vuelva al loop del menu abra las listas con los cambios realizados
                            
                            
                            us=True
                            
                            
                        elif x==3:
                            user_menu(user) #el user es necesario entre parentesis para que se guarde el user entre la gestion de perfil y el menu principal
                        
                        elif x==4:
                            guardar_datos(playlists,artists,listeners,albums)
                            estaditica_menu()
                        elif x==5:
                            user.show_all_likes(user.l_albums,user.l_songs,user.l_artists,user.l_playlists)
                        elif x==6:
                            guardar_datos(playlists,artists,listeners,albums)
                            return
                        else:
                            print("No es una de las opciones")
                        
                        
                elif user.type_user=="musician": #muestra dos menu dependiendo de que es el user que inicio sesion
                    print("""

                
                1. Crear Album
                2. Gestion de Perfil
                3. Ver estadisticas
                4. Cerrar programa""")
                    y=input()

                    if not y.isnumeric():
                        print("Input invalido, tiene que ser numerico")
                
                    else:
                        y=int(y)
                        us=True

                        if y==1:
                    
                            albums=user.crear_album(albums)
                            guardar_datos(playlists,artists,listeners,albums)
                            us=True
                
                        elif y==2:
                            guardar_datos(playlists,artists,listeners,albums)
                            user_menu(user)
                            
                            us=True
                            guardar_datos(playlists,artists,listeners,albums)
                        elif y==3:
                            guardar_datos(playlists,artists,listeners,albums)
                            estaditica_menu()
                        elif y==4:
                            guardar_datos(playlists,artists,listeners,albums)
                            print("Cierre de Metrotify")
                            return
                        else:
                            print("No es una de las opciones")
                    
                
                

          

    return user
