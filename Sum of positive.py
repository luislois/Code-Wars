def positive_sum(arr):
    if (arr):
        sum = 0
        for x in arr:
            if (x > 0):
                sum += x

        return sum
        
    else:
        return 0