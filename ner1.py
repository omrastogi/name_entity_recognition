import en_core_web_sm

nlp = en_core_web_sm.load()


def get_entity(txt):
    doc = nlp(txt)
    ner = [(X.text, X.label_) for X in doc.ents]
    return ner