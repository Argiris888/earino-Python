
class Song:

    def __init__(self,name:str,artist:object,year:int,album:object,rank:int=0):
        self.name=name
        self.artist=artist
        self.year=year
        self.album=album
        self.rank=rank

        # using the methods of classes Song and Album 
        artist.addSong(self)
        album.addSong(self)