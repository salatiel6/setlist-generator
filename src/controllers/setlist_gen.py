import random


class SetlistGen:
    @staticmethod
    def current_album_setlist(album, opening, closure):
        setlist = []

        for song in album:
            if (song['song'] != opening and song['song'] != closure
                    and not song['acoustic']):
                setlist.append(song['song'])

        random.shuffle(setlist)
        setlist.insert(0, opening)
        setlist.append(closure)

        return setlist

    @staticmethod
    def get_album_setlist(album):
        song_dict = {}
        for song in album:
            priority = song['priority']

            if priority not in song_dict:
                song_dict[priority] = []

            song_dict[priority].append(song)

        random_songs = []
        for songs in song_dict.values():
            random_song = random.choice(songs)
            random_songs.append(random_song)

        return random_songs
