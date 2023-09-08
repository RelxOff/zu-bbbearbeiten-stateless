import datetime
import operator
from dataclasses import dataclass

items = []


@dataclass
class Item:
    text: str
    date: datetime
    category: str
    isCompleted: bool = False


def oneWeekFromToday():
    today = datetime.datetime.now()
    oneWeek = datetime.timedelta(weeks=1)
    return today + oneWeek


def add(text, date=None, category=None):
    text = text.replace("b", "bbb").replace("B", "Bbb")
    if date is None:
        date = oneWeekFromToday()
    else:
        date = datetime.datetime.strptime(date, "%Y-%m-%d")

    if category is None:
        category = "default"

    items.append(Item(text, date, category))
    items.sort(key=lambda x: (x.date, x.category))


def get_all():
    return items


def get(index):
    return items[index]


def update(index):
    items[index].isCompleted = not items[index].isCompleted
