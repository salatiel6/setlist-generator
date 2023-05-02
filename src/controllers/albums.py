from .db_connect import db


class Albums:
    def __init__(self):
        self.album_names = [
            "blood_shot_eyes",
            "going_insane",
            "nothing_to_say",
            "breath_once_more",
            "empty_ocean"
        ]

        for album_name in self.album_names:
            setattr(self, album_name.upper(), self.get_album(album_name))

    @staticmethod
    def get_album(album):
        return db[album].find()


albums = Albums()
