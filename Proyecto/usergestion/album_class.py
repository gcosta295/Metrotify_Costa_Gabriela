
class Album(object):
    def __init__(self,ide,name,desc,cover,date,genre,artist,artist_id,tracklist,likes,streams):
        self.ide=ide
        self.name=name
        self.desc=desc
        self.cover=cover
        self.date=date
        self.genre=genre
        self.artist=artist
        self.artist_id=artist_id
        self.tracklist=tracklist
        self.likes=likes
        self.streams=streams

    def show_attr(self):
        print(f"""
              Id: {self.ide}
              Name: {self.name}
              Description: {self.desc}
              Cover: {self.cover}
              Fecha: {self.date}
              Genero: {self.genre}
              Artista: {self.artist}
              Tracklist: {self.tracklist}
              Likes: {self.likes}""")
        
    def suma_streams(self): #funcion para sumar los streams de todas sus canciones
        for i in self.tracklist:
            self.streams+=i.reproducciones

class Song(object):
    def __init__(self,idd,name,duration,link,reproducciones):
        self.idd=idd
        self.name=name
        self.duration=duration
        self.link=link
        self.reproducciones=reproducciones

    def show_attr(self):
        print(f"""
              Id: {self.idd}
              Name: {self.name}
              Duration: {self.duration}
              Link= {self.link}
              Reproducciones: {self.reproducciones}""")
    