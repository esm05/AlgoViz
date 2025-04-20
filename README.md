# AlgoViz - Data Structures and Sorting Algorithms Visualizer

AlgoViz is an interactive visualization tool built with the Tkinter library in Python that helps users understand common data structures and sorting algorithms through animated visualizations.

## Features

### Sorting Algorithms w/ Big O Notation
| Sorting Algorithm  | Time Complexity |
|--------------------|-----------------|
| Bubble Sort        |  (O(N))         |
| Quick Sort         |  (O(N log N)    |
| Merge Sort         |  (O(N log N)    |
| Selection Sort     |  (O(N^2)        |
| Insertion Sort     |  (O(N)          |

### Sorting Algorithms Control Panel:
- Adjustable array size
- Adjustable value ranges
- Adjustable animation speed in seconds
- Select an algorithm from the combobox
- Real-time visualization

### Supported Data Structure and Methods:
- Stack: Push, Pop, Search, Peek
- Queue: Enqueue, Dequeue, Search
- Linked List: Insert at tail, Delete, Search at index
- BST: Insert, Delete, Search

## Requirements

- Python 3 or higher

## Installation

1. Clone the repository:
```bash
clone https://github.com/esm05/AlgoViz.git
```

2. Navigate to the project directory:
```bash
cd AlgoViz
```

3. Run the application:
```bash
python main.py
```

## Usage

1. Choose between "Sorting Algorithms" or "Data Structures" from HomePage

### Sorting Visualization
1. Select array size, minimum, and maximum values using the sliders
2. Click "Generate" to create an array of random values in the range 
3. Choose a sorting algorithm from the dropdown menu
4. Adjust animation speed if desired
5. Click "Visualize" to see the sorting process

### Data Structure Visualization
1. Select a data structure from the dropdown menu
2. Enter values in the input field
3. Use the operation buttons to interact with the data structure
4. Watch the visualization update in real-time
5. Clear the canvas if a reset is necessary
