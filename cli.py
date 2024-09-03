import time
import functions

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is",now)

while True:
    user_action = input("Type add, edit, complete, show or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos, 'todos.txt')

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        for index, todo in enumerate(todos):
            todo = todo.capitalize()
            todo = todo.strip('\n')
            row = f"{index+1}-{todo}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos, 'todos.txt')

        except ValueError:
            print("Your command is invalid!!")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with the entered index.")
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print("Invalid comment")
print("Bye!!")
