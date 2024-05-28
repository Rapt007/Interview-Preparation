## Insertion Sort

def insertionsort(array):
    for i in range(0, len(array)-1):
        for j in range(i+1, 0, -1):
            if array[j] < array[j-1]:
                temp = array[j]
                array[j] = array[j-1]
                array[j-1] = temp
            else:
                break

    return array
array = [3,1,5,4,2]
print(insertionsort(array))