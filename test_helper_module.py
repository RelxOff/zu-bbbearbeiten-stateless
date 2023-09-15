import datetime
import pytest
import random
import helper


def test_download():
    # Given: I have entered a whole bunch of todos
    todos = [
        {
            "title": "Kommentieren, mit Emojis",
            "date": "2023-10-31",
            "category": "Kunst",
            "description": "Die gesamte Code-Base mit aussagekräftigen Kommentaren versehen, die nur aus Emojis bestehen",
        },
        {
            "title": "Hello World-AI",
            "date": "2023-10-01",
            "category": "Hausaufgaben",
            "description": "Eine AI trainieren, die darauf spezialisiert ist, Hello World-Programme zu generieren",
        },
    ]

    for todo in todos:
        helper.add(
            todo["title"],
            date=todo["date"],
            category=todo["category"],
            description=todo["description"],
        )

    # When: I click the download button
    data = helper.get_csv()

    # Then: I receive a file in CSV format
    assert (
        f'"{todos[0]["title"]}",31.10.2023,{todos[0]["category"]},"{todos[0]["description"]}"'
        in data
    )
    assert (
        f'{todos[1]["title"]},01.10.2023,{todos[1]["category"]},"{todos[1]["description"]}"'
        in data
    )


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
        helper.add(todo[0], date=f"2023-{month}-{day}", category=todo[1])

    # Then: They ought to have their categories
    for item in helper.items:
        categories = [todo[1] for todo in todos]
        assert item.category in categories


def test_description():
    # Given: I have todos with descriptions
    todos = [
        (
            "Zeitmaschine bauen",
            "Vergangenheit kompilieren, Gegenwart laufen lassen, Zukunft debuggen",
        ),
        (
            "AI-Nebenprojekt",
            "Eine unglaublich nervige AI trainieren, die den Benutzer nur veräppelt",
        ),
    ]

    # When: I add the items
    for todo in todos:
        helper.add(todo[0], description=todo[1])

    # Then: They should have descriptions
    for item in helper.items:
        assert item.description is not None


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
        helper.add(todo[0], todo[1])

    # Then: They should be sorted by date
    for i in range(len(helper.items) - 1):
        assert helper.items[i].date <= helper.items[i + 1].date


def test_add():
    # Given: I want to add a to-do with a date
    title = "Lorem ipsum"
    date = "2023-09-02"

    # When: I add the item
    helper.add(title, date)

    # Then: The most recently added to-do should have a date
    item = helper.items[-1]
    assert isinstance(item.date, datetime.date)
