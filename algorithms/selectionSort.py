import time 

def selection_sort(data, drawData, timeTick):
    for i in range(len(data) - 1):
        # store first element of the array as the minimum
        min_index = i
        # find the minimum value
        for j in range(i + 1, len(data)):
            if data[j] < data[min_index]:
                min_index = j
                drawData(data, getColorArr(len(data), min_index, i))
                time.sleep(timeTick)
        # swap the values
        data[i], data[min_index] = data[min_index], data[i]

        drawData(data, ['green' if x <= i else 'white' for x in range(len(data))])
        time.sleep(timeTick)
    return data

def getColorArr(length, min, curr):
    colorArray = []
    for i in range(length):
        if i == min:
            color = 'lightgreen'  # current known min value
        elif i == curr:
            color = 'yellow'      # index where the min will be placed
        elif i < curr:
            color = 'green'
        else:
            color = 'white'
        colorArray.append(color)
    return colorArray
        
