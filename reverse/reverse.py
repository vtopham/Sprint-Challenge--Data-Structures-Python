class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        #In case we're given something empty
        if node == None:
            return node
        #This is the new head
        if node.next_node == None:
            self.head = node
            return node
        #get the last node by recursively calling itself, as the recursion unfolds the node will move
        lastNode = self.reverse_list(node.get_next(), None)
        #move the current node to the right of the last node
        lastNode.next_node = node
        #now that the current node is the tail, it should point to None
        node.next_node = None
        #now that the current node is the tail, return it
        return node
