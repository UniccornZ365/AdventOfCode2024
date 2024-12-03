import csv

def getDistance(list1, list2):
    list1  = sorted(list1)
    list2 = sorted(list2)
    end = 0

    def distance(x, y):
        if x >= y:
            result = x - y
        else:
            result = y - x
        return result

    for items in range(0,len(list1)):
        item1 = list1[items]
        item2 = list2[items]
        result = distance(item1, item2)
        end = end + result
    
    return end

list1 = []
list2 = []

with open('Day1_Input.csv', newline='') as csvfile:
    lines  = csvfile.readlines()
    for line in lines:
        parts = line.split("   ")
        list1.append(int(parts[0]))
        list2.append(int(parts[1]))

print(getDistance(list1,list2))