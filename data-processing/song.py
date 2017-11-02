import hdf5_getters


class Song:
    songCount = 0

    def __init__(self, songH5File):
        self.id = str(hdf5_getters.get_song_id(songH5File))

        self.artistID = str(hdf5_getters.get_artist_id(songH5File))
        self.albumID = str(hdf5_getters.get_release_7digitalid(songH5File))
        self.albumName = str(hdf5_getters.get_release(songH5File))
        self.artistLatitude = str(hdf5_getters.get_artist_latitude(songH5File))
        self.artistLocation = str(hdf5_getters.get_artist_location(songH5File))
        self.artistLongitude = str(hdf5_getters.get_artist_longitude(songH5File))
        self.artistName = str(hdf5_getters.get_artist_name(songH5File))
        self.danceability = str(hdf5_getters.get_danceability(songH5File))
        self.duration = str(hdf5_getters.get_duration(songH5File))
        self.keySignature = str(hdf5_getters.get_key(songH5File))
        self.keySignatureConfidence = str(hdf5_getters.get_key_confidence(songH5File))
        self.tempo = str(hdf5_getters.get_tempo(songH5File))
        self.timeSignature = str(hdf5_getters.get_time_signature(songH5File))
        self.timeSignatureConfidence = str(hdf5_getters.get_time_signature_confidence(songH5File))
        self.title = str(hdf5_getters.get_title(songH5File))
        self.year = str(hdf5_getters.get_year(songH5File))

        self.songCount += 1


    def displaySongCount(self):
        print "Total Song Count %i" % self.songCount


    def displaySong(self):
        print "ID: %s" % self.id
