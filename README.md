# Lyric Scraper
### [Andrew Barlow](https://github.com/dandrewbarlow)

## Description 
This repo contains a script to scrape lyrics for an artist using the PyLyrics python library. As of now (August 2020) the library does not work as is, but I am using a [version that I fixed](https://github.com/dandrewbarlow/PyLyrics) and manually placed in my Python libraries. I submitted a pull request so this might not be relevant soon, but who knows. The script is pretty straightforward, enter the artist name in the "artist" variable in scraper.py, run the script, and the results should be downloaded to a txt file in a "results" folder with the artist name. Because this is a precursor to attempting to use gpt-2 to generate fake lyrics for a given artist, the songs are seperated with a <|endoftext|> tag. This can easily be changed in the script, if desired.
