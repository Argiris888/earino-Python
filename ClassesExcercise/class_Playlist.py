class Playlist:

    def __init__(self,name:str,songs:list=[]):
        self.name=name
        self.songs=songs

    def addSong(self,song:object):

         self.songs.append(song)
