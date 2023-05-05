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
    def get_album_setlist(album, previous_setlist):
        song_dict = {}
        for song in album:
            priority = song['priority']

            if priority not in song_dict:
                song_dict[priority] = []

            song_dict[priority].append(song)

        random_songs = []
        for songs in song_dict.values():
            random_song = random.choice(songs)
            while random_song['song'] in previous_setlist:
                random_song = random.choice(songs)
            random_songs.append(random_song)

        if not random_songs:
            raise ValueError('No songs found in album')

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

    @staticmethod
    def write_setlists(setlists):
        with open('setlists.txt', 'w') as f:
            for i, inner_list in enumerate(setlists, start=1):
                f.write(f'---{i}---\n')
                for j, item in enumerate(inner_list, start=1):
                    f.write(f'{j}.{item.upper()}\n')
                f.write('\n')


setlist_gen = SetlistGen()
