import time

def bubble_sort(data, drawData, timeTick):
    for i in range(len(data) - 1):
        for j in range(len(data) - 1):
            if data[j] > data[j+1]:
                # TO-DO: Add Swap() function
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, ['green' if x == j or x == j + 1 else 'red' for x in range(len(data))]) # green is the two elements being compared 
                time.sleep(timeTick)
    # Rectangles turn green when the array is fully sorted
    drawData(data, ['green' for x in range(len(data))])
