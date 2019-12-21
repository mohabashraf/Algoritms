import math
def binarySearch(list, searchedItem):
    lowest = 0
    highest = len(list)
    while(lowest <= highest):          
        middle = math.ceil(lowest + highest/2) 
        if(searchedItem == list[middle]):
            return searchedItem 
        elif searchedItem > list[middle]:
            lowest = middle
        highest = middle
   
list = [1, 2, 3]
print(binarySearch(list , 3))