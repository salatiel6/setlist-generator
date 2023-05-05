import random

from controllers import albums, setlist_gen


def define_current_album():
    opening = "whispers in the dark"
    closure = "the final episode"
    setlist, acoustic = \
        setlist_gen.current_album_setlist(albums.EMPTY_OCEAN, opening, closure)

    return setlist, acoustic


def define_previous_albums():
    albums_list = [albums.BLOOD_SHOT_EYES, albums.GOING_INSANE,
                   albums.NOTHING_TO_SAY, albums.BREATH_ONCE_MORE]
    gross_setlist = []

    for album in albums_list:
        gross_setlist.append(setlist_gen.get_album_setlist(album))

    return gross_setlist


def main():
    current_album_setlist, current_album_acoustic = define_current_album()

    gross_setlist = define_previous_albums()

    previous_albums_setlist, acoustic_setlist = \
        setlist_gen.split_previous_songs(gross_setlist, current_album_acoustic)

    setlist_gen.define_previous_songs_setlist_length(
        previous_albums_setlist, current_album_setlist)

    finished_setlist = setlist_gen.merge_setlists(
            current_album_setlist, previous_albums_setlist, acoustic_setlist)

    print(current_album_setlist)
    print(previous_albums_setlist)
    print(acoustic_setlist)
    print(len(current_album_setlist))
    print(len(previous_albums_setlist))
    print(finished_setlist)


if __name__ == "__main__":
    main()
