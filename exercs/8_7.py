def make_album(name, album, track_numbers=0):
    """Cria um Dict com infos de um álbum musical"""
    music_album = {'name': name, 'album': album}
    if track_numbers > 0:
        music_album['track_numbers'] = track_numbers

    return music_album

print(make_album('Ethel Cain', 'Peverts', ))
print(make_album('Lil Peep', 'Castles II', 16))
print(make_album('Nicole Dollaganger', 'Natural Born Losers', 11))

