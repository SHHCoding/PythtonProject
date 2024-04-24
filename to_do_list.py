import os
import time


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        os.system('cls')
        print('\t\t\t====> Add Task <====')
        task = input('\n. Enter task: ')
        self.tasks.append(task)
        print(f"Task '{task}' added successfully.")
        input('\nPress enter to continuous... ')

    def delete_task(self):
        os.system('cls')
        print('\t\t\t====> Delete Task <====')
        index = int(input('\n. Enter task index to deete: ')) - 1
        try:
            task = self.tasks.pop(index)
            print(f"Task '{task}' delete successfully.")
        except IndexError:
            print('Invalid task index.')
        input('\nPress enter to continuous... ')

    def show_task(self):
        os.system('cls')
        print('\t\t\t====> Tasks List <====\n')
        if self.tasks:
            for i, task in enumerate(self.tasks):
                print(f'{i+1}. {task}')
        else:
            print('Your list is emoty.')
        input('\nPress enter to continuous... ')


def main():
    todo_list = ToDoList()

    while True:
        os.system('cls')
        print('\t\t\t====> ToDo List <====')
        print('\n1.   Add Task')
        print('2.   Delete Task')
        print('3.   View Tasks')
        print('4.   Quit')

        choice = input('Enter your choice 1-4: ')

        if choice == '1':
            todo_list.add_task()
        elif choice == '2':
            todo_list.delete_task()
        elif choice == '3':
            todo_list.show_task()
        elif choice == '4':
            print('\n===> Good Bye <====')
            break
        else:
            invalid = '\nInvalid choice. Please enter a number between 1 to 4.'
            for i in invalid:
                print(i, end='')
                time.sleep(0.05)
            time.sleep(1)
