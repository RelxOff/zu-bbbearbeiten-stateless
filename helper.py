from dataclasses import dataclass

# Exercise 1602: This is where the data is stored:
# It's just a simple array, which we will replace
# by a database at a later point
todos = []


@dataclass
class Todo:
    title: str
    isCompleted: bool = False


def add(title):
    # Exercise 1602: This is where the bbb-isation happens
    title = title.replace('b', 'bbb').replace('B', 'Bbb')
    todos.append(Todo(title))


def get_all():
    """This actually isn't necessary, in python you don't have 
    to deal with things such as private and public
    and getters and setters if you don't want to. You can access 
    todos directly from main.py"""
    return todos


def get(index):
    """Same as above"""
    return todos[index]


def update(index):
    todos[index].isCompleted = not todos[index].isCompleted
