class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def max_sum_bst(root):
    if root is None:
        return 0

    left_sum = max_sum_bst(root.left)
    right_sum = max_sum_bst(root.right)

    max_sum = max(left_sum, right_sum) + root.data

    return max_sum

# Example usage:

root = Node(10)
root.left = Node(5)
root.right = Node(15)

max_sum = max_sum_bst(root)

print(max_sum)