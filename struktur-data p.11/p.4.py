class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    
    def insert(self, new_key):
        if new_key < self.key:
            if self.left:
                self.left.insert(new_key)
            else:
                self.left = BSTNode(new_key)
        elif new_key > self.key:
            if self.right:
                self.right.insert(new_key)
            else:
                self.right = BSTNode(new_key)

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.key, end=" ")
        if self.right:
            self.right.inorder()

bst = BSTNode(50)
for value in [30, 70, 20, 40, 60, 80]:
    bst.insert(value)

print("\nBinary Search Tree - Inorder Traversal:")
bst.inorder()