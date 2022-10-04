def past(h, m, s):
    if (0 >= h >= 23 or 0 >= m >= 59 or 0 >= s >= 59
):
        return 0
    
    midnight_h = 0
    midnight_m = 0
    midnight_s = 0
    
    h1 = (h - midnight_h) * 3600
    m1 = (m - midnight_m) * 60
    s1 = s - midnight_s
    
    return (h1 + m1 + s1) * 1000