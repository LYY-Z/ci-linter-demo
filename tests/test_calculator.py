from calculator import add
import pytest


# 1. 测试正常情况
def test_add_positive_numbers():
    assert add(2, 3) == 5
    assert add(1, 99) == 100


# 2. 测试边界情况（负数、零）
def test_add_with_negative_numbers():
    assert add(-1, 5) == 4
    assert add(-2, -3) == -5
    assert add(0, 0) == 0  # 零也是边界


# 3. 测试异常情况（输入非数字，这里我们期望它抛出TypeError）
def test_add_with_non_numbers():
    with pytest.raises(TypeError):
        add("hello", 3)
