
def get_most_active_authors(content):
    """
    content is a list of dict has 2 keys: author and timeStamp
    """
    authors = {}
    for message in content:
        author = message["author"]
        if author in authors:
            authors[author] += 1
        else:
            authors[author] = 1

    return authors