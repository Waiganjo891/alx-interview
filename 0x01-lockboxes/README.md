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
