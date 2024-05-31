class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def rightSideView(root):
    if root is None:
        return []

    queue = [root]
    result = []

    while queue:
        # Get the size of the current level
        level_size = len(queue)

        # Iterate over the current level
        for i in range(level_size):
            node = queue.pop(0)

            # If we are at the last node of the current level,
            # add it to the result
            if i == level_size - 1:
                result.append(node.data)

            # Add the left and right children of the current node to the queue
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

    return result

# Example usage:

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(rightSideView(root))