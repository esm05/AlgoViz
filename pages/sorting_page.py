from tkinter import *
from tkinter import ttk
from algorithms.bubbleSort import bubble_sort
from algorithms.quickSort import quick_sort
from algorithms.mergeSort import merge_sort
from algorithms.selectionSort import selection_sort
from algorithms.insertionSort import insertion_sort
import random

class SortingPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="#004080")
        
        selected_algo = StringVar()
        random_data = []

        self.controller = controller

        def drawData(data, colorArray):
            self.middle_canvas.delete("all")
            ## Create rectangle for each element
            # Get same agruments as the canvas widget 
            c_relheight = 400
            c_relwidth = 600

            # width of the rectangle 
            x_width = c_relwidth / (len(data) + 1)

            # offset from the border of the widget
            offset = 10
            # spacing between each rectangle
            spacing = 10

            # "Normalize" data so really high numbers do not take up the height of the whole widget and resizes the other rectangles to be proportionate
            normal_data = [i / max(data) for i in data]
            

            for i, height in enumerate(normal_data):
                # Top left corner
                x0 = i * x_width + offset + spacing
                y0 = c_relheight - height * 370 # hightest value has 30 pixels from the height

                # Bottom right corner
                x1= (i + 1) * x_width + offset 
                y1 = c_relheight

                self.middle_canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
               # middle_canvas.create_text(x0+2, y0, anchor="sw",text=data[i])
            # Updates the graph to see step-by-step updates
            self.update_idletasks()

        def Generate():
            """
            # generate an array of random integers to display 
            # setting the min_val, max_val, and size variables from the user entries
            
            #  try catch in the user does not have entries the program assigns default values
            try:
                min = int(minEntry.get()) 
                max = int(maxEntry.get()) 
                size = int(sizeEntry.get()) 
            except ValueError:
                # Handle the case where conversion to int fails
                print("Error: Please enter valid integer values")
                # Assign default values
                min = 0
                max = 100
                size = 10
            
            # The min cannot be negative
            if min < 0: min = 0
            # The max cannot be above 100
            if max > 100: max = 100
            # The size cannot go above 150
            if size > 150: size = 150

            # If the user types a min value greater than max swap the variables
            if min > max: min, max = max, min """
            global random_data
            # do not need any of the checks because of the scales
            min = int(minEntry.get()) 
            max = int(maxEntry.get()) 
            size = int(sizeEntry.get()) 

            random_data = []
            for i in range(size):
                random_data.append(random.randrange(min, max+1)) # Inclusive
            
            drawData(random_data, ['#CFCFFF' for x in range(len(random_data))]) 
            
            
        
        def VisualizeAlgorithm():
            global random_data
            if (algMenu.get() == 'Bubble Sort'):
                bubble_sort(random_data, drawData, speedScale.get())
            elif (algMenu.get() == 'Quick Sort'):
                quick_sort(random_data, 0, len(random_data) - 1, drawData, speedScale.get())
                drawData(random_data, ['green' for x in range(len(random_data))])
            elif(algMenu.get() == 'Merge Sort'):
                merge_sort(random_data, drawData, speedScale.get())
                drawData(random_data, ['green' for x in range(len(random_data))])
            elif(algMenu.get() == 'Selection Sort'):
                selection_sort(random_data, drawData, speedScale.get())
                drawData(random_data, ['green' for x in range(len(random_data))])
            elif(algMenu.get() == 'Insertion Sort'):
                insertion_sort(random_data, drawData, speedScale.get())
                drawData(random_data, ['green' for x in range(len(random_data))])
            
        

        # Top_frame w/title
        top_frame = Frame(self, bg='#0000DC')
        top_frame.place(relwidth=0.4, relheight=0.1, relx=0.5, rely=0.0, anchor='n')
        
        # Title
        title = Label(top_frame, text="Sorting Algorithms", font=("Arial", 20, "bold"), fg='#EFEFFF')
        title.config(bg='#004080')
        title.place(relheight=1, relwidth=1)
        
        # Middle_frame w/UI
        middle_frame_top = Frame(self, bg='#1B003C')
        middle_frame_top.place(relwidth=1.0, relheight=0.2, rely=0.11)

        # Middle canvas for the sorting algorithm visualization
        self.middle_canvas = Canvas(self, width=650, height=400, bg="white")
        self.middle_canvas.grid(row=1, column=0, padx=80, pady=260)

        # First Row of UI
        Label(middle_frame_top, text="Select Values: ", bg='#400080', fg='#EFEFFF').grid(row=0, column=0, padx=5, pady=5, sticky='w')
        sizeEntry = Scale(middle_frame_top, from_=5, to=40, resolution=1, orient="horizontal", label="Size")
        sizeEntry.grid(row=0, column=1, padx=5, pady=5)

        minEntry = Scale(middle_frame_top, from_=1, to=10, resolution=1, orient="horizontal", label="Min Val")
        minEntry.grid(row=0, column=2, padx=5, pady=5)

        maxEntry = Scale(middle_frame_top, from_=10, to=100, resolution=1, orient="horizontal", label="Max Val")
        maxEntry.grid(row=0, column=3, padx=5, pady=5)

        Button(middle_frame_top, text="Generate", command=Generate, bg='#4242FF', fg='#EFEFFF').grid(row=0, column=4, padx=5, pady=5)

        # Second row of UI
        Label(middle_frame_top, text="Algorithm: ", bg='#400080', fg='#EFEFFF').grid(row=1, column=0, padx=5, pady=5, sticky='w')
        algMenu = ttk.Combobox(middle_frame_top, textvariable=selected_algo, values=['','Bubble Sort', 'Merge Sort', 'Quick Sort', 'Selection Sort', 'Insertion Sort'])
        algMenu.grid(row=1, column=1, padx=5, pady=5)
        
        speedScale = Scale(middle_frame_top, from_=0.2, to=2.0, length=200, digits=2, resolution=0.2, orient="horizontal", label="Select Speed (in Seconds)")
        speedScale.grid(row=1, column=2, padx=5, pady=5)
        Button(middle_frame_top, text="Visualize", command=VisualizeAlgorithm, bg='#4242FF', fg='#EFEFFF').grid(row=1, column=3, padx=5, pady=5)

        # Lower Frame w/ Back button
        back_button = Button(self, text="Back to Main Menu", bg='#4242FF', fg='#EFEFFF', command=self.go_to_main_page )
        back_button.place(relx = 0.1, rely=0.9, anchor='n')
    
    def go_to_main_page(self):
        self.middle_canvas.delete('all')
        # Avoids circular imports
        from pages.main_page import MainPage
        
        self.controller.show_page(MainPage)

   