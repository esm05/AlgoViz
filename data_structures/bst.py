from data_structures.node import Node
from tkinter import messagebox

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        
        if not int(value):
            messagebox.showerror("Error", "BST values must be numeric")
            return
        
        value = int(value)
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)
    
    def search(self, value):
        if not str(value).isdigit():
            return False, []
        
        value = int(value)
        return self._search_recursive(self.root, value, [])
    
    def _search_recursive(self, node, value, path):
        if node is None:
            return False, path
        
        path.append(str(node.value))
        
        if node.value == value:
            return True, path
        
        if value < node.value:
            return self._search_recursive(node.left, value, path)
        else:
            return self._search_recursive(node.right, value, path)
    
    def delete(self, value):
        if not str(value).isdigit():
            return False
        
        value = int(value)
        if self.root is None:
            return False
        
        self.root = self._delete_recursive(self.root, value)
        return True
    
    def _delete_recursive(self, node, value):
        if node is None:
            return None
        
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Node with two children
            # Get the inorder successor (smallest in the right subtree)
            temp = self._min_value_node(node.right)
            node.value = temp.value
            node.right = self._delete_recursive(node.right, temp.value)
        
        return node
    
    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current