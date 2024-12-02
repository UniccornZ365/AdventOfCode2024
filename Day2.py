levels = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

levelList = levels.splitlines()

def check(levelItems):
    
    safe = []

    #Checks if the list is assending or decending
    asc = str(sorted(levelItems))[1:-1:] #strip of []
    listCopy = levelItems.copy()
    listCopy.sort(reverse=True)
    desc = str(listCopy)[1:-1:] #revese

    if str(levelItems)[1:-1:] == asc or str(levelItems)[1:-1:] == desc:

        #Check that no item shave more than 3 apart
        itemCount = len(levelItems)
        for i in range(0, itemCount):
            
            if i < itemCount-1:
                x = int(levelItems[i])
                y = int(levelItems[i+1])
                if x >= y:
                    result = x-y
                else:
                    result = y-x
                if result <=3 and result > 0:
                    safe.append("Yes")

        fail = safe.count("Yes")
        if fail == itemCount -1:
            print("Safe")
        else:
            print("Unsafe")
    else:
        print("Unsafe")

for level in levelList:
    print(level)
    check(level.split(" "))