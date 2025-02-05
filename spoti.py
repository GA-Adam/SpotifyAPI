import random

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

SP = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


def beker():
    bekeres = input('Mi a kedvenc előadód neve?\t')
    return bekeres


def albumokat_leker(bekeres):
    kereses = SP.search(q=bekeres, limit=1, type='artist')
    valasz = SP.artist_albums(artist_id=kereses['artists']['items'][0]['id'], include_groups='album', limit=50)
    sorsolas = random.randint(0, valasz['total'] - 1)
    return valasz, sorsolas


def megjelenit(megjeleniteshez):
    sorsolt_album = megjeleniteshez[0]['items'][megjeleniteshez[1]]['name']
    szavak = sorsolt_album.split()
    leghosszabb_szo = max(szavak, key=len)
    szohossz = len(leghosszabb_szo)
    kitalalando = sorsolt_album.replace(leghosszabb_szo, '_' * szohossz)
    print(f'Az album neve: {kitalalando}')
    tipp = input(f'Találd ki a hiányzó szót!\t').strip()
    if tipp == leghosszabb_szo:
        print('Eltaláltad!')
    else:
        print(f'Nem találtad el, a jó megoldás {leghosszabb_szo} lett volna, a teljes neve pedig: {sorsolt_album}')


def main():
    bekeres = beker()
    megjeleniteshez = albumokat_leker(bekeres)
    megjelenit(megjeleniteshez)


main()
