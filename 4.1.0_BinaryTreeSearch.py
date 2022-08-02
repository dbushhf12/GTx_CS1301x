class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right


def binary_tree_search(node, value):
    if node.value == value:
        return True
    elif value < node.value:
        try:
            return binary_tree_search(node.left, value)
        except:
            return False    
    elif value > node.value:
        try:
            return binary_tree_search(node.right, value)
        except:
            return False

    


            

root_node = Node(10)
root_node.left = Node(5)
root_node.right = Node(15)
root_node.left.left = Node(3)
root_node.left.right = Node(7)
root_node.right.left = Node(12)
root_node.right.right = Node(18)

print(binary_tree_search(root_node, 22))
