import time

def parition(data, low, high, drawData, timeTick):
    pivot = data[high] # make pivot last element
    split = low - 1 # the element where the subarrays will eventually split

    drawData(data, getColorArray(len(data), low, high, split, split, False))
    time.sleep(timeTick)

    for j in range(low, high):
        if data[j] <= pivot:
            # swap variables so there are two subarrays of values greater than pivot and less than pivot
            drawData(data, getColorArray(len(data), low, high, split, j, True))
            time.sleep(timeTick)

            split += 1
            data[split], data[j] = data[j], data[split]

        drawData(data, getColorArray(len(data), low, high, split, j, False))
        time.sleep(timeTick)
    
    # Swap the pivot with the middle of the two subarrays
    drawData(data, getColorArray(len(data), low, high, split, low, True))
    time.sleep(timeTick)
    data[split + 1], data[high] = data[high], data[split+1]
    # Return the middle of the two subarrays
    return split + 1

def quick_sort(data, low, high, drawData, timeTick): 
    if low < high:
        paritionIndex = parition(data, low, high, drawData, timeTick)

        # Call quick sort recursively then sort left and right side of index
        # left subarray 
        quick_sort(data, low, paritionIndex - 1, drawData, timeTick)
        
        #right subarray
        quick_sort(data, paritionIndex + 1, high, drawData, timeTick)

def getColorArray(dataLength, low, high, split, curr, swapping):
    colorArray=[]
    for i in range(dataLength):
        # Default color when it is outside the active partition
        color = 'grey'

        # Inside the active partition
        if low <= i <= high:
            color = 'white'

        # Mark the pivot
        if i == split:
            color = 'orange'

        # Mark the current element being compared
        if i == curr:
            color = 'yellow'

        # If a swapping
        if swapping and (i == split or i == curr):
            color = 'green'

        colorArray.append(color)
    return colorArray

