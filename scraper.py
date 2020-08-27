'''
Andrew Barlow
lyric scraper

note: current (August 2020) PyLyrics repo doesn't work
I'm using a version I fixed and put into my local python library
https://github.com/dandrewbarlow/PyLyrics
I submitted a pull request tho so hopefully it'll be working soon
'''
from PyLyrics import *
from tqdm import tqdm


artist = "Pixies"

def main():

    lyrics = []
    tracks = []

    albums = PyLyrics.getAlbums( singer=artist )


    try:

        filename = artist + ".txt"

        file = open("results/" + filename, "w")


        for album in tqdm( albums, desc="Downloading tracklist" ):
            for track in album.tracks():
                tracks.append( track )


        for track in tqdm( tracks, desc="Downloading lyrics" ):

            #print ("> downloading (", track.name, "-", album.name, ")")
            try:
                lyrics = PyLyrics.getLyrics(artist, track)

                file.write(lyrics)
                file.write("\n<|endoftext|>\n")

            except ValueError:
                    pass

            #print ("> exporting")


        file.close()

    except TypeError:
        print("Nothing found")


main()
