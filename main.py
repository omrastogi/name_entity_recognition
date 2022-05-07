# from ner1 import get_entity
from ner2 import get_entity
from read_data import get_data


def get_paras():
    return get_data()


def get_names(num):
    try:
        text = get_data()[num]
    except Exception as e:
        print(e)
    names = []
    try:
        ners = get_entity(text)
        for ner in ners:
            if ner[0] == 'PER':
                names.append(ner[1])
    except Exception as e:
        print(e)
    return names


def get_places(num):
    try:
        text = get_data()[num]
    except Exception as e:
        print(e)
    places = []
    try:
        ners = get_entity(text)
        for ner in ners:
            if ner[0] == 'LOC':
                places.append(ner[1])
    except Exception as e:
        print(e)
    return places


if __name__ == '__main__':
    i = 1
    print(get_places(i))
    print(get_names(i))
