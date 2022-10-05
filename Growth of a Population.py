def nb_year(p0, percent, aug, p):
    t = 0
    while p0 < p:
        p0 = int(p0*(1 + percent/100)) + aug  # If i dont round this, it dont pass 1 basic test
        t += 1
    return t