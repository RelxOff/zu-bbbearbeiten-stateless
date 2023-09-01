import pytest
import helper
import datetime


def test_add():
    # Given: I want to add a to-do with a date
    text = "Lorem ipsum"
    date = "2023-09-02"

    # When: I add the item
    helper.add(text, date)
    print("title:", helper.todos[-1].title)
    print("Date:", helper.todos[-1].date)

    # Then: The most recently added to-do should have a date
    assert isinstance(helper.todos[-1].date, datetime.date)
