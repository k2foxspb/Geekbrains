

def thesaurus(*args):
    first_w = {}
    for name in args:
        if name[0] not in first_w:
            first_w[name[0]] = [name]
        else:
            first_w[name[0]].append(name)
    return first_w

x= thesaurus('Иван', 'Мария', 'Никита', 'Николай')
print(x)