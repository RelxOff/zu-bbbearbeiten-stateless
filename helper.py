import datetime
import operator

items = []

class Item:
    text: str
    date: datetime
    category: str = None
    description: str = None
    isCompleted: bool = False


def oneWeekFromToday():
    today = datetime.datetime.now()
    oneWeek = datetime.timedelta(weeks=1)
    return today + oneWeek


def add(title, date=None, category=None, description=None):
    title = title.replace("b", "bbb").replace("B", "Bbb")
    if date is None:
        date = oneWeekFromToday()
    else:
        date = datetime.datetime.strptime(date, "%Y-%m-%d")

    if category is None:
        category = "default"
    
    todos.sort(key=attrgetter("date"))
    todos.append(todo(title, date, category, description))

def get_all():
    return items


def get(index):
    return items[index]


def update(index):
    items[index].isCompleted = not items[index].isCompleted
