from class_Song import Song
from class_Album import Album

class Artist:

    def __init__(self,name:str,albums:list=[],songs:list=[]):
        self.name=name
        self.albums=albums
        self.songs=songs

   
    def addAlbum(self,album:object):

        # to make sure that the added album is object
        if isinstance(album,Album):
        
            self.albums.append(album)


    def addSong(self,song:object):
       
        # to make sure that the added song is object
        if isinstance(song,Song):
        
            self.songs.append(song)
