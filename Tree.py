class Node_tree:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __str__(self):
        return "(%s %s %s)" % (self.left or "", self.key, self.right or "")


def insert(tree, key):
    if not tree:
        tree = Node_tree(key)
    elif key < tree.key:
        tree = Node_tree(tree.key, insert(tree.left, key), tree.right)
    elif key > tree.key:
        tree = Node_tree(tree.key, tree.left, insert(tree.right, key))
    else:
        tree = Node_tree(tree.key, tree.left, insert(tree.right, key))
    return tree

def postorder(tree, temp):
    if tree:
        if(tree.left!=None):
            postorder(tree.left, temp)
        if(tree.right!=None):
           postorder(tree.right, temp)
        temp.append(tree.key)