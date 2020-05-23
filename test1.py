def binary_search(a, val):
    start = 0
    end = len(a)- 1 

    print ("start", start, "end", end)
    while start <= end:
        mid = (end + start ) // 2
        print ("mid:", mid)

        if (a[mid]== val):
            return mid
        elif val > a[mid]:
            start = mid + 1
        else:
            end = mid - 1
    
    return -1 # I can't find

d = [1, 3, 5, 7, 9, 11, 14, 20, 22, 23, 30, 33]
print(binary_search(d, 20))
