def reverse_seq(n):
    arr = []
    for x in range(1, n+1):
        arr.append(x)
    
    return sorted(arr, reverse=True)