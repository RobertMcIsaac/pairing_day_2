from lib.high_value import *

def test_highvalue_value_first_is_2():  
    high_value_1 = HighValue(2, 3)
    assert high_value_1.value_first == 2

"""
test that get_highest method 
returns first value is higher when value_first is higher
"""

def test_highvalue_first_value_is_higher():
    high_value_1 = HighValue(3, 2)
    assert high_value_1.get_highest() == "First value is higher"

def test_highvalue_second_value_is_higher():
    high_value_1 = HighValue(2, 3)
    assert high_value_1.get_highest() == "Second value is higher"