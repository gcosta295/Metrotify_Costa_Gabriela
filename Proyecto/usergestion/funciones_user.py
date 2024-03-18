import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from usergestion.album_class import Song,Album
import sys
from usergestion.funciones_api import *


#este archivo tiene todas las funciones del modulo de gestion del perfil que no son metodos de las clases



def searchName(listeners,artists): #esta funcion es para la busqueda de los datos de un usuario por su nombre
    r=True
    while r==True: #esta parte es apra poder garfabtizar que se esta buscando al usuario en la base de datos correcta
        j=input("""
        
        Ingrese el numero del tipo de usuario que desea buscar 
                (se van a mostrar todos los usuarios o artistas con ese nombre)
            1. Listener
            2. Artista
            3. Salir ---->""")
        
        if j.isnumeric():
            if j=="1":
                n=listeners
                r=False
                break
            elif j=="2":
                n=artists
                r=False
                break
            elif j=="3":
                r=False
                return 
            else:
                print("No es una de las opciones")
        else:
            print("Input no valido")

    m=True
    while m==True:
       
        print("""
                Nombre que desea buscar 
                (si desea salir escriba 1)----->""")
        y=input()
        if y=="1":
            break
                
       
        else:
            for i in n:
                x=i.name 
                if x==y:
                    if i.type_user=="listener":
                        print(i.show_attr()) #esto muestra los datos del perfil que buscamos
                        print(i.show_likes(i.l_albums,i.l_songs))
                        print(i.show_playlists(i.playlists))
                    
                    else: 
                        print(i.show_attr()) #llama a los metodos de listener o artist
                        print("""Albums:""")
                        for l in i.albums:
                            print("--------------------")
                            print(f"""
                {l.name}""")
                            for k in l.tracklist:
                                print(f"""--{k.name}""")
                        print("------------------")
                        print(i.show_top_10())
            

        print("No tenemos ese nombre en nuestra base de datos,")
        print("Revise que este bien escrito, los artistas tienen un espacio despues de su nombre")
        
    
        
        
    return


#todas las funciones que siguen son las necesarias para crear un nuevo usuario

def create_user_name(m): #esta es parte de las funciones utilizadas para crear un nuevo objeto de clase User \
    x=True
    while x==True:
        name=input("Nombre deseado")
        h=True
        for i in m:
            if i.name==name: #esto garantiza que cada usuario tenga un nombre unico

                print("Ese nombre esta en uso, ingrese otro porfavor")
                n=True

                h=False

 

            else:
                pass
            
        if h==False:
            continue
        else:
            print('ok valido')
            x=False
            break
    return name
                




def create_user_mail(m): #tambien permite realizar un correo y verifica que no exista ese correo anterioremtne en la base de datos
    x=True
    while x==True:
        h=True
        mail=input("""
                   Ingrese el correo que desee, sin el @unimet.edu.ve
                   Ejemplo: gcosta ---->""")
        mail+="@unimet.edu.ve"
        for i in m:
            if i.email==mail:
                print("Ese correo esta en uso, desea ingresar otro?")
                
                h=False

            else:
             pass
        
        if h==False:
            continue
        else:
            print(mail)
            return mail
            
       
def create_user_type():
    x=True
    while x==True:
        tipo=input("""
Ingrese el tipo de usuario que desea (Solo el numero)
1. Listener
2. Musician
                   """)
        if tipo.isnumeric():
            tipo=int(tipo)
            if tipo==1:
                tipo="listener"
                x=False
            if tipo==2:
                tipo="musician"
                x=False
            else:
                pass
        else:
            print("No valido")
    return tipo


def user_creation_id(username):
    user_id=username+str("Nuevo")
    return user_id


def create_own_username(m): #este es para que cada usuario haga su propio username, verificando aue no existe en la base de datos
    x=True
    while x==True:
        h=True
        username=input("""
                   Ingrese el usuario que desee---->""")
        for i in m:
            if i.username==username:
                print("Ese usuario esta en uso, desea ingresar otro?")
                
                h=False

            else:
             pass
        
        if h==False:
            continue
        else:
            print(username)
            return username


def New_user(listeners,artists,Listener,Artist): #listeners y artists son las listas de los objetos
    tipo=create_user_type()
    

    if tipo=="listener":
        lista1=[]
        lista2=[]
        lista4=[]
        lista3=[]
        lista5=[]
        nombre=create_user_name(listeners)
        correo=create_user_mail(listeners)
        usern=create_own_username(listeners)
        ide=user_creation_id(usern)
        listeners.append(Listener(ide,nombre,correo,tipo,usern,lista1,lista2,lista3,lista4,lista5,0))

    if tipo=="musician":
        top=[]
        albu=[]

        nombre=create_user_name(artists)
        correo=create_user_mail(artists)
        usern=create_own_username(artists)
        ide=user_creation_id(usern)
        artists.append(Artist(ide,nombre,correo,tipo,usern,albu,top,0))

    return listeners,artists

def ingresar_user(listeners,artists): #esta funcion es para ingresa r a una de las cuentas que ya existen, para poder realizarles cambios a estas
   
    y=True
    while y==True:

        tipeo=input("Es un 1. Listener o 2. Artista --->")
        if tipeo.isnumeric():
            tipeo=int(tipeo)
            if tipeo==1:
                x=True
                pass
            elif tipeo==2:
                x=True
                pass
            else:
                print("Input no valido")
                x=False
        else:
            print("Tiene que poner el numero")
            x=False

        while x==True:
        
            usern=input("Ingrese el username de su cuenta --->")
            if tipeo==1:
                for i in listeners:
                    if i.username==usern:
                        print("Usuario encontrado")
                        x=False
                        return i
                    else: 
                        pass
            if tipeo==2:
                for i in artists:
                    if i.username==usern:
                        print("Usuario encontrado")
                        return i
                    else: 
                        pass
                
            print('No se ha encontrado al usuario, revise que exista')
            y=True
    



