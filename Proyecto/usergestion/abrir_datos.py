
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from usergestion.funciones_api import abrir_album,abrir_playlist,abrir_users
from usergestion.playlist_class import Playlist
from usergestion.class_artist import Artist
from usergestion.class_listener import Listener
from usergestion.album_class import Album,Song

def downloadArtists(x): #esta es la funcion para descargar los artists del api
    artists=[]
    alb=[]
    top_songs=[]
    for i in x:
        for k,j in i.items():      
            if j == "musician":
                artists.append(Artist(i["id"], i["name"], i["email"], i["type"], i["username"],alb,top_songs,0))
    return artists

def downloadListeners(x): #esta funcion es para recopilar todos los datos de la api en una lista
    listeners=[]
    play=[]
    likes_0=[]
    likes_1=[]
    likes_2=[]
    likes_3=[]
    
    for i in x:
        for k,j in i.items():
            if j == "listener":
                listeners.append(Listener(i["id"], i["name"], i["email"], i["type"], i["username"],likes_0,likes_1,likes_2,likes_3,play,0))
    return listeners    
    
def downloadPlaylists(playl,albums): #esta es una funcion para abrir las playlists del api
    playlists=[]
    tracks=[]
    for i in playl:
        for k,v in i.items():
            if k=="tracks":
                tracks=[]
                for l in v:
                    for j in albums:
                        for m in j.tracklist:
                          if m.idd==l:
                             tracks.append(m)

                playlists.append(Playlist(i["id"],i["name"],i["description"],None,i["creator"],tracks,None)) 
                tracks=[]
    return playlists

def link_playlists(playlists,users,albums,artists): #esta es una funcion que convierte todos los id del user en sus respectivos objetos
    playl=[]
    l_songs=[]
    l_albums=[]
    l_songs=[]
    l_playlists=[]
    l_artists=[]
    for a in users: 
        for i in playlists:
        
            if i.artist_id==a.idd:
                    playl.append(i)
                    i.artist=a.name  #esto pone el nombre del artista en los atributos de la playliost
            for o in a.l_playlists:   #este bucle recor
                if o==i.idd:
                    l_playlists.append(i)
        a.playlists=playl #esto pone las playlists en el atributos playlists del listener
        playl=[]
        for i in albums:
            for g in i.tracklist:
                for h in a.l_songs:
                    if g.idd==h:
                        l_songs.append(g)

            for u in a.l_albums:
                if u==i.ide:
                    l_albums.append(i)

        for j in a.l_artists:
            for i in artists:
                if i.idd==j:
                        l_artists.append(i)
                       


        a.l_songs=l_songs
        l_songs=[]
        a.l_albums=l_albums
        l_albums=[]
        a.l_artists=l_artists
        l_artists=[]

 

    return users,playlists
    


def guardar_users(liste,arti): #esta es una funcion para guardar los datos de los listeners y artists cuando se cierra el programa en un .txt file
    open('Proyecto\\datos\\users.txt', 'w').close()
    file = open('Proyecto\\datos\\users.txt', 'a',encoding='utf-8')
    for i in liste:
        playl=[]
        l_songs=[]
        l_albums=[]
        l_artists=[]
        l_playlists=[]
        if i.playlists==None:
            playl=None
        else:
            for j in i.playlists:
                playl.append(j.idd)
            for c in i.l_songs:
                l_songs.append(c.idd)
            for b in i.l_albums:
                l_albums.append(b.ide)
            for w in i.l_artists:
                l_artists.append(w.idd)
            for z in i.l_playlists:
                l_playlists.append(z.idd)
        elemento=str({"id":i.idd,"name":i.name,"email":i.email,"type":i.type_user,"username":i.username,"l_artists":l_artists,"l_playlists":l_playlists,"l_albums":l_albums,"l_songs":l_songs,"playlists":playl,"streams":i.streams})
        
        file.write(elemento +"\n")

    for i in arti:
        album=[]
        top=[]
        if i.albums==None:
            album=None
        else:
            for j in i.albums:
                album.append(j.ide)
        elemento2=str({"id":i.idd,"name":i.name,"email":i.email,"type":i.type_user,"username":i.username,"albums":album,"top_songs":top,"reproducciones":i.reproducciones})
        file.write(elemento2 +"\n")
    file.close()

def abrir_users_modificados(): #esta funcion solo aplica en el caso de que exista el txt file, de otra manera se tiene que inicialiozar el api
    lista=[]
    file = open('Proyecto\\datos\\users.txt', 'r', encoding='utf-8')
    counter=0
    while True:
        counter+=1
        line=file.readline()
        if not line:
            break
       
        linef=eval(line)
        lista.append(linef)
    return lista


def downloadListenersModificados(x): #esta funcion es para recopilar todos los datos en las listas, se usa si hay .txt file de donde sacar los datos
    listeners=[]
    for i in x:
        for k,j in i.items():
            if j == "listener":
                listeners.append(Listener(i["id"], i["name"], i["email"], i["type"], i["username"],i["l_artists"],i["l_playlists"],i["l_albums"],i["l_songs"],i["playlists"],i["streams"]))
    return listeners


def downloadArtistsModificados(x): #esta funcion es para recopilar todos los datos en las listas, se usa si hay .txt file de donde sacar los datos
    artists=[]
    for i in x:
        for k,j in i.items():
            if j == "musician":
                artists.append(Artist(i["id"], i["name"], i["email"], i["type"], i["username"],i["albums"],i["top_songs"],i["reproducciones"]))
    return artists


def link_albums(artists,albums): #esta es la funcion que se usa para vincular los datos de los artistas y los albums de los apis
    for i in artists:
        x=i.idd
        y=""
        m=[]
        for j in albums:
            y=j.artist_id
            if x==y:
                m.append(j)
        i.albums=m


def guardar_albums(lista): #esta es una funcion para guardar los datos de los listeners y artists cuando se cierra el programa en un .txt file
    open('Proyecto\\datos\\albums.txt', 'w').close()
    file = open('Proyecto\\datos\\albums.txt', 'a',encoding='utf-8')
    for i in lista:
        tracklist=[]
        for j in i.tracklist:
            tracklist.append(({"id":j.idd,"name":j.name,"duration":j.duration,"link":j.link,'reproducciones':j.reproducciones}))
        elemento=str({"id":i.ide,"name":i.name,"desc":i.desc,"cover":i.cover,"date":i.date,"genre":i.genre,"artist":i.artist,"artist_id":i.artist_id,"tracklist":tracklist,"likes":i.likes,"streams":i.streams,})
        file.write(elemento +"\n")
       
    file.close()


def check_txt_files(): #esta funcion es para revisar si se tiene que empezar el programa con los datos de la api o si ya se ha inicializado antes
    
    file_path = 'Proyecto\\datos\\users.txt'

    try: 
        # get the size of file
        file_size = os.path.getsize(file_path)

        # if file size is 0, it is empty
        if (file_size == 0):
            #print("File is empty")
            return True
        else:
           # print("File is NOT empty")
            return False
    # if file does not exist, then exception occurs
    except FileNotFoundError as e:
        #esto es cuando los .txt no existen 
        return True

def downloadAlbums(x,l): #esta funcion es para cargar los datos de la api en una lista
    songs=[]
    albums=[]
    for i in x: #elementos de la lista
        for k,v in i.items(): #key y value del diccionario del elemento
            if k=="tracklist":
                for h in v:
                    songs.append(Song(h["id"],h["name"],h["duration"],h["link"],0))

            for a in l: #esto es para que en el author de cada album ponga el nombre del artista en lugar del id de este
            
                if k=="artist":
                    if a.idd==v:
                        
                        albums.append(Album(i["id"],i["name"],i["description"],i["cover"],i["published"],i["genre"],a.name,i["artist"],songs,0,0))
            
        songs=[]
    return albums

def abrir_albums_modificados(): #esta es la funcion para abrir los datos del txt si este existe
    lista=[]
    file = open('Proyecto\\datos\\albums.txt', 'r',encoding='utf-8')
    counter=0
    while True:
        counter+=1
        line=file.readline()
        if not line:
            break
        linef=eval(line)
        lista.append(linef)
    return lista


def artistas_completo_album(artistas,albums): #esta funcion permite vincular los albums a el objeto de cada artista
    link_albums(artistas,albums)
    return artistas

def abrir_playlists_modificados(): #esta es la funcion para abrir los datos del txt si este existe
    lista=[]
    file = open('Proyecto\\datos\\playlists.txt', 'r',encoding='cp437')
    counter=0
    while True:
        counter+=1
        line=file.readline()
        if not line:
            break
        linef=eval(line)
        lista.append(linef)
    return lista

def download_albums_modificados(x): # guarda los datos de la api txt de albums en una lista
    songs=[]
    albums=[]
    for i in x: #elementos de la lista
        for k,v in i.items(): #key y value del diccionario del elemento
            if k=="tracklist":
                for h in v:
                    songs.append(Song(h["id"],h["name"],h["duration"],h["link"],h["reproducciones"]))

        albums.append(Album(i["id"],i["name"],i["desc"],i["cover"],i["date"],i["genre"],i["artist"],i["artist_id"],songs,i["likes"],i["streams"]))
        songs=[]
    return albums

def abrir_datos_users_artists(): #esta funcion es para determinar si se tiene que inicializar el programa con las funciones de descargar de api o si se usan las .txt
    if check_txt_files()==True:
        artists=downloadArtists(abrir_users())
    else:
        artists=downloadArtistsModificados(abrir_users_modificados())
    return artists

def abrir_datos_users_listeners(): #esta funcion es para determinar si se tiene que inicializar el programa con las funciones de descargar de api o si se usan las .txt
    if check_txt_files()==True:
        artists=listeners=downloadListeners(abrir_users())
        
    else:
        listeners=downloadListenersModificados(abrir_users_modificados())
    return listeners

def abrir_datos_album():
    artistas=abrir_datos_users_artists() #hay que llamar esta funcion para poder vincular el artista a los albums
    if check_txt_files()==True:
        albums=downloadAlbums(abrir_album(),artistas)
    else:
        albums=download_albums_modificados(abrir_albums_modificados())
    return albums


def guardar_playlists(lista): #esta es la funcion para guardar los datos de la playlist en la api
    open('Proyecto\\datos\\playlists.txt', 'w').close()
    file = open('Proyecto\\datos\\playlists.txt', 'a',encoding='utf-8')
    for i in lista:
        tracklist=[]
        for j in i.tracklist:
            tracklist.append(j.idd)
        elemento=str({"id":i.idd,"name":i.name,"desc":i.desc,"artist":i.artist,"artist_id":i.artist_id,"tracklist":tracklist,"likes":i.likes})
        file.write(elemento +"\n")
       
    file.close()

def downloadPLaylists_modificadas(x,albums):
    playlists=[]
    tracks=[]
    for i in x:
        for k,v in i.items():
            if k=="tracklist":
                tracks=[]
                for l in v:
                    for j in albums:
                        for m in j.tracklist:
                          if m.idd==l:
                             tracks.append(m)
                   

                playlists.append(Playlist(i["id"],i["name"],i["desc"],i['artist'],i["artist_id"],tracks,i["likes"])) 
                tracks=[]
    return playlists

def abrir_datos_playlists(albums):
    if check_txt_files()==True:
        playlists=downloadPlaylists(abrir_playlist(),albums)
   
    else:
        playlists=downloadPLaylists_modificadas(abrir_playlists_modificados(),albums)
    return playlists

def guardar_datos(playlists,artists,listeners,albums):
    guardar_playlists(playlists)
    guardar_users(listeners,artists)
    guardar_albums(albums)

 
# artists=(artistas_completo_album(abrir_datos_users_artists(),abrir_datos_album()))
# albums=abrir_datos_album()

# listeners=abrir_datos_users_listeners()

# playlists=(downloadPlaylists(abrir_playlist(),albums))

# playlists=abrir_datos_playlists(albums)
# link_playlists(playlists,listeners)

# guardar_datos(playlists,artists,listeners,albums)