class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.insert(0, item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def get_items(self):
        return self.items