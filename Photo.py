class Photo(object):
    def __init__(self, orientation: str, number_of_tags: int, tags: set):
        self.orientation = orientation
        self.number_of_tags = number_of_tags
        self.tags = tags
