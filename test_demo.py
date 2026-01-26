import pytest


def test_one():
    assert 1 == 1

@pytest.mark.smoke
def test_two():
    """这是一个冒烟测试"""
    assert 1 + 1 == 2    
    assert 1 + 1 == 2