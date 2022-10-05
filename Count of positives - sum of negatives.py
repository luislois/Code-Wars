def count_positives_sum_negatives(arr):
    result = []
    if (arr):
        count = 0
        sum = 0
        for x in arr:
            if (x > 0):
                count += 1
            else:
                sum += x
        result.append(count)
        result.append(sum)
        return result
    else:
        return result