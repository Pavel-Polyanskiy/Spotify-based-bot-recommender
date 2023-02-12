import pathlib
import pandas as pd
def get_track_id(artist, song_name):
    id2track = pd.read_csv(str(pathlib.Path().parent.absolute()) + '/data/id2track.csv')
    track_id = id2track[(id2track.song_name == song_name) & (id2track.artist == artist)].index[0]
    return
    