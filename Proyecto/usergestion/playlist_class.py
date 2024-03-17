
class Playlist(object):
    def __init__(self,idd,name,desc,artist,artist_id,tracklist,likes):
        self.idd=idd
        self.name=name
        self.desc=desc
        self.artist=artist
        self.artist_id=artist_id
        self.tracklist=tracklist
        self.likes=likes

    def show_attr(self):
        print(f"""
              Id: {self.idd}
              Name: {self.name}
              Description: {self.desc}
              Creator: {self.artist}
              Tracklist: {self.tracklist}
              Likes: {self.likes}""")