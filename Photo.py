class Photo(object):
    def __init__(self, photo_id: int, orientation: str, number_of_tags: int, tags: set):
        self.id = photo_id
        self.orientation = orientation
        self.number_of_tags = number_of_tags
        self.tags = tags
