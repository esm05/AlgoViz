import time

def insertion_sort(data, drawData, timeTick):
    for i in range(1, len(data)):
        # Track the index where the current element should be inserted 
        insert_index = i
        # Save the current value
        curr_value = data[i]
        drawData(data, getColorArr(len(data), insert_index, i))
        time.sleep(timeTick)
        # Traverse backwards through "sorted" portion of the array
        for j in range(i - 1, -1, -1):
            if data[j] > curr_value:
                # Shift each element up one to the right to make space for the insertion
                data[j + 1] = data[j]
                # Update index where the curr value is going to go
                insert_index = j

                drawData(data, getColorArr(len(data), insert_index, j))
                time.sleep(timeTick)
            else:
                break
            
        data[insert_index] = curr_value
        drawData(data, getColorArr(len(data), insert_index, i))
        time.sleep(timeTick)
    return data

def getColorArr(length, insert_index, curr):
    colorArray = []
    for i in range(length):
        if i == insert_index:
            color = 'lightgreen'  # where the element will be placed
        elif i == curr:
            color = 'yellow'      #  curr element
        elif i < insert_index - 1:
            color = 'green'
        else:
            color = 'white'
        colorArray.append(color)
    return colorArray