import wikipedia


def wiki(name="Kanban", length=3):
    "'This is a wikipedia reader'"
    my_wiki = wikipedia.summary(name, length)
    return my_wiki
