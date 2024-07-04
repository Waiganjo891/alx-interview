#!/usr/bin/python3


def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked.
    Args:
        boxes (list of list of int): List of boxes with keys.
    Returns:
        bool: True if all boxes can be opened, else False.
    """
    n = len(boxes)
    visited = set()
    stack = [0]

    while stack:
        current_box = stack.pop()
        if current_box not in visited:
            visited.add(current_box)
            for key in boxes[current_box]:
                if key not in visited and key < n:
                    stack.append(key)

    return len(visited) == n


if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))
