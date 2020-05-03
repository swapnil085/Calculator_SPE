from calculator import Claculator

def test_operations_1():
    c = Claculator()
    assert c.add(4,5) == 9
    assert c.sub(4,5) == -1
    assert c.mul(4,5) == 20
    assert c.div(4,5) == 0.8

def test_operations_2():
    c = Claculator()
    assert c.add(42,8) == 50
    assert c.sub(42,8) == 34
    assert c.mul(42,8) == 336
    assert c.div(42,8) == 5.25
