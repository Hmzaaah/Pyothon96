def binarySearch(array ,serach ,lowIndex ,highIndex):
    while lowIndex <= highIndex:
        mid = lowIndex +(highIndex - lowIndex)
        if array[mid]==search:
            return mid
        elif array[mid] < search:
            lowIndex = mid + 1

        else:
            highIndex = mid -1
            return -1


grades = [10 , 12 , 15,17 ,18 ,19 ,20]
search = 15
#Best Case:o(1)
#worst caseo(7)
result =binarySearch(grades , search , 0 ,len(grades) -1)
if result == -1:
    print("Not found")
else:
    print("found")
                     