
from class_Artist import Artist
from class_Album import Album
from class_Song import Song
from class_Playlist import Playlist


myBand = Artist("The Beatles")

myAlbum = Album("Sgt. Pepper's Lonely Hearts Club Band", myBand, 1967,'Rock')  

song1= Song("With a Little Help from My Friends",myBand,1967,myAlbum)

song2=Song("Lucy in the Sky with Diamonds",myBand,1967,myAlbum)
 
song3=Song("Sgt. Pepper’s Lonely Hearts Club Band",myBand,1967,myAlbum)

myPlaylist = Playlist("Beatles for ever")  

for song in myAlbum.songs:

    myPlaylist.addSong(song)

for song in myPlaylist.songs :

      print(song.name)
