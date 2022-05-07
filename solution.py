from ner1 import get_entity
from ner2 import RobertaNER
from read_data import get_data


def get_paras() -> list:
    """
    :return: list of paragraphs in the text
    """
    return get_data()


def get_names(model: RobertaNER, num: int) -> set:
    """
    :param model: an object RobertaNER
    :param num: paragraph number from the top, 0 being the first one
    :return: set of names in the paragraph
    """
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


def get_places(model: RobertaNER, num: int) -> set:
    """
    :param model: an object RobertaNER
    :param num: paragraph number from the top, 0 being the first one
    :return: set of names of places in the paragraph
    """
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
    print("places are", get_places(model, i))
    print("names are", get_names(model, i))
