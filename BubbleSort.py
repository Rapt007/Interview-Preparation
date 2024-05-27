## Algorithm where we compare adjacent elements
def bubblesort(array):

    for i in range(0, len(array)-1):
        swap = False
        for j in range(i, len(array)):
            if array[j] < array[j-1]:
                temp = array[j]
                array[j] = array[j-1]
                array[j-1] = temp
                swap = True

        if swap is False:
            return array

bubble_arr = [3,1,5,4,2]
print(bubblesort(bubble_arr))
