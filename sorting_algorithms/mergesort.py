def mergesort(list):
    if(len(list) <= 1):
        return list
    half = len(list)//2
    list1, list2 = mergesort(list[:half]), mergesort(list[half:])
    return merge(list1,list2)
def merge(left, right):
    new_list = []
    i, j = 0, 0
    print(left, right)
    while i < len(left) and j < len(right):
        if int(left[i]) <= int(right[j]):
            new_list.append(left[i])
            i += 1
        else:
            new_list.append(right[j])
            j += 1
    if i < len(left):
        new_list += left[i:]
    if j < len(right):
        new_list += right[j:]

    return new_list
def main():
    print(mergesort([-1,0,156,-100,6,1,3,5]))
    print(mergesort([-1]))
main()