# linked_list_examples.py

# Example: Finding an element in the linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def find(self, key):
        curr = self.head
        while curr:
            if curr.data == key:
                return True
            curr = curr.next
        return False

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

# Test the implementation
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
print(ll.find(2))  # Output: True
print(ll.find(4))  # Output: False
ll.print_list()    # Output: 1 -> 2 -> 3 -> None
