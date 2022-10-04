def sum_array(arr):
    if (arr):
        
        if (len(arr) < 3):
            return 0
            
        return sum(sorted(arr)[1:-1])
    
    else:
        return 0