from Photo import Photo


def fetch_photos(input_filepath: str):
    with open(input_filepath, 'r') as input_file:
        _ = input_file.readline()
        for line in input_file:
            orientation, number_of_tags, *tags = line.strip('\n').split(" ")
            yield Photo(orientation=orientation,
                        number_of_tags=number_of_tags,
                        tags=set(tags))
