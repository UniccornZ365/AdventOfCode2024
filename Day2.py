levels = """"""




def check(levelItems):
    
    gapCheck = []

    #Checks if the list is assending or decending
    asc = str(sorted(levelItems))[1:-1:] #strip of []
    listCopy = levelItems.copy()
    listCopy.sort(reverse=True)
    desc = str(listCopy)[1:-1:] #revese

    if str(levelItems)[1:-1:] == asc or str(levelItems)[1:-1:] == desc:

        #Check that no item shave more than 3 apart
        itemCount = len(levelItems)
        for i in range(0, itemCount):
            
            if i < itemCount - 1:
                x = int(levelItems[i])
                y = int(levelItems[i+1])
                
                if x >= y:
                    result = x-y
                else:
                    result = y-x
                
                if result > 3 or result == 0:
                    return False

        return True
    else:
        return False
    
with open('Day2_Input.txt', newline='') as csvfile:
    levelList  = csvfile.readlines()

safeCount = 0
for level in levelList:
    if(check(level.rstrip().split(" ")) == True):
        safeCount = safeCount+1

print(safeCount)