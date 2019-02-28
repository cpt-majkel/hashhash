class Slide(object):
    def __init__(self, photos: list):
        self.photos = photos
        self.tags = set()
        for photo in photos:
            self.tags.update(photo.tags)

    def __str__(self):
        return ' '.join(map(str, self.photos))
