list1 = [3,4,2,1,3,3]
list2 = [4,3,5,3,9,3]

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

print(end)
