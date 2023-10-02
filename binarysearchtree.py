# Binary search tree using python

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return TreeNode(key)
        else:
            if key < root.val:
                root.left = self.insert(root.left, key)
            else:
                root.right = self.insert(root.right, key)
        return root

    def search(self, root, key):
        if root is None or root.val == key:
            return root
        if root.val < key:
            return self.search(root.right, key)
        return self.search(root.left, key)

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.val, end=" ")
            self.inorder_traversal(root.right)

# Example usage:
bst = BinarySearchTree()
root = None
keys = [50, 30, 20, 40, 70, 60, 80]

for key in keys:
    root = bst.insert(root, key)

# Perform an inorder traversal to print the elements in sorted order
print("Inorder Traversal:")
bst.inorder_traversal(root)

# Search for an element in the BST
search_key = 60
result = bst.search(root, search_key)
if result:
    print(f"\n{search_key} found in the BST.")
else:
    print(f"\n{search_key} not found in the BST.")
