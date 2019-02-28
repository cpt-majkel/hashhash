from Photo import Photo


def fetch_photos(input_filepath: str):
    with open(input_filepath, 'r') as input_file:
        number_of_photos = int(input_file.readline().strip())
        for photo_id in range(number_of_photos):
            orientation, number_of_tags, *tags = input_file.readline().strip().split(" ")
            yield Photo(photo_id=photo_id,
                        orientation=orientation,
                        number_of_tags=int(number_of_tags),
                        tags=set(tags))


def total_score(slides):
    result = 0
    for s1, s2 in zip(slides[:-1], slides[1:]):
        result += transition_score(s1, s2)
    return result


def transition_score(s1, s2):
    union = len(s1.tags.union(s2.tags))
    difference1 = len(s1.tags - s2.tags)
    difference2 = len(s2.tags - s1.tags)
    return min(union, difference1, difference2)
