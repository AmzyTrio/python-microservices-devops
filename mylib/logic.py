import wikipedia


def wiki(name="Kanban", length=3):
    my_wiki = wikipedia.summary(name, length)
    return my_wiki
