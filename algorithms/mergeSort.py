import time 
def merge_sort(data, drawData, timeTick):
    return merge_sort_algorithm(data, 0, len(data)-1, drawData, timeTick)

# Recursive merge sort algorithm that splits and sorts left and right partitions.
def merge_sort_algorithm(data, left, right, drawData, timeTick):
    if left < right:
        # Find mid value using integer division
        middle = (left + right) // 2
        
        # Sort left half
        merge_sort_algorithm(data, left, middle, drawData, timeTick)
        
        # Sort right half
        merge_sort_algorithm(data, middle + 1, right, drawData, timeTick)
        
        # Merge the sorted left and right sides
        merge(data, left, middle, right, drawData, timeTick)
    

def merge(data, left, middle, right, drawData, timeTick):
    # Visualize before merge
    drawData(data, getColorArray(len(data), left, middle, right))
    time.sleep(timeTick)

    lhs = data[left:middle + 1] # left hand side temporary array
    rhs = data[middle + 1:right + 1] # right hand side temporary array
    
    leftIdx = rightIdx = 0 # Start each subarray at the first element
    
    for index in range(left, right + 1):
        # Compare elements from both subarrays and place samller values in left hand side
        if leftIdx < len(lhs) and rightIdx < len(rhs):
            if lhs[leftIdx] <= rhs[rightIdx]:
                data[index] = lhs[leftIdx]
                leftIdx += 1
            else:
                data[index] = rhs[rightIdx]
                rightIdx += 1
        # Put remaining elements in the data array
        elif leftIdx < len(lhs):
            data[index] = lhs[leftIdx]
            leftIdx += 1
        else:
            data[index] = rhs[rightIdx]
            rightIdx += 1
    
    # Show final merged state
    drawData(data, ['green' if x >= left and x <= right else "grey" for x in range(len(data))])
    time.sleep(timeTick)

def getColorArray(length, left, middle, right):

    colorArray = []
    for i in range(length):
        # Mark the range currently being recursively sorted
        if left <= i <= right:
            color = 'white'
        else:
            color = 'grey'

        # Highlight midpoint (used to split)
        if i == middle:
            color = 'orange'

        colorArray.append(color)

    return colorArray