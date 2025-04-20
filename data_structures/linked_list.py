from data_structures.node import Node

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def insert_at_index(self, index, value):
        if index < 0:
            return False
        
        if index == 0:
            self.insert_at_beginning(value)
            return True
        
        current = self.head
        pos = 0
        
        while current and pos < index - 1:
            current = current.next
            pos += 1
        
        if current is None:
            return False
        
        new_node = Node(value)
        new_node.next = current.next
        current.next = new_node
        return True
    
    def delete_node(self, value):
        if self.head is None:
            return False
        
        if self.head.value == value:
            self.head = self.head.next
            return True
        
        prev = self.head
        current = self.head.next
        
        while current:
            if current.value == value:
                prev.next = current.next
                return True
            prev = current
            current = current.next
        
        return False
    
    def search(self, value):
        current = self.head
        index = 0
        
        while current:
            if current.value == value:
                return True, index
            current = current.next
            index += 1
        
        return False, -1