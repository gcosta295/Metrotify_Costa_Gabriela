from usergestion.abrir_datos import guardar_datos
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

#esta es una funcion que sirve para la cuenta en la que tienes inciaida sesion de la base de datos
def borrar_cuenta(cuenta,listeners,artists,playlists,albums):
    
    x=True
    while x==True:
        y=input("""
    Esta usted seguro? Despues tendra que iniciar sesion en otra cuenta 
    o registrarse otra vez para usar las funciones de Metrotify
        1. Si
        2. No ------>""")
        if not y.isnumeric():
            print("Tiene que poner los numeros")
        else:
            y=int(y)
            if y==1:
                if cuenta.type_user=="listener":
                    listeners.remove(cuenta)
                    guardar_datos(playlists,artists,listeners,albums)
                    cuenta=0
                    return
                else:
                    artists.remove(cuenta)
                    guardar_datos(playlists,artists,listeners,albums) #es necesario guardarlo para que se transmita el cambio a las bases de datos
                    cuenta=0
            if y==2:
                break
            
        