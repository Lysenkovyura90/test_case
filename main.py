from typing import Callable

from models import Library

from method import get_data_for_new_book, delete_book_by_id, find_books_in_library, display_all_books, change_book_status, exit_program

def main() -> None:
   
    library = Library()

    actions: Dict[int, Callable[[Library], None]] = {
        1: get_data_for_new_book,
        2: delete_book_by_id,
        3: find_books_in_library,
        4: display_all_books,
        5: change_book_status,
        6: exit_program,
    }

    while True:
        try:
            answer = int(input('Choose a command by number:\n'
                               '1: Add a book\n'
                               '2: Delete a book\n'
                               '3: Find a book\n'
                               '4: Get all books\n'
                               '5: Change book status\n'
                               '6: Exit\n'
                               'Command: '))
            action = actions.get(answer)
            if action:
                action(library)
            else:
                print('Непраильная команда! ввкдите правильную команду.\n')
        except ValueError:
            print('Неверный ввод. Пожалуйста, введите число, соответствующее команде.\n')


if __name__ == '__main__':
    main()