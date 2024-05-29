## cycle sort

def cyclesort(array):
    i = 0
    while i < len(array):
        if array[i] == i+1:
            i = i+1
        else:
            temp = array[i]
            array[i] = array[temp-1]
            array[temp-1] = temp

    return array
array = [3,1,5,4,2]
print(cyclesort(array))