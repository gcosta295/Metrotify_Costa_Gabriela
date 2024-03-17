import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from usergestion.class_listener import Listener
from usergestion.class_artist import Artist
from usergestion.abrir_datos import abrir_users,abrir_datos_album,abrir_datos_users_artists,abrir_datos_users_listeners
from usergestion.funciones_user import viewUser,searchName,New_user,ingresar_user,borrar_cuenta
from usergestion.abrir_datos import abrir_datos_playlists, abrir_datos_album, artistas_completo_album,link_playlists,guardar_datos
from Gestion_musical.top_functions import top_albums_list
# abrir_users()
# link_albums()
# abrir_datos_album()

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
    
    link_playlists(playlists,listeners,albums)#esto es para que se muestre en los atributos de las playlists el nombre del creador de esta
    
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
         
        if x==2:
            user=ingresar_user(listeners,artists)
            
            us=True
        if x==3:
            if user==0:
                print("No ha iniciado sesion")
                us=True
            else:
                if user.type_user=="listener":
                    user.show_attr()
                    if user.playlists==None:
                        pass
                    else:

                        for i in user.playlists:
                            pass
                            print(f'''          - {i.name}''')
                    us=True
                else:
                    user.show_attr()
                    for i in user.albums:
                        print()
                        print(f'''         {i.name}''')
                        for j in i.tracklist:
                            print(f'''         -{j.name}''')
                    us=True
        if x==4:
            if user==0:
                print("No ha iniciado sesion")
                us=True
            else:
                if user.type_user=="listener":
                    user.cambios_cuenta(listeners)
                    us=True
                else:
                    user.cambios_cuenta(artists)
                    us=True
        if x==5:
            if user==0:
                print("No has iniciado sesion")
                us=True
            else:
                borrar_cuenta(user)
                user=0
                us=True
        if x==6:
            searchName(listeners,artists)
            us=True
        if x==7:
            guardar_datos(playlists,artists,listeners,albums)
            break

    return user

user_menu(None)