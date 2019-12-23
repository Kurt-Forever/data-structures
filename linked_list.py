# A simple Python program for traversal of a linked list

# Node class
class Node:
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # This function prints contents of linked list
    # starting from head
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def create_list_from_array(self, a):
        current_node = None
        for i in a:
            node = Node(i)
            if self.head is None:
                self.head = node
            else:
                current_node.next = node
            current_node = node


# Code execution starts here
if __name__ == '__main__':

    # Start with the empty list
    llist = LinkedList()
    a = [3, 4, 7, 9, 12]
    llist.create_list_from_array(a)

    llist.print_list()
