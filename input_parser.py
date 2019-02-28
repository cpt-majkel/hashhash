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
