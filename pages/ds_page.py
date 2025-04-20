from tkinter import *
from tkinter import ttk, messagebox
from data_structures.bst import BST
from data_structures.stack import Stack
from data_structures.linked_list import LinkedList
from data_structures.queue import Queue

class DataStructurePage(Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent, bg="#004080")
        
        # Top frame with title
        top_frame = Frame(self, bg='#0000DC')
        top_frame.place(relwidth=0.4, relheight=0.1, relx=0.5, rely=0.0, anchor='n')
        
        # Title
        title = Label(top_frame, text="Data Structures", font=("Arial", 20, "bold"), fg='#EFEFFF', bg='#004080')
        title.place(relheight=1, relwidth=1)
        
        # Canvas frame for visualization
        c_frame = Frame(self, bg='#4242FF')
        c_frame.place(relwidth=0.7, relheight=0.7, relx=0.02, rely=0.1)
        self.ds_canvas = Canvas(c_frame, bg="white")
        self.ds_canvas.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)
        
        # UI frame for controls
        UI_frame = Frame(self, bg='#4242FF')
        UI_frame.place(relwidth=0.24, relheight=0.7, relx=0.75, rely=0.1)
        
        # Data structure selection
        self.ds_selected = StringVar()
        self.ds_combo = ttk.Combobox(UI_frame, textvariable=self.ds_selected, values=["Stack", "Queue", "Linked List", "BST"])
        self.ds_combo.grid(row=0, column=0, padx=25, pady=5)
        self.ds_combo.current(0)  # Default to Stack

        # Binding function to combo box to prevent any confusion which ds is selected 
        self.ds_combo.bind("<<ComboboxSelected>>", self.change_data_structure)
        
        # Value entry
        value_frame = Frame(UI_frame, bg='#4242FF')
        value_frame.grid(row=1, column=0, pady=5)
        Label(value_frame, text="Value:", bg='#4242FF', fg='white').grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.value_var = StringVar()
        self.value_entry = Entry(value_frame, textvariable=self.value_var, width=20)
        self.value_entry.grid(row=0, column=1)
        
        # Index entry
        index_frame = Frame(UI_frame, bg='#4242FF')
        index_frame.grid(row=2, column=0, pady=5)
        Label(index_frame, text="Index:", bg='#4242FF', fg='white').grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.index_var = StringVar()
        self.index_entry = Entry(index_frame, textvariable=self.index_var, width=20)
        self.index_entry.grid(row=0, column=1)
        
        # Operation Buttons
        # Have a placeholder name for the buttons since they will change during a data structure change 
        button_frame = Frame(UI_frame, bg='#4242FF')
        button_frame.grid(row=3, column=0, pady=10)
        
        self.insert_btn = Button(button_frame, text="Insert", command=self.insert_element, bg='#400080', fg='#E6DEFF')
        self.insert_btn.pack(fill=X, pady=2)
        
        self.delete_btn = Button(button_frame, text="Delete", command=self.delete_element, bg='#400080', fg='#E6DEFF')
        self.delete_btn.pack(fill=X, pady=2)
        
        self.search_btn = Button(button_frame, text="Search", command=self.search_element, bg='#400080', fg='#E6DEFF')
        self.search_btn.pack(fill=X, pady=2)
        
        self.insert_at_index_btn = Button(button_frame, text="Insert at Index", command=self.insert_at_index, bg='#400080', fg='#E6DEFF')
        self.insert_at_index_btn.pack(fill=X, pady=2)
        
        self.clear_btn = Button(button_frame, text="Clear", command=self.clear_all, bg='#1B003C', fg='#E6DEFF')
        self.clear_btn.pack(fill=X, pady=2)
        
        # Home button
        back_button = Button(self, text="Back to Main Menu", bg='#4242FF', fg='#EFEFFF', command=self.go_to_main_page)
        back_button.place(relx=0.1, rely=0.9, anchor='n')
        
        # Initialize data structures
        self.stack = Stack()
        self.queue = Queue()
        self.linked_list = LinkedList()
        self.bst = BST()
        self.current_ds = "Stack"
        
        # Set up initial view
        self.change_data_structure(None)

    def go_to_main_page(self):
        self.ds_canvas.delete('all')
        try:
            from pages.main_page import MainPage
            self.controller.show_page(MainPage)
        except ImportError:
            messagebox.showinfo("Info", "MainPage module not found")
    
    def change_data_structure(self, event):
        self.current_ds = self.ds_selected.get()
        self.clear_canvas()
        
        # Enable/disable appropriate buttons based on data structure
        # Also assigns appriopiate labels to the buttons 
        
        if self.current_ds == "Stack":
            self.insert_at_index_btn.config(text="     Peek      ", command=self.highlight_peek)
            self.index_entry.config(state=DISABLED)
            self.delete_btn.config(text="Pop")
            self.insert_btn.config(text="Push")
            

        elif self.current_ds == "Queue":
            self.insert_at_index_btn.config( text="Insert at Index", command=self.insert_at_index, state=DISABLED)
            self.index_entry.config(state=DISABLED)
            self.delete_btn.config(text="Dequeue")
            self.insert_btn.config(text="Enqueue")

        elif self.current_ds == "Linked List":
            self.insert_at_index_btn.config( text="Insert at Index", command=self.insert_at_index, state=NORMAL)
            self.index_entry.config(state=NORMAL)
            self.delete_btn.config(text="Delete")
            self.insert_btn.config(text="Insert at Tail")
            
        elif self.current_ds == "BST":
            self.insert_at_index_btn.config( text="Insert at Index", command=self.insert_at_index, state=DISABLED)
            self.index_entry.config(state=DISABLED)
            self.delete_btn.config(text="Delete")
            self.insert_btn.config(text="Insert")
        
        # Draw the current data structure
        self.draw_data_structure()
    
    def clear_canvas(self):
        self.ds_canvas.delete("all")
    
    def get_value(self):
         # Only accept valid integers
        try:
            value = int(self.value_var.get())
            return value
        except ValueError:
            messagebox.showerror("Error", "Value must be an integer")
            return None
    
    def get_index(self):
        # Only accept valid integers
        try:
            index = int(self.index_var.get())
            return index
        except ValueError:
            messagebox.showerror("Error", "Index must be an integer")
            return None
        
    
    def highlight_peek(self):
        if self.current_ds == "Stack":
            self.draw_data_structure(highlight_value=self.stack.peek())

    # Draw the data structure after each operation
    
    def insert_element(self):
        value = self.get_value()
        if value is None:
            return
        
        if self.current_ds == "Stack":
            self.stack.push(value)
        elif self.current_ds == "Queue":
            self.queue.enqueue(value)
        elif self.current_ds == "Linked List":
            self.linked_list.insert_at_end(value)
        elif self.current_ds == "BST":
            self.bst.insert(value)
        
        self.draw_data_structure()
        self.value_var.set("")  # Make the value entry widget empty
    
    def insert_at_index(self):
        value = self.get_value()
        index = self.get_index()
        
        if value is None or index is None:
            return
        
        if self.current_ds != "Linked List":
            messagebox.showinfo("Info", "Insert at index only supported for Linked List")
            return
        
        success = self.linked_list.insert_at_index(index, value)
        if not success:
            messagebox.showerror("Error", "Index out of range")
            return
        
        self.draw_data_structure()
        self.value_var.set("")  # Make the value entry widget empty
        self.index_var.set("")  # Make the index entry widget empty
    
    def delete_element(self):
        # Declaring items to see if the value is in the stack
        stack_items = self.stack.get_items()
        
        # If data structure empty
        if self.current_ds == "Stack":
            if self.stack.is_empty():
                messagebox.showinfo("Warning", "Stack is empty")
                return
            elif self.get_value() not in stack_items:
                messagebox.showinfo("Error", "Value not in stack. Try Again.")
            elif self.get_value() in stack_items and self.get_value() != self.stack.peek():
                messagebox.showinfo("Warning", "Value not on top. Try Again.")
            else:
                messagebox.showinfo("Info","{} popped from stack".format(self.stack.pop()))
        
        elif self.current_ds == "Queue":
            # Declaring items to see if the value is in the queue
            items = self.queue.get_items()
            # If data structure empty
            if self.queue.is_empty():
                messagebox.showinfo("Warning", "Queue is empty")
                return
            elif self.get_value() not in items:
                messagebox.showinfo("Error", "Value not in queue. Try Again.")
            else:
                messagebox.showinfo("Info","{} removed from Front".format(self.queue.dequeue()))
            
            
        
        elif self.current_ds == "Linked List":
            value = self.get_value()
            if value is None:
                return
            
            success = self.linked_list.delete_node(value)
            if not success:
                messagebox.showinfo("Error", "Value {} not found".format(value))
                return
        
        elif self.current_ds == "BST":
            value = self.get_value()
            if value is None:
                return
            
            success = self.bst.delete(value)
            if not success:
                messagebox.showinfo("Error", "Value {} not found or BST is empty".format(value))
                return
        
        self.draw_data_structure()
        self.value_var.set("")  # Make the entry empty
    
    def search_element(self):
        value = self.get_value()
        if value is None:
            return
        
        success = False
        message = ""
        
        # If the element and index are found alert the user, if the operation succeded flip a boolean
        # And alert the user if the method did not find a value
        if self.current_ds == "Stack":
            items = self.stack.get_items()
            if value in items:
                index = items.index(value)
                success = True
                message = "Found {} at position {} from top".format(value, len(items)-index-1)
        
        elif self.current_ds == "Queue":
            items = self.queue.get_items()
            if value in items:
                index = items.index(value)
                success = True
                message = "Found {} at position {} from Front".format(value, index)
        
        elif self.current_ds == "Linked List":
            success, index = self.linked_list.search(value)
            if success:
                message = "Found {} at index {}".format(value, index)
        
        elif self.current_ds == "BST":
            success, path = self.bst.search(value)
            if success:
                message = "Found {} in BST. Path: {}".format(value,' -> '.join(path))
        
        if not success:
            messagebox.showinfo("Search Result", "Value {} not found".format(value))
        else:
            messagebox.showinfo("Search Result", message)
            # Highlight the found element
            self.draw_data_structure(highlight_value=value)
        
        self.value_var.set("")  # Clear the entry
    
    def clear_all(self):
        self.stack = Stack()
        self.queue = Queue()
        self.linked_list = LinkedList()
        self.bst = BST()
        self.clear_canvas()
        self.value_var.set("")
        self.index_var.set("")
    
    def draw_data_structure(self, highlight_value=None):
        self.clear_canvas()
        
        if self.current_ds == "Stack":
            self.draw_stack(highlight_value)
        elif self.current_ds == "Queue":
            self.draw_queue(highlight_value)
        elif self.current_ds == "Linked List":
            self.draw_linked_list(highlight_value)
        elif self.current_ds == "BST":
            self.draw_bst(highlight_value)

    """ Visualizer for the Stack Data Structure 

            Stack is drawn vertically with the top of the stack at the top of the data structure
            when the user enters a value it is inserted to the top of the stack following LIFO (Last-In First-Out).
            Each element is represented by a rectangle.
    """

    def draw_stack(self, highlight_value=None):
        # Get all elements from the stack
        items = self.stack.get_items()
        if not items:
            self.ds_canvas.create_text(250, 150, text="Stack is empty", font=("Arial", 16))
            return
        
        # Dimensions for each rectangle
        box_height = 40
        box_width = 150

        # Starting position of intial value or first rectangle of the stack
        start_y = 400
        
        # Display Stack in LIFO order
        for i, item in enumerate(reversed(items)):
            y = start_y - i * box_height
            
            # Determine color based on highlight
            if item == highlight_value:
                box_color = "#FFD700" 
            else: 
                box_color = "#87CEEB"
            
            # Draw the box 
            # left, top, right, bottom side of rectangle
            self.ds_canvas.create_rectangle(
                175, y - box_height,        # Top left corner
                175 + box_width, y,         # Top right corner
                fill=box_color, outline="black"
            )
            
            # Add the text
            self.ds_canvas.create_text(
                175 + box_width/2,  # Horizontal center
                y - box_height/2,   # Vertical center
                text=item, font=("Arial", 12)
            )
        
        # Add stack labels
        # put "Bottom" label a little under the intial y value
        # put in the middle of a rectangle
        self.ds_canvas.create_text(175 + box_width/2, 420, text="Bottom", font=("Arial", 10))

        # Only show the top label when there are more than 0 elements
        # Put in the middle of the rectangle by using it's vertical center and horizontal center
        if len(items) > 0:
            self.ds_canvas.create_text(
                (175 + box_width/2) - 120, 
                start_y - (len(items)-1) * box_height - box_height/2, 
                text="Top", font=("Arial Bold", 13)
            )
    
    """ Visualizer for the Queue Data Structure 

            Queue is drawn horizontally with the FRont on the left most side of the drawing and the end of the queue closer right side.
            When the user enters a value it is inserted into the end of the queue following FIFO (First-In First-Out).
            Each element is represented by a rectangle.
    """
    def draw_queue(self, highlight_value=None):
        # Retrieve all elements from queue
        items = self.queue.get_items()
        if not items:
            self.ds_canvas.create_text(250, 150, text="Queue is empty", font=("Arial", 16))
            return
        
        # Dimensions of each element rectangle
        box_height = 40
        box_width = 60

        # Starting location of intial rectangle or the Front
        start_x = 50
        y = 150
        
        # Display items in FIFO order
        for i, item in enumerate(items):
            x = start_x + i * box_width
            
           # Determine color based on highlight
            if item == highlight_value:
                box_color = "#FFD700" 
            else: 
                box_color = "#87CEEB"
            
            # Draw the box
            # left, top, right, bottom side of rectangle
            self.ds_canvas.create_rectangle(
                x, y - box_height/2,            # Top left corner
                x + box_width, y + box_height/2,  # Bottom right corner
                fill=box_color, outline="black"
            )
            
            # Add the text
            self.ds_canvas.create_text(
                x + box_width/2, y, 
                text=item, font=("Arial", 12)
            )
        
        # Add Front label
        self.ds_canvas.create_text(start_x + box_width/2, y + box_height, text="Front", font=("Arial", 10))
        
    """ Visualizer for the Linked List Data Structure 

            Shows a singly Linked List as the drawing on the canvas.
            Data structure is drawn horizontally with the head on the leftmost side of the canvas,
            and if there are any more nodes they're connected with arrows pointing to the next one.
            Each node is a circle. 
    """
    def draw_linked_list(self, highlight_value=None):
        if self.linked_list.head is None:
            self.ds_canvas.create_text(250, 150, text="Linked List is empty", font=("Arial", 16))
            return
        
        # Dimensions of each element's node
        node_radius = 25
        spacing = 80

        # Starting location of head
        start_x = 50
        y = 150
        
        curr = self.linked_list.head
        ll_len = 0
        i = 0
        
        self.ds_canvas.create_text(start_x, y - 40, text="Head", font=("Arial", 10))
        # Traverse through linked list until None is reached 
        while curr:
            # Calculate horizontal position for curr node
            x = start_x + i * spacing
            
            # Determine color based on highlight
            if curr.value == highlight_value:
                node_color = "#FFD700" 
            else: 
                node_color = "#87CEEB"
            
            # Draw the node circle
            # left, top, right, bottom coordinates of node
            self.ds_canvas.create_oval(
                x - node_radius, y - node_radius,  # Top-left corner
                x + node_radius, y + node_radius,  # Bottom-right corner
                fill=node_color, outline="black"
            )
            
            # Add the node's value in the center of the node
            self.ds_canvas.create_text(
                x, y,                       # Center of circle
                text=curr.value, font=("Arial", 12)
            )
            
            # Draw arrow to next node if it exists
            if curr.next:
                self.ds_canvas.create_line(
                    x + node_radius, y,   # Start of line which the rightmost side of the node
                    x + spacing - node_radius, y, # Ending point leftmost side of next node
                    arrow=LAST,                   # Arrow at the end of the line
                    width=2                        # Line thickness
                )
            
            curr = curr.next
            i += 1

            # Move to next row if list is too wide
            if x > 300:
                i = 0
                x = start_x + i * spacing
                y += 70
            ll_len += 1

            # Handle case where list is too long
            if ll_len > 24:
                self.ds_canvas.create_text(
                    x + spacing, y, 
                    text="...", font=("Arial", 16, "bold")
                )
                break
        
        

    """ Visualizer for the BST Data Structure 

            BST is drawn with the root at the top and branches extending to children.
            Each node is represented as a circle with lines (edges) connecting parent to child nodes.
    """
    def draw_bst(self, highlight_value=None):
        if self.bst.root is None:
            self.ds_canvas.create_text(250, 150, text="BST is empty", font=("Arial", 16))
            return
        
        # Dimensions of each node
        node_radius = 25

        # Using canvas width or default to 500
        canvas_width = self.ds_canvas.winfo_width() or 500
        # canvas_height = self.ds_canvas.winfo_height() or 400
        
        # Calculate positions for each node in the tree before drawing
        # This ensures proper spacing and positioning of all nodes
        # min_x, max_x, level, vertical_step
        self.calculate_positions(self.bst.root, 0, canvas_width, 0, node_radius * 2)
        
        # Draw the lines (edges) first so they behind the nodes
        self.draw_bst_connections(self.bst.root)
        
        # Draw the nodes
        self.draw_bst_nodes(self.bst.root, highlight_value, node_radius)
    
    def calculate_positions(self, node, x_min, x_max, level, y_step):

        """Recursively calculates the x,y coordinates for each node in the BST.
    
            Keep slitting the available space in half:
                The current node is positioned at the middle of its available space
                The left subtree gets the left half of the space
                The right subtree gets the right half of the space
            
        """

        # Base case 
        if node is None:
            return
        
        # Set current node's position
        node.x = (x_min + x_max) // 2     # Horizontally centered in available space
        node.y = 50 + level * y_step      # Determined by level in the tree
        
        # Calculate positions for children
        self.calculate_positions(node.left, x_min, node.x, level + 1, y_step)
        self.calculate_positions(node.right, node.x, x_max, level + 1, y_step)

    def draw_bst_connections(self, node):

        # Recursively draws lines between nodes
        if node is None:
            return
        
        # Draw line connecting to left child if it exitsts
        if node.left:
            self.ds_canvas.create_line(
                node.x, node.y,             # Curr node
                node.left.x, node.left.y,   #Left child
                width=2
            )
            self.draw_bst_connections(node.left)
        
         # Draw line connecting to right child if it exitsts
        if node.right:
            self.ds_canvas.create_line(
                node.x, node.y,             # Curr node
                node.right.x, node.right.y, # Right child
                width=2
            )
            self.draw_bst_connections(node.right)
    
    def draw_bst_nodes(self, node, highlight_value, node_radius):

        # Recursively draw the nodes starting at the root

        if node is None:
            return
        
       # Determine color based on highlight
        if node.value == highlight_value:
            node_color = "#FFD700" 
        else: 
            node_color = "#87CEEB"
        
        # Draw the node circle
        self.ds_canvas.create_oval(
            node.x - node_radius, node.y - node_radius,  # Top left corner
            node.x + node_radius, node.y + node_radius,  # Bottom right corner
            fill=node_color, outline="black"
        )
        
        # Add the text
        self.ds_canvas.create_text(
            node.x, node.y, 
            text=str(node.value), font=("Arial", 12)
        )
        
        # Draw children
        self.draw_bst_nodes(node.left, highlight_value, node_radius)
        self.draw_bst_nodes(node.right, highlight_value, node_radius)
    
    


