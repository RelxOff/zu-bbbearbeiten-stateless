'''
import helper
import pytest

def test_add():
    str = "Test Item"
    helper.add("Test Item")
    assert helper.todos[-1].title == str
'''