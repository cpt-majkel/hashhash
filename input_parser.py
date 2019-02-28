from Photo import Photo
from Slide import Slide
from random import shuffle


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


def save_to_output_file(output_filepath, slides):
    with open(output_filepath, 'w') as output_file:
        output_file.write('{}\n'.format(len(slides)))
        output_file.writelines('\n'.join(map(str, slides)))


if __name__ == '__main__':
    photos = list(fetch_photos('inputs/b_lovely_landscapes.txt'))
    horizontal = [p for p in photos if p.orientation == 'H']
    vertical = [p for p in photos if p.orientation == 'V']
    slides_horizontal = [Slide([h]) for h in horizontal]
    best = 0

    for i in range(10):
        shuffle(vertical)
        slides_vertical = [Slide([v1, v2]) for v1, v2 in zip(vertical[::2], vertical[1::2])]
        slides = slides_horizontal + slides_vertical
        shuffle(slides)
        solution = total_score(slides)
        print(solution)
        if solution > best:
            best = solution
            best_vertical = list(vertical)
            best_slides = list(slides)

    print(best)
    print(total_score(slides))
    save_to_output_file('inputs/output.txt', slides)
