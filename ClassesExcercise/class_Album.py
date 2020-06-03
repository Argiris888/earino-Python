from class_Song import Song

class Album:

    
    def __init__(self,name:str,artist:object,year:int,genre:str,songs:list=[]):
        self.name=name
        self.artist=artist
        self.year=year
        self.genre=genre
        self.songs=songs
        artist.addAlbum(self)

    
    
    def addSong(self,song:object):
       
        # to make sure that the added song is object
        if isinstance(song,Song):
        
            self.songs.append(song)

 
    