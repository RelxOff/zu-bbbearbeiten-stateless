from dataclasses import dataclass
import datetime
from operator import attrgetter

# speicher
todos = []


@dataclass
class todo:
    title: str
    date: datetime.date = None
    description: str = None
    isCompleted: bool = False


# test
# BBB-sierung
def add(title, date, description):
    title = title.replace("b", "bbb").replace("B", "Bbb")
    date = datetime.datetime.strptime(date, "%Y-%m-%d")
    todos.sort(key=attrgetter("date"))
    # index übergabe
    todos.append(todo(title, date, description))


def get_all():
    return todos


def get(index):
    return todos[index]


def update(index):
    todos[index].isCompleted = not todos[index].isCompleted


def delete():
    todos.remove = todos
