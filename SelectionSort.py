## As the name suggest select the highest number or lowest number and place it at their respective index.
def selectionsort(array):
    for i in range(0, len(array)):
        last = len(array)-i-1
        print(last)
        maxi = 0
        for j in range(0, last+1):
            if array[j] > array[maxi]:
                maxi = j
        print(array)
        print(maxi)
        temp = array[last]
        array[last] = array[maxi]
        array[maxi] = temp
        print(array)
    return array



select_arr = [1,-1]
print(selectionsort(select_arr))
