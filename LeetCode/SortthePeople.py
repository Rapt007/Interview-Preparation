def sortPeople(names, heights):
    diction = dict(zip(heights, names))
    sorted_list = []
    for i in range(0, len(heights)):
        swap = False
        for j in range(1, len(heights) - i):
            if heights[j] > heights[j - 1]:
                swap = True
                temp = heights[j]
                heights[j] = heights[j - 1]
                heights[j - 1] = temp

        if swap is False:
            for i in heights:
                sorted_list.append(diction[i])
            return sorted_list

    for i in heights:
        sorted_list.append(diction[i])
    return sorted_list

heights = [180,165,170]
names = ['Mary', 'Joh', 'Aman']
print(sortPeople(names, heights))
