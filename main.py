# from ner1 import get_entity
from ner2 import RobertaNER
from read_data import get_data


def get_paras():
    return get_data()


def get_names(model, num):
    try:
        text = get_data()[num]
    except Exception as e:
        return e
    names = []
    try:
        ners = model.get_entity(text=text)
        for ner in ners:
            if ner[0] == 'PER':
                names.append(ner[1])
    except Exception as e:
        return e
    return set(names)


def get_places(model, num):
    try:
        text = get_data()[num]
    except Exception as e:
        return e
    places = []
    try:
        ners = model.get_entity(text=text)
        for ner in ners:
            if ner[0] == 'LOC':
                places.append(ner[1])
    except Exception as e:
        return e
    return set(places)


if __name__ == '__main__':
    i = 1
    model = RobertaNER()
    print(get_places(model, i))
    print(get_names(model, i))
