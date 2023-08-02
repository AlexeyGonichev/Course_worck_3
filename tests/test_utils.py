import pytest
from utils import load_operations


def test_load_operations():
    '''load_json возвращает данные не из словара'''
    data = load_operations()
    assert isinstance(data, list)

def test_
