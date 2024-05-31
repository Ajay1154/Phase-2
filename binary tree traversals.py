class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None
 
 
def printPreorder(root):
    if root == None:
        return 
    # 1 
    print(root.data, end = ", ")
    # 2 
    printPreorder(root.left)
    # 3
    printPreorder(root.right)
 
 
def printInorder(root):
    if root == None:
        return 
    # 1 
    printInorder(root.left)
    # 2 
    print(root.data, end = ", ")
    # 3
    printInorder(root.right)
 
def printPostorder(root):
    if root == None:
        return 
    # 1 
    printPostorder(root.left)
    # 2 
    printPostorder(root.right)
    # 3
    print(root.data, end = ", ")