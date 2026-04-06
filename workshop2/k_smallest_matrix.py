def kth_smallest(matrix: list[list[int]], k: int) -> int:
    n = len(matrix)

    low = matrix[0][0]
    high = matrix[n - 1][n - 1]

    while low < high:
        mid = (low + high) // 2

        row = n - 1
        col = 0
        count = 0

        while row >= 0 and col < n:
            if matrix[row][col] <= mid:
                count += row + 1
                col += 1
            else:
                row -= 1

        if count < k:
            low = mid + 1
        else:
            high = mid

    return low

matrix = [
    [1, 5, 9, 11],
    [2, 6, 10, 12],
    [3, 7, 13, 14],
    [4, 8, 15, 16]
]

print(kth_smallest(matrix, 7))
