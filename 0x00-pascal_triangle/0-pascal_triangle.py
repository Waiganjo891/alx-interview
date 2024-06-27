#!/usr/bin/python3
"""
This code will generate Pascal's Triangle up to the n-th row,
ensuring the correct structure and values as demonstrated in the test script.
"""


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            row = [1]
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
            triangle.append(row)

    return triangle


if __name__ == "__main__":
    from pprint import pprint
    pprint(pascal_triangle(5))
