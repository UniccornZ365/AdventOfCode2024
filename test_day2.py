import Day2


def test_mixed_returns_false():
    assert Day2.check(["1","20","3","4"]) == False

def test_asc_returns_true():
    assert Day2.check(["1","2","3","4"]) == True

def test_desc_returns_true():
    assert Day2.check(["4","3","2","1"]) == True

def test_gap1_returns_true():
    assert Day2.check(["1","2"]) == True

def test_gap2_returns_true():
    assert Day2.check([1,3,4]) == True

def test_gap3_returns_true():
   assert  Day2.check([1,4]) == True

def test_gap4_returns_false():
    assert Day2.check([1,5]) == False

def test_gap10_returns_false():
    assert Day2.check([1,11]) == False

def test_no_gap_returns_false():
   assert Day2.check([1,1]) == False

def test_line1():
    assert Day2.check([7, 6, 4, 2, 1]) == True

def test_line2():
    assert Day2.check([1, 2, 7, 8, 9]) == False

def test_line3():
    assert Day2.check([9, 7, 6, 2, 1]) == False

def test_line4():
    assert Day2.check([1, 3, 2, 4, 5]) == False

def test_line5():
    assert Day2.check([8, 6, 4, 4, 1]) == False

def test_line6():
    assert Day2.check([1, 3, 6, 7, 9]) == True

def test_line7():
    assert Day2.check([24, 26, 27, 29, 32, 34, 35]) == True

def test_line8():
    assert Day2.check([64, 66, 68, 69, 70, 72, 75]) == True
                      
def test_line():
    assert Day2.check([28, 27, 24, 23, 21, 18, 16]) == True

def test_line():
    assert Day2.check(["63", "66", "67", "68", "71", "73", "75"]) == True
