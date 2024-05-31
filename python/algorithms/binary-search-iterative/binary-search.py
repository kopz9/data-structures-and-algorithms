import math

def getMiddle(start, end): 
  return math.floor((start + end) / 2)

def binarySearch(numbers, target): 
  start = 0
  end = len(numbers) - 1
  middle = getMiddle(start, end)
  found = False
  
  while start <= end and not found:
    middle = getMiddle(start, end)
    middleNumber = numbers[middle]   

    if (middleNumber == target):
      found = True
      
    if (middleNumber > target):
      end = middle - 1  
      
    if(middleNumber < target):
      start = middle + 1
  
  return found

