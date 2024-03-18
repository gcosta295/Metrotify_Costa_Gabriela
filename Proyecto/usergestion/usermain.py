import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from usergestion.class_listener import Listener
from usergestion.class_artist import Artist
from usergestion.abrir_datos import abrir_datos_album,abrir_datos_users_artists,abrir_datos_users_listeners
from usergestion.funciones_user import searchName,New_user,ingresar_user
from usergestion.abrir_datos import abrir_datos_playlists, abrir_datos_album, artistas_completo_album,link_playlists,guardar_datos
from Gestion_musical.top_functions import top_albums_list
from usergestion.borrar_datos import borrar_cuenta

#este es el menu principal de gestion de perfil


def user_menu(real): #esta funcion es para realizar un menu de todas las opciones del modulo "Gestion de Perfil"
    artists=artistas_completo_album(abrir_datos_users_artists(),abrir_datos_album())
    albums=abrir_datos_album() #la explicacion de como funcionan todas estas funciones de abrir datos estan en abrir_datos.py
    listeners=abrir_datos_users_listeners()
    playlists=abrir_datos_playlists(albums)

    for i in albums:
        i.suma_streams() #esta funcion es para vincular las reproducciones de las canciones a las reproducciones de los albums
    
    albums=top_albums_list(albums)  #suma los streams de toxas las canciones de cada album
    for i in artists:
        i.reproducciones_suma()
    artists=artistas_completo_album(abrir_datos_users_artists(),albums) #los aritstas tienen que volver a abrirse pero con los albums ya modificados con la cantidad de reproducciones

    for i in artists: #suma las reproducciones de todos los albums del artista
        i.reproducciones_suma()
    
    link_playlists(playlists,listeners,albums,artists)#esto es para que se muestre en los atributos de las playlists el nombre del creador de esta
    
    if real==None: #este if es para que se guarde los datos entre el main menu y la gestion del usuario
        user=0
    else:
        user=real
    us=True
    
    si=True
  
    
    while si==True:
        while us==True:
            print("""

        1. Registrar usuario nuevo
        2. Ingresar a una cuenta
        3. Ver datos de su perfil
        4. Modificar informacion personal de la cuenta
        5. Borrar datos de la cuenta
        6. Buscar perfil de otro usuario
        7. Salir de gestion del perfil""")
            x=input()

            if not x.isnumeric():
                print("Input invalido, tiene que ser numerico")
        
            else:
                x=int(x)
                us=False
                break

        if x==1:
            New_user(listeners,artists,Listener,Artist)
            print("Usuario Registrado Exitosamente")
            print("Debe ahora iniciar sesion con su usuario para acceder a su cuenta")
            us=True
         
        elif x==2:
            user=ingresar_user(listeners,artists)
            
            us=True
        elif x==3:
            if user==0:
                print("No ha iniciado sesion")
                us=True
            else:
                if user.type_user=="listener":
                   print(user.show_attr()) #esto muestra los datos del perfil que buscamos
                   print(user.show_likes(user.l_albums,user.l_songs))
                   print(user.show_playlists(user.playlists))
                   us=True
                else:
                    print(user.show_attr())
                    print("""Albums:""")
                    for l in user.albums:
                        print("--------------------")
                        print(f"""
             {l.name}""")
                        for k in l.tracklist:
                            print(f"""--{k.name}""")
                    print("------------------")
                    print(user.show_top_10())
                    
                    us=True

        elif x==4:
            if user==0:
                print("No ha iniciado sesion")
                us=True
            else:
                if user.type_user=="listener":
                    user.cambios_cuenta(listeners) 
                    guardar_datos(playlists,artists,listeners,albums) #se tiene que guardar para que se transmita a la base de datos
                    us=True
                else:
                    user.cambios_cuenta(artists)
                    guardar_datos(playlists,artists,listeners,albums)
                    us=True
        elif x==5:
            if user==0:
                print("No has iniciado sesion")
                us=True
            else:
                user=borrar_cuenta(user,listeners,artists,playlists,albums)
                user=0 #se vuelve el user 0 para que te vuelva a pedir iniciar sesion 
                us=True
        elif x==6:
            searchName(listeners,artists)
            us=True
        elif x==7:
            guardar_datos(playlists,artists,listeners,albums)
            break
        else:
            print("No es una de las opciones")
            us=True

    return user

