import sys
import os
import re

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from usergestion.funciones_user import create_own_username, create_user_mail,create_user_name
from Gestion_musical.funcion_crear_albun import validar_fecha,tracklist, validar_link
from usergestion.album_class import Album
from datetime import datetime


class User(object):
    def __init__(self,idd,name,email,type_user,username):
        self.idd=idd
        self.name=name
        self.email=email
        self.type_user=type_user
        self.username=username

    def cambios_cuenta(self,lista): #esta funcion es para poder realizarle cambioos a la cuenta a la que iniciaste sesion4
        y=True
        j=True

        while j==True:
            while y==True:
                dato=input("""
            Escoga cual es el dato que quiera cambiar
                1. Nombre
                2. Email
                3. Username 
                4. Salir ----->
                        """"")
                if dato.isnumeric():
                    dato=int(dato)
                    if not dato==1 and dato==2 and dato==3:
                        print("Input no valido")
                    else:
                        break
                else:
                    print("Tiene que poner el numero")

            if dato==1:
                self.name=create_user_name(lista)
                y=True
            if dato==2:
                self.email=create_user_mail(lista)
                y=True
            if dato==3:
                self.username=create_own_username(lista)
                y=True
            if dato==4:
                break

        return self







