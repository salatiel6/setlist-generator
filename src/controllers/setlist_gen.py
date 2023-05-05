import random


class SetlistGen:
    @staticmethod
    def current_album_setlist(album, opening, closure):
        setlist = []
        acoustic = []

        for song in album:
            if (song['song'] != opening and song['song'] != closure
                    and not song['acoustic']):
                setlist.append(song['song'])
            elif song['acoustic']:
                acoustic.append(song['song'])

        random.shuffle(setlist)
        setlist.insert(0, opening)
        setlist.append(closure)

        return setlist, acoustic

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

    @staticmethod
    def split_previous_songs(gross_setlist, current_album_acoustic):
        setlist = [
            song['song'] for lst in gross_setlist
            for song in lst if not song.get("acoustic")]
        acoustic = [
            song['song'] for lst in gross_setlist for song in lst
            if song.get("acoustic")]
        acoustic.extend(current_album_acoustic)

        random.shuffle(setlist)
        random.shuffle(acoustic)

        return setlist, acoustic

    @staticmethod
    def define_previous_songs_setlist_length(
            previous_albums_setlist, current_album_setlist):
        while len(previous_albums_setlist) >= len(current_album_setlist):
            index = random.randint(0, len(previous_albums_setlist) - 1)
            del previous_albums_setlist[index]

    @staticmethod
    def merge_setlists(
            current_album_setlist, previous_albums_setlist, acoustic_setlist):
        setlist = [
            val for pair in zip(
                current_album_setlist, previous_albums_setlist)
            for val in pair] + \
                current_album_setlist[len(previous_albums_setlist):] + \
                previous_albums_setlist[len(current_album_setlist):]

        middle_index = len(setlist) // 2
        setlist[middle_index:middle_index] = acoustic_setlist

        return setlist


setlist_gen = SetlistGen()
