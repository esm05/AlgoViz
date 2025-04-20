from tkinter import *
from tkinter import ttk
# Import pages
from pages.main_page import MainPage
from pages.sorting_page import SortingPage
from pages.ds_page import DataStructurePage

#Intialize main window
class AlgoVizApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("DSA Visualizer")
        self.geometry("{}x{}".format(800, 800))
        self.configure(bg="grey")
        
        # Create a frame widget as the parent container
        self.container = Frame(self)
        self.container.place(relwidth=1.0, relheight=1.0)
        
        # Dictionary to store different pages
        self.frames = {}
        
        # Initialize frames
        for page in (MainPage, SortingPage, DataStructurePage):
            frame = page(self.container, self)
            self.frames[page] = frame
            frame.place(relwidth=1.0, relheight=1.0)
    
        # Show main page initially
        self.show_page(MainPage)
    
    def show_page(self, page):
        #Bring a specified frame to the front
        frame = self.frames[page]
        frame.tkraise()