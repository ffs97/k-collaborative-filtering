import re
import os
import sys
import glob
import numpy

import hdf5_getters
from song import Song


def extractFeaturesForSongs(root_path="/home/fat-fighter/Documents/cs771-project/"):
    features_file = open(
        root_path + "hybrid-method/data/features/tracks-features.csv", 'w')
    timbres_file = open(
        root_path + "hybrid-method/data/features/tracks-init-timbres.csv", 'w')

    attributes = ["TrackID", "SongID", "AlbumID", "AlbumName", "ArtistID", "ArtistLatitude", "ArtistLocation", "ArtistLongitude", "ArtistName",
                  "Danceability", "Duration", "KeySignature", "KeySignatureConfidence", "Tempo", "TimeSignature", "TimeSignatureConfidence", "Title", "Year"]

    basedir = root_path + "hybrid-method/data/million-song-subset"
    ext = ".h5"

    delim = "\t"

    features_file.write("SongNumber" + delim)
    features_file.write(delim.join(attributes) + "\n")

    for root, dirs, files in os.walk(basedir):
        files = glob.glob(os.path.join(root, '*' + ext))
        for f in files:
            print f

            song_h5_file = hdf5_getters.open_h5_file_read(f)
            song = Song(song_h5_file)

            row = song.GetAttributes(attributes)
            features_file.write(delim.join(row) + "\n")

            for segment_timbre in song.segmentTimbres:
                segment_timbre = [str(timbre) for timbre in segment_timbre]
                timbres_file.write(str(song.trackID) +
                                   delim + delim.join(segment_timbre) + "\n")

            song_h5_file.close()
    features_file.close()
    timbres_file.close()
