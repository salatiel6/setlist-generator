from controllers import albums, SetlistGen


def main():
    setlist_gen = SetlistGen()
    opening = "whispers in the dark"
    closure = "the final episode"
    setlist = setlist_gen.current_album_setlist(
        albums.EMPTY_OCEAN, opening, closure)

    albums_list = [albums.BLOOD_SHOT_EYES, albums.GOING_INSANE,
                   albums.NOTHING_TO_SAY, albums.BREATH_ONCE_MORE]
    previous_albuns_setlist = []

    for album in albums_list:
        previous_albuns_setlist.append(setlist_gen.get_album_setlist(album))

    acoustic_list = [
        d for lst in previous_albuns_setlist for d in lst
        if d.get("acoustic")]
    non_acoustic_list = [d for lst in previous_albuns_setlist for d in lst
                         if not d.get("acoustic")]

    print(setlist)
    print(previous_albuns_setlist)
    print(acoustic_list)
    print(non_acoustic_list)


if __name__ == "__main__":
    main()
