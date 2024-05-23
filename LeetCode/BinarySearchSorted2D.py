## if it is a sorted 2D matrix
def searchMatrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])
    start, end = 0, rows * cols - 1

    while start <= end:
        mid = start + (end - start) // 2
        mid_row, mid_col = mid // cols, mid % cols
        print(mid, mid_row, mid_col)

        if target == matrix[mid_row][mid_col]:
            return True
        elif target > matrix[mid_row][mid_col]:
            start = mid + 1
        else:
            end = mid - 1

    return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
print(searchMatrix(matrix, target))