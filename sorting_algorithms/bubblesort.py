def bubblesort(list):
    for i in range(len(list)):
        swapped = False
        for j in range(len(list)-i-1):
            if int(list[j]) > int(list[j+1]):
                list[j], list[j+1] = list[j+1], list[j]
                swapped = True
        if not swapped:
            break
    return list