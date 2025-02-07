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
def main():
    list = [5,6,1,3,4]
    print(bubblesort(list))
    list = [-1,5,6,1,2]
    print(bubblesort(list))
main()
