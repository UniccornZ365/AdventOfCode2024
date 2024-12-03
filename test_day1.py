import Day1

def test_day1():
    list1 = [3,4,2,1,3,3]
    list2 = [4,3,5,3,9,3]
    assert Day1.getDistance(list1,list2) == 11
