import pytest
from sd_py.sd import *

def test_standard_deviation():
    assert standard_deviation([1,1,1]) == 0.0
    assert standard_deviation([1,2,3,4,5]) == 1.4142135623730951
    assert standard_deviation([-5,-5]) == 0.0
    with pytest.raises(Exception) as e:
        standard_deviation(1)
    assert e.value == 'object of type "int" has no len()'
    with pytest.raises(Exception) as e:
        standard_deviation(1.0)
    assert e.value == 'object of type "float" has no len()'
    with pytest.raises(Exception) as e:
        standard_deviation(True)
    assert e.value == 'object of type "bool" has no len()'
    with pytest.raises(Exception) as e:
        standard_deviation('hello')
    assert e.value == 'unsupported operand type(s) for +: "int" and "str"'
    with pytest.raises(Exception) as e:
        standard_deviation([])
    assert e.value == 'division by zero'
    with pytest.raises(Exception) as e:
        standard_deviation()
    assert e.value == 'standard_deviation() missing 1 required positional argument: "x"'
    with pytest.raises(Exception) as e:
        standard_deviation(s)
    assert e.value == 'name "s" is not defined'

def test_standard_error():
    assert standard_error([1,1,1]) == 0.0
    assert standard_error([1,2,3,4,5]) == 0.6324555320336759
    assert standard_deviation([-5,-5]) == 0.0
    with pytest.raises(Exception) as e:
        standard_error(1)
    assert e.value == 'object of type "int" has no len()'
    with pytest.raises(Exception) as e:
        standard_error(1.0)
    assert e.value == 'object of type "float" has no len()'
    with pytest.raises(Exception) as e:
        standard_error(True)
    assert e.value == 'object of type "bool" has no len()'
    with pytest.raises(Exception) as e:
        standard_error('hello')
    assert e.value == 'unsupported operand type(s) for +: "int" and "str"'
    with pytest.raises(Exception) as e:
        standard_error([])
    assert e.value == 'division by zero'
    with pytest.raises(Exception) as e:
        standard_error()
    assert e.value == 'standard_deviation() missing 1 required positional argument: "x"'
    with pytest.raises(Exception) as e:
        standard_error(s)
    assert e.value == 'name "s" is not defined'
