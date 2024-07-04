Lockboxes
Explanation:
Initialization:

n is the total number of boxes.
visited is a set to track boxes that have been opened.
stack is initialized with the first box (index 0).
Traversal:

While the stack is not empty, pop a box from the stack.
If the box is not in visited, add it to visited.
Iterate over all keys in the current box. If a key corresponds to a box that hasn't been visited and is within the range of existing boxes, add it to the stack.
Result:

After the traversal, check if the number of visited boxes is equal to the total number of boxes (n). If so, return True; otherwise, return False.

You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False
carrie@ubuntu:~/0x01-lockboxes$ cat main_0.py
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))

carrie@ubuntu:~/0x01-lockboxes$
carrie@ubuntu:~/0x01-lockboxes$ ./main_0.py
True
True
False
carrie@ubuntu:~/0x01-lockboxes$
Repo:

GitHub repository: alx-interview
Directory: 0x01-lockboxes
File: 0-lockboxes.py
