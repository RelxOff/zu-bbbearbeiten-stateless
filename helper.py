from dataclasses import dataclass

# spiecher
todos = []


@dataclass
class todo:
    title: str
    isCompleted: bool = False

# BBB-sierung
def add(title):
    title = title.replace('b', 'bbb').replace('B', 'Bbb')
    # index übergabe
    todos.append(todo(title))


def get_all():
    return todos


def get(index):
    return todos[index]


def update(index):
    todos[index].isCompleted = not todos[index].isCompleted
