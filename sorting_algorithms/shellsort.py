def shellsort(list):
    interval = len(list)//2
    while interval > 0:
        for i in range(interval, len(list)):
            temp = int(list[i])
            j = i
            while j >= interval and int(list[j-interval]) > temp:
                list[j] = list[j-interval]
                j -= interval
            list[j] = temp
        interval = interval//2
    return list