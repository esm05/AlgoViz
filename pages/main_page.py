from tkinter import *
from tkinter import ttk

class MainPage(Frame):
    def __init__(self, parent, controller):

        # Store controller as an attribute of the class
        self.controller = controller
        Frame.__init__(self, parent, bg="#004080")
        
        # Create a centered frame for different widgets for a title, a desciption, and two buttons
        content_frame = Frame(self, bg="#A2A2FF", bd=50, relief="groove")
        content_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        # Title
        title_label = Label(
            content_frame, 
            text="AlgoViz", 
            font=("Sans", 24, "bold"),
            bg="#A2A2FF",
            fg = "#400080"
        )
        title_label.pack(pady=20)
        
        # Description
        description = Label(
            content_frame,
            text="Choose a category to explore:",
            font=("Arial", 14),
            bg="#A2A2FF",
            fg = "#400080"
        )
        description.pack(pady=10)
        
        # Sorting button
        sorting_button = ttk.Button(
            content_frame, 
            text="Sorting Algorithms", 
            command=self.go_to_sorting_page, 
            width=20
            )
        sorting_button.pack(pady=10)
        
        # Data Structures Button
        ds_button = ttk.Button(
            content_frame, 
            text="Data Structures", 
            command=self.go_to_ds_page, 
            width=20
            )
        ds_button.pack(pady=10)
        
    def go_to_ds_page (self):
        from pages.ds_page import DataStructurePage
        self.controller.show_page(DataStructurePage)

    def go_to_sorting_page(self):
        from pages.sorting_page import SortingPage
        self.controller.show_page(SortingPage)