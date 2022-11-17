def abbrev_name(name):
    result = name[0].upper() + "."
    n= 0
    for x in name:
        if x == " ":
            n += 1
            return result + name[n].upper()
        else:
            n+= 1
    return 0