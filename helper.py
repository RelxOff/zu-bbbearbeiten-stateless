from dataclasses import dataclass

# spiecher
items = []


@dataclass
class Item:
    text: str
    isCompleted: bool = False

# BBB-sierung
def add(text):
    text = text.replace('b', 'bbb').replace('B', 'Bbb')
    # index übergabe
    items.append(Item(text))


def get_all():
    return items


def get(index):
    return items[index]


def update(index):
    items[index].isCompleted = not items[index].isCompleted
