"""Given an m x n matrix,
return all elements of the matrix in spiral order."""


def spiral_order(matrix):
    """Given an m x n matrix,
    return all elements of the matrix in spiral order."""
    m = len(matrix)
    n = len(matrix[0])
    # Initialize variables to keep track of row and column indexes
    top = 0
    bottom = m - 1
    left = 0
    right = n - 1

    # Initialize list to store the elements in spiral order
    spiral = []

    # Loop until all elements in the matrix have been added to the list
    while len(spiral) < m * n:
        # Add elements from the top row to the list
        for i in range(left, right + 1):
            spiral.append(matrix[top][i])
        top += 1

        # Add elements from the right column to the list
        for i in range(top, bottom + 1):
            spiral.append(matrix[i][right])
        right -= 1

        # Add elements from the bottom row to the list
        for i in range(right, left - 1, -1):
            spiral.append(matrix[bottom][i])
        bottom -= 1

        # Add elements from the left column to the list
        for i in range(bottom, top - 1, -1):
            spiral.append(matrix[i][left])
        left += 1

    return spiral


def spiral_order2(matrix):
    """Given an m x n matrix,
    return all elements of the matrix in spiral order."""
    if not matrix:
        return []

    m, n = len(matrix), len(matrix[0])
    left, right, top, bottom = 0, n - 1, 0, m - 1
    direction = 0
    spiral = []

    while left <= right and top <= bottom:
        if direction == 0:
            # Add elements from the top row to the list
            for i in range(left, right + 1):
                spiral.append(matrix[top][i])
            top += 1
        elif direction == 1:
            # Add elements from the right column to the list
            for i in range(top, bottom + 1):
                spiral.append(matrix[i][right])
            right -= 1
        elif direction == 2:
            # Add elements from the bottom row to the list
            for i in range(right, left - 1, -1):
                spiral.append(matrix[bottom][i])
            bottom -= 1
        elif direction == 3:
            # Add elements from the left column to the list
            for i in range(bottom, top - 1, -1):
                spiral.append(matrix[i][left])
            left += 1

        direction = (direction + 1) % 4

    return spiral


def spiral_order3(matrix):
    if not matrix:
        return []
    m, n = len(matrix), len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    curr_dir = 0
    curr_pos = (0, 0)
    visited = set()
    result = []

    while len(visited) < m * n:
        dx, dy = directions[curr_dir]
        new_pos = (curr_pos[0] + dx, curr_pos[1] + dy)

        if not (0 <= new_pos[0] < m and 0 <= new_pos[1] < n) or new_pos in visited:
            curr_dir = (curr_dir + 1) % 4
            dx, dy = directions[curr_dir]
            new_pos = (curr_pos[0] + dx, curr_pos[1] + dy)

        curr_pos = new_pos
        visited.add(curr_pos)
        result.append(matrix[curr_pos[0]][curr_pos[1]])

    return result


if __name__ == "__main__":
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(spiral_order(matrix))
    print(spiral_order2(matrix))
    print(spiral_order3(matrix))
