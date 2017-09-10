"""
 Insert a node into a sorted doubly linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list
"""
def SortedInsert(head, data):
    new_node = Node()
    new_node.data = data

    if head == None:
        return new_node
    elif data <= head.data:
        new_node.next = head
        head.prev=new_node
        return new_node
    else:
        rest = SortedInsert(head.next,data)
        head.next = rest
        rest.prev = head
        return head
