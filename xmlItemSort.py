def itemSort(parent, childName):
    data = []
    for elem in parent:
        key = elem.findtext(childName)
        data.append((key, elem))
    data.sort(key = lambda x: x[0])
    parent[:] = [item[-1] for item in data]
    return parent
