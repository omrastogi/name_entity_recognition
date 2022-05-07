def get_data():
    story, para, lines = [], "", [i.strip('\n') for i in open('text.txt')]
    for line in lines:
        if line == "":
            story += [para]
            para = ""
        para += line + " "

    return story