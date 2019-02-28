class Slide(object):
    def __init__(self, photos: list):
        self.photos = photos
        self.tags = set()
        for photo in photos:
            self.tags.update(photo.tags)
