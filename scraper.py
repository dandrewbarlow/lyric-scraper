'''
Andrew Barlow
lyric scraper

This script saves all lyrics by artists in the eponymous list in ./results/artist.txt

Then it goes through all the files in this folder and concatenates them into a results.txt file

I am using this to feed a large dataset of lyrics into gpt-2, so this suits my needs, but it could
easily be modified if you desired

note: current (August 2020) PyLyrics repo doesn't work
I'm using a version I fixed and put into my local python library
https://github.com/dandrewbarlow/PyLyrics
I submitted a pull request tho so hopefully it'll be working soon
'''

from PyLyrics import *
from tqdm import tqdm
import os

artists = [
"Death Grips",
"David Bowie",
"Swans",
"Modest Mouse",
"Kate Bush",
"Radiohead",
"Sufjan Stevens",
"Brian Eno",
"Nirvana",
"Kanye West",
"Sophie",
"Pixies",
"The Velvet Underground",
"Talking Heads",
"Japanese Breakfast",
"Bjork",
"Leonard Cohen",
"Bob Dylan",
"Frank Ocean",
"Animal Collective",
"Pink Floyd",
"Patti Smith",
"Kero Kero Bonito",
"Sublime",
"Laurie Anderson",
"Devo"
]

outFile = "results.txt"

def saveToFile(data, filename):

    file = open( filename, "w")

    if type(data) is list:

        for datum in data:
            file.write("<|startoftext|>\n")
            file.write(datum)
            file.write("<|endoftext|>\n")

    else:
        file.write(data)

    file.close


def getLyrics(artist):

    # check if the data has already been scraped and do nothing if it has
    if os.path.isfile("results/" + artist + ".txt"):
        print(artist + " lyrics found")
        return


    lyrics = []
    tracks = []

    try:
        albums = PyLyrics.getAlbums( singer=artist )
    except ValueError:
        print("Error finding artist")
        return

    try:

        for album in tqdm( albums, desc="Downloading tracklist" ):
            try:
                for track in album.tracks():
                    tracks.append( track )
            except TypeError:
                print("Album miss: " + album)
                pass


        for track in tqdm( tracks, desc="Downloading lyrics" ):

            #print ("> downloading (", track.name, "-", album.name, ")")
            try:
                lyrics.append( PyLyrics.getLyrics(artist, track) )

            except ValueError:
                pass

            except KeyboardInterrupt:
                print("Saving progress")
                saveToFile(lyrics, "results/" + artist + ".txt")
                print("Exiting")
                exit()


        saveToFile(lyrics, "results/" + artist + ".txt")
        return

    except TypeError:
        print("Nothing found")
        return


def main():

    '''
    Turns out, when you scrape a lot of artists, it takes a while. I decided to create individual text files for each artist in the results folder,
    and then concatenate them into a large meta-file so that I could skip re-scraping while trying to iron out this script
    '''

    for artist in artists:
        print("Scraping " + artist)
        getLyrics( artist )


    filenames = os.listdir("./results/")

    file = open(outFile, "w")

    for filename in filenames:
        if os.path.isfile(filename):
            artistFile = open(filename, "r")
            file.write( artistFile.read() )
            artistFile.close()

    file.close()

main()
