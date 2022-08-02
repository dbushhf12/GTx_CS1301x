class LinkedListNode:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node
        
#Write your function here!
def linked_list_search(node, term):
    while node.next_node:
        if node.value == term:
            return True
        else:
            return linked_list_search(node.next_node, term)
    return False
    
node_7 = LinkedListNode(5)
node_6 = LinkedListNode(2, node_7)
node_5 = LinkedListNode(9, node_6)
node_4 = LinkedListNode(1, node_5)
node_3 = LinkedListNode(4, node_4)
node_2 = LinkedListNode(6, node_3)
root_node = LinkedListNode(7, node_2)

print(linked_list_search(root_node, 9))
print(linked_list_search(root_node, 3))        
