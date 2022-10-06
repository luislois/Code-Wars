def clean_string(s):
    result = ""
    for x in s:
        if x=='#':
            result = result[:-1]
        else:
            result += x
        
    return result