# Find Smallest Letter Greater Than Target

letters = ["c", "f", "j"]
target = "a"

def nextGreatestLetter(letters, target):
    start, end = 0, len(letters) - 1

    if target >= letters[end]:
        return letters[0]

    while start <= end:
        mid = start + int((end - start) / 2)
        if target >= letters[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return letters[start]

letter = nextGreatestLetter(letters, target)
print('next Greatest Letter: ' + str(letter))
