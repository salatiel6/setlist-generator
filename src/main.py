import logging

from controllers import albums, setlist_gen
from logzero import setup_logger

logfile = './logs/application.log'
log = setup_logger(
    name="Setlist Generator",
    level=logging.DEBUG,
    logfile=logfile,
    maxBytes=1024000,
    backupCount=4
)


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
    # Log the start of the function
    log.info('Starting main() function')

    # Call define_current_album() function and log the result
    current_album_setlist, current_album_acoustic = define_current_album()
    log.debug(f'Current album setlist: {current_album_setlist}')
    log.debug(f'Current album acoustic: {current_album_acoustic}')

    # Call define_previous_albums() function and log the result
    gross_setlist = define_previous_albums()
    log.debug(f'Gross setlist: {gross_setlist}')

    # Call split_previous_songs() function and log the result
    previous_albums_setlist, acoustic_setlist = \
        setlist_gen.split_previous_songs(gross_setlist, current_album_acoustic)
    log.debug(f'Previous albums setlist: {previous_albums_setlist}')
    log.debug(f'Acoustic setlist: {acoustic_setlist}')

    # Call define_previous_songs_setlist_length() function and log the result
    setlist_gen.define_previous_songs_setlist_length(
        previous_albums_setlist, current_album_setlist)
    log.info('Setlist length defined')

    # Call merge_setlists() function and log the result
    finished_setlist = setlist_gen.merge_setlists(
            current_album_setlist, previous_albums_setlist, acoustic_setlist)
    log.debug(f'Finished setlist: {finished_setlist}')

    # Log the end of the function
    log.info('Finished main() function')

    print(len(finished_setlist))


if __name__ == "__main__":
    main()
