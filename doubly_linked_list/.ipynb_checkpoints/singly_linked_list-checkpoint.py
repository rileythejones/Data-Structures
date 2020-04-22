class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.next = next

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

class SinglyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = self.tail = new_node 
        else:
            new_node.next = self.head
            self.head.prev = new_node 
            self.head = new_node 

    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value 

    def move_to_front(self, node):
        if node is self.head:
            return 
        self.add_to_head(node.value)
        self.delete(node)

    def delete(self, node):
        self.length -= 1 
        if self.head is self.tail: 
            self.head = self.tail = None
        elif node is self.head:
            self.head = node.next
            node.delete()
        elif node is self.tail:
            self.tail = node.next
            node.delete()
        else:
            node.delete()
        
