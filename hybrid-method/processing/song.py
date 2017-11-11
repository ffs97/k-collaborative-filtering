import numpy as np
import hdf5_getters


class Song:
    songCount = 0

    def __init__(self, songH5File):
        self.trackID = str(hdf5_getters.get_track_id(songH5File))
        self.songID = str(hdf5_getters.get_song_id(songH5File))
        self.artistID = str(hdf5_getters.get_artist_id(songH5File))
        self.albumID = str(hdf5_getters.get_release_7digitalid(songH5File))
        self.albumName = str(hdf5_getters.get_release(songH5File))
        self.artistLatitude = str(hdf5_getters.get_artist_latitude(songH5File))
        self.artistLocation = str(hdf5_getters.get_artist_location(songH5File))
        self.artistLongitude = str(
            hdf5_getters.get_artist_longitude(songH5File))
        self.artistName = str(hdf5_getters.get_artist_name(songH5File))
        self.danceability = str(hdf5_getters.get_danceability(songH5File))
        self.duration = str(hdf5_getters.get_duration(songH5File))
        self.keySignature = str(hdf5_getters.get_key(songH5File))
        self.keySignatureConfidence = str(
            hdf5_getters.get_key_confidence(songH5File))
        self.tempo = str(hdf5_getters.get_tempo(songH5File))
        self.timeSignature = str(hdf5_getters.get_time_signature(songH5File))
        self.timeSignatureConfidence = str(
            hdf5_getters.get_time_signature_confidence(songH5File))
        self.title = str(hdf5_getters.get_title(songH5File))
        self.year = str(hdf5_getters.get_year(songH5File))
        self.segmentTimbres = np.array(
            hdf5_getters.get_segments_timbre(songH5File), float)

        self.songCount += 1

    def DisplaySongCount(self):
        print "Total Song Count %i" % self.songCount

    def DisplaySong(self):
        print "ID: %s" % self.songID

    def GetAttributes(self, attributes):
        row = [str(self.songCount)]

        for attribute in attributes:
            if attribute == 'AlbumID':
                row.append(self.albumID)
            elif attribute == 'AlbumName':
                albumName = self.albumName
                albumName = albumName.replace(',', "")
                row.append("\"" + albumName + "\"")
            elif attribute == 'ArtistID':
                row.append("\"" + self.artistID + "\"")
            elif attribute == 'ArtistLatitude':
                latitude = self.artistLatitude
                if latitude == 'nan':
                    latitude = ''
                row.append(latitude)
            elif attribute == 'ArtistLocation':
                location = self.artistLocation
                location = location.replace(',', '')
                row.append("\"" + location + "\"")
            elif attribute == 'ArtistLongitude':
                longitude = self.artistLongitude
                if longitude == 'nan':
                    longitude = ''
                row.append(longitude)
            elif attribute == 'ArtistName':
                row.append("\"" + self.artistName + "\"")
            elif attribute == 'Danceability':
                row.append(self.danceability)
            elif attribute == 'Duration':
                row.append(self.duration)
            elif attribute == 'KeySignature':
                row.append(self.keySignature)
            elif attribute == 'KeySignatureConfidence':
                row.append(self.keySignatureConfidence)
            elif attribute == 'SongID':
                row.append("\"" + self.songID + "\"")
            elif attribute == 'TrackID':
                row.append("\"" + self.trackID + "\"")
            elif attribute == 'Tempo':
                row.append(self.tempo)
            elif attribute == 'TimeSignature':
                row.append(self.timeSignature)
            elif attribute == 'TimeSignatureConfidence':
                row.append(self.timeSignatureConfidence)
            elif attribute == 'Title':
                row.append("\"" + self.title + "\"")
            elif attribute == 'Year':
                row.append(self.year)
            else:
                print "There was some Error with the data file" + file
                row.append("ERROR")

        return row
