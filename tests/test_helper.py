import datetime
import pytest
import random
import helper


def test_category():
    # Given: I have todos with different categories
    todos = [
        ("Kabelsalat auflösen", "Hausarbeit"),
        ("Wäsche machen", "Hausarbeit"),
        ("Trash Core-Album aufnehmen", "Kunst"),
        ("Französisch lernen", "Hausaufgaben"),
    ]

    # When: I add the items
    for todo in todos:
        month = random.randrange(1, 13)
        day = random.randrange(1, 29)
        date = f"2023-{month}-{day}"
        category = todo[1]
        helper.add(todos[0], date, category, None)

    # Then: They ought to have their categories
    for todo in helper.get_all():
        categories = [todo[1] for todo in todos]
        assert todo.category in categories


def test_add():
    # Given: I want to add a to-do with a date
    text = "Lorem ipsum"
    date = "2023-09-02"
    description = "Lorem ipsum hi hi ha ha"

    # When: I add the item
    helper.add(text, date, None, description)

    # Then: The most recently added to-do should have a date
    assert isinstance(helper.todos[-1].date, datetime.date)
    assert helper.todos[-1].description == description


def test_sort():
    # Given: I have several to-dos with dates
    todos = [
        ("Universum debuggen", "2023-09-06"),
        ("Sinn des Lebens entdecken", "2023-09-01"),
        ("Superheld werden", "2023-10-25"),
        ("Netto null", "2050-01-01"),
    ]

    # When: I add the items
    for todo in todos:
        helper.add(todo[0], todo[1], None, None)

    # Then: They should be sorted by date
    for i in range(len(helper.todos) - 1):
        assert helper.todos[i].date <= helper.todos[i + 1].date


def test_add():
    # Given: I want to add a to-do with a date
    text = "Lorem ipsum"
    date = "2023-09-02"

    # When: I add the item
    helper.add(text, date, None, None)

    # Then: The most recently added to-do should have a date
    item = helper.todos[-1]
    assert isinstance(item.date, datetime.date)
