
#el codigo fue programado para tener que reproducir una cancion para poder darle me gusta
# de forma que si buscas un album tendras la opcion de darle me gusta a la cancion que reproduciste y al album
#es la misma funcionalidad si buscas por artista o por playlist

from usergestion.abrir_datos import guardar_albums
def ReproduceSong(user,playlists,artists,albums,listeners): #esta funcion es para la busqueda de los datos de un usuario por su nombre
    r=True
    x=''
    while r==True: #esta parte es apra poder garantizar que se esta buscando al usuario en la base de datos correcta
        j=input("""
        
        Buscar por:
            1. Album
            2. Artista
            3. Cancion
            4. Playlist
            5. Salir ---->""")
        
        if j.isnumeric(): #esto es para verificar que estes agarrando una de las opciones
            if j=="1":
                n=artists
                r=False
                break
            elif j=="2":
                n=artists
                r=False
                break
            elif j=="3":
                n=artists
                r=False
                break 
            elif j=="4":
                n=playlists
                r=False
                break
            elif j=="5":
                r=False
                return
            else:
                print("No es una de las opciones")
        else:
            print("Input no valido")

    
    if j=="1":
            y=input(print("Escriba el nombre del album que desea buscar ---->"))
            for i in albums:
                albu=i
                if y==i.name:
                    print(f"Album: {i.name}")
                    print("-----------")
                    for k in i.tracklist:
                        print("--",k.name)
                    si=True
                    while si==True:
                        x=input(print("Escriba el nombre de la cancion que desea reproducir ---->"))
                        for k in i.tracklist:
                            if k.name==x:
                                print(f"{k.name} ha sido reproducida")
                                k.reproducciones+=1
                                user.streams+=1
                                
                                darlikeSong(k,user)
                                darLikealbum(user,albu)
                                guardar_albums(albums) #es necesario guardarlo para que se quede en la base de datos los cambios en los streams
                                si=False
                                return user,playlists,artists,albums
                        
    if j=="2":
            no=True
            while no==True:
                z=False
                print("Escriba el nombre del artista que desea buscar ")
                print("Va a mostrar los resultados de todos los artistas con ese nombre")
                print(" Escriba 1 para salir")
                y=input()
                if y=="1":
                    return user,playlists,albums,artists
                else:
                    for i in artists:
                        if y==i.name:
                            print('------------------------------')
                            print(i.name)
                            print(i.username)
                            print('---------')
                            artis=i
                            for j in artis.albums:
                                print("-----------")
                                print(f"Album: {j.name}")
                                
                                for k in j.tracklist:
                                    print("--",k.name)
                                    z=True
                if z==True:
                    no=False    
                    si=True
                    break   
                if z==False:     
                    print("Artista no encontrado, asegurese de escribirlo bien")
                    print("Todos los nombres de los artistas tienen un espacio despues del nombre, asegurese de ponerlo")
                    print("---------------")
            
            while si==True:
                                print("Escriba el nombre de la cancion que desea reproducir")
                                print("1 si desea salir ------->")
                                x=input()
                                if x=="1":
                                    break
                                else:
                                    for k in artis.albums:
                                        for m in k.tracklist:
                                            if m.name==x:
                                                print(f"{m.name} ha sido reproducida")
                                                m.reproducciones+=1
                                                user.streams+=1
                                                darlikeSong(m,user)
                                                darlikeArtist(user,artis)
                                                guardar_albums(albums)

                                                return user,playlists,albums,artists
                                            
                                    print("Cancion no encontrada")

    if j=="3":
             si=True
             while si==True:
                print("Escriba el nombre de la cancion que desea reproducir ")
                print(" Escriba 1 para salir")
                x=input()
                if x=="1":
                     break
                     
                for j in albums:
                        for k in j.tracklist:
                            if k.name==x:
                                print(f"{k.name} ha sido reproducida")
                                k.reproducciones+=1
                                user.streams+=1
                                darlikeSong(k,user)
                                guardar_albums(albums)
                                return user,playlists,albums,artists
                            
                print("Cancion no ha sido encontrada")
                 

    if j=="4":
            print("Escriba el nombre de la playlist que desea buscar ---->")
            print("Escriba 1 si desea salir")
            x=input()
            if x=="1":
                 return user,playlists,albums,artists
            else:
                for i in playlists:
                    if i.name==x:
                        print(f"Playlist: {i.name}")
                        print("-----------")
                        for k in i.tracklist:
                            print("--",k.name)

                        si=True
                        while si==True:
                            print("Escriba el nombre de la cancion que desea reproducir ---->")
                            x=input()
                            for k in i.tracklist:
                                    if k.name==x:
                                        print(f"{k.name} ha sido reproducida")
                                        k.reproducciones+=1
                                        user.streams+=1
                                        darlikeSong(k,user)
                                        darLikePlaylist(user,i)
                                        guardar_albums(albums)
                                        
                                        return user,playlists,albums,artists
                                    
                            print("Cancion no encontrada")

                     
                    
                print("playlist no encontrada")
        
    if j=="5":
        return user,playlists,albums,artists
    

# las funciones de dar like trabajan de forma de que si el objeto ya fue likeado por el user se borra de la lista de likes del user
# pero si no esta ya en la lista se agrega
    
def darlikeSong(song,user):
    si=True
    while si==True:
        print("Desea darle/quitar like a esta cancion? 1. si 2. no") #esta funcion agrega un like si no esta likeada y se lo quita si ya esta likeada
        x=input()
        if x=="1":
            for i in user.l_songs:
             if i.idd==song.idd:
                user.l_songs.remove(i)
                print(f"Se le ha quitado me gusta a {song.name}")
                si=False
                
                return user
                
            
            song.likes=+1  
            user.l_songs.append(song)
            print(f"Se le ha dado me gusta a {song.name}")
            si=False
            break
        elif x=="2":
            return  user
        else:
             print("Input No Valido")
    return user

def darlikeArtist(user,artist):
    si=True
    
    while si==True:
        print("Desea darle/quitar like a esta artista? 1. si 2. no") #esta funcion agrega un like si no esta likeada y se lo quita si ya esta likeada
        x=input()
        if x=="1":
            for i in user.l_artists:
             if i.idd==artist.idd:
                user.l_artists.remove(i)
                print(f"Se le ha quitado me gusta a {artist.name}")
                si=False
                return user
                
            
             
            user.l_artists.append(artist)
            print(f"Se le ha dado me gusta a {artist.name}")
            si=False
            return user
        elif x=="2":
            return  user
        else:
             print("Input No Valido")
    return user

def darLikealbum(user,album):
    si=True
    
    while si==True:
        print("Desea darle/quitar like a esta album? 1. si 2. no") #esta funcion agrega un like si no esta likeada y se lo quita si ya esta likeada
        x=input()
        if x=="1":
            for i in user.l_albums:
             if i.ide==album.ide:
                user.l_albums.remove(i)
                print(f"Se le ha quitado me gusta a {album.name}")
                si=False
                return user
                
            
            user.l_albums.append(album)
            print(f"Se le ha dado me gusta a {album.name}")
            si=False
            return user
        elif x=="2":
            return  user
        else:
             print("Input No Valido")
    return user

def darLikePlaylist(user,playlist):
    si=True
    
    while si==True:
        print("Desea darle/quitar like a esta playlist? 1. si 2. no") #esta funcion agrega un like si no esta likeada y se lo quita si ya esta likeada
        x=input()
        if x=="1":
            for i in user.l_playlists:
       
             if i.idd==playlist.idd:
                user.l_playlists.remove(i)
                print(f"Se le ha quitado me gusta a {playlist.name}")
                si=False
                return user
                
            
            user.l_playlists.append(playlist)
            print(f"Se le ha dado me gusta a {playlist.name}")
            si=False
            return user
        elif x=="2":
            return  user
        else:
             print("Input No Valido")
    return user



