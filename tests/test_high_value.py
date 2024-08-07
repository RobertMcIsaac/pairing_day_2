from lib.high_value import HighValue

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

def test_highvalue_both_values_are_equal():
    high_value_1 = HighValue(2, 2)
    assert high_value_1.get_highest() == "Values are equal"

"""
testing the add method against two arguments
"""
def test_highvalue_add_method():
    high_value_1 = HighValue(2, 3)
    assert high_value_1.add(1, "second") == 4