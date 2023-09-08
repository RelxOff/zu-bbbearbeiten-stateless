import datetime
from operator import attrgetter

todos = []


class todo:
    def __init__(self, title, date, category=None, description=None, isCompleted=False):
        self.title = title
        self.date = date
        self.category = category
        self.description = description
        self.isCompleted = isCompleted


def oneWeekFromToday():
    today = datetime.datetime.now()
    oneWeek = datetime.timedelta(weeks=1)
    return today + oneWeek


def add(title, date, category=None, description=None):
    date = datetime.datetime.strptime(date, "%Y-%m-%d")

    if category is None:
        category = "default"

    todos.append(todo(title, date, category, description))
    todos.sort(key=attrgetter("date"))


def get_all():
    return todos


def get(index):
    return todos[index]


def update(index):
    todos[index].isCompleted = not todos[index].isCompleted
