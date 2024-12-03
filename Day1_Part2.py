import csv

def similarityScore(list1,list2):
    score = 0
    for i in list1:
        appearances = list2.count(i)
        score = score + (i*appearances)
    return score


list1 = []
list2 = []

with open('Day1_Input.csv', newline='') as csvfile:
    lines  = csvfile.readlines()
    for line in lines:
        parts = line.split("   ")
        list1.append(int(parts[0]))
        list2.append(int(parts[1]))

print(similarityScore(list1,list2))