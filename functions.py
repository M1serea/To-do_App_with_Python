FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Reads a text file and returns the list of
    to-do items
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todo_arg, filepath=FILEPATH):
    """ Writes the to-do list items to a text file """
    with open(filepath, 'w') as file:
        file.writelines(todo_arg)

if'__name__' == '__main__':
    print("Hello, I'm from functions.py")