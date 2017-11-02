import re
import os
import sys
import glob
from song import Song
import hdf5_getters


def main():
    rootPath = "/home/fat-figther/Documents/cs771-project/"
    outputFile = open(rootPath + "/hybrid-method/data/songs-features.csv", 'w')

    attributes = ["SongID", "AlbumID", "AlbumName", "ArtistID", "ArtistLatitude", "ArtistLocation", "ArtistLongitude", "ArtistName",
                  "Danceability", "Duration", "KeySignature", "KeySignatureConfidence", "Tempo", "TimeSignature", "TimeSignatureConfidence", "Title", "Year"]

    basedir = "/home/fat-fighter/Documents/cs771-project/hybrid-method/data"
    ext = ".h5"

    delim = "\t"

    outputFile.write("SongNumber,")
    outputFile.write(delim.join(attributes) + "\n")

    for root, dirs, files in os.walk(basedir):
        files = glob.glob(os.path.join(root, '*' + ext))
        for f in files:
            print f

            songH5File = hdf5_getters.open_h5_file_read(f)
            song = Song(str(hdf5_getters.get_song_id(songH5File)))

            row = [str(song.songCount)]

            for attribute in attributes:
                if attribute == 'AlbumID':
                    row.append(song.albumID)
                elif attribute == 'AlbumName':
                    albumName = song.albumName
                    albumName = albumName.replace(',', "")
                    row.append("\"" + albumName + "\"")
                elif attribute == 'ArtistID':
                    row.append("\"" + song.artistID + "\"")
                elif attribute == 'ArtistLatitude':
                    latitude = song.artistLatitude
                    if latitude == 'nan':
                        latitude = ''
                    row.append(latitude)
                elif attribute == 'ArtistLocation':
                    location = song.artistLocation
                    location = location.replace(',', '')
                    row.append("\"" + location + "\"")
                elif attribute == 'ArtistLongitude':
                    longitude = song.artistLongitude
                    if longitude == 'nan':
                        longitude = ''
                    row.append(longitude)
                elif attribute == 'ArtistName':
                    row.append("\"" + song.artistName + "\"")
                elif attribute == 'Danceability':
                    row.append(song.danceability)
                elif attribute == 'Duration':
                    row.append(song.duration)
                elif attribute == 'KeySignature':
                    row.append(song.keySignature)
                elif attribute == 'KeySignatureConfidence':
                    row.append(song.keySignatureConfidence)
                elif attribute == 'SongID':
                    row.append("\"" + song.id + "\"")
                elif attribute == 'Tempo':
                    # print "Tempo: " + song.tempo
                    row.append(song.tempo)
                elif attribute == 'TimeSignature':
                    row.append(song.timeSignature)
                elif attribute == 'TimeSignatureConfidence':
                    # print "time sig conf: " + song.timeSignatureConfidence
                    row.append(song.timeSignatureConfidence)
                elif attribute == 'Title':
                    row.append("\"" + song.title + "\"")
                elif attribute == 'Year':
                    row.append(song.year)
                else:
                    print "There was some Error with the data file" + file
                    row.append("ERROR")

            outputFile.write(delim.join(row) + "\n")
            songH5File.close()
    outputFile.close()


if __name__ == "__main__":
    main()
