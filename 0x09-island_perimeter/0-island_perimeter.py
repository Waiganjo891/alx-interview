#!/usr/bin/env python3
"""
This module contains a function to compute the
perimeter of an island given a grid where 1 represents
land and 0 represents water.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island in the grid.
    The grid is a list of lists of integers:
    - 0 represents water
    - 1 represents land
    Each cell is square with a side length of 1.
    The island is connected horizontally/vertically
    The grid is completely surrounded by water.
    There is only one island (or nothing).
    Args:
        grid (list of list of int): The grid representing
        the island and water.
    Returns:
        int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4

                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 1
                if r < rows - 1 and grid[r + 1][c] == 1:
                    perimeter -= 1
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 1
                if c < cols - 1 and grid[r][c + 1] == 1:
                    perimeter -= 1
    return perimeter
