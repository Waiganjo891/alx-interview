#!/usr/bin/python3
"""
This script contains a function that calculates the
perimeter of an island in a grid. The grid is a list
of lists where 0 represents water and 1 represents land.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.
    The grid is rectangular and contains only one
    island, with no lakes inside it. Each cell
    is square and
    connected either horizontally or vertically.
    :param grid: List[List[int]] -- A rectangular grid
    of 0s and 1s
    :return: int -- The perimeter of the island
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                if r == 0 or grid[r - 1][c] == 0:
                    perimeter += 1
                if r == rows - 1 or grid[r + 1][c] == 0:
                    perimeter += 1
                if c == 0 or grid[r][c - 1] == 0:
                    perimeter += 1
                if c == cols - 1 or grid[r][c + 1] == 0:
                    perimeter += 1

    return perimeter
