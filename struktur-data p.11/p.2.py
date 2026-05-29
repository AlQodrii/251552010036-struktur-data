class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = BinaryNode("A")
root.left = BinaryNode("B")
root.right = BinaryNode("C")
root.left.left = BinaryNode("D")
root.left.right = BinaryNode("E")

def preorder_(node):
    if node:
        print(node.value, end=" ")
        preorder_(node.left)
        preorder_(node.right)

print("Binary Tree - Preorder Traversal:") 
preorder_(root)