from typing import Callable

from models import Library

def get_data_for_new_book(library: Library) -> None:

    title = input('Введите название книги: ')
    author = input('Введите автора книги: ')
    try:
        year = int(input('введите в каком году она была написана '))
        library.add_book(title=title, author=author, year=year)
    except ValueError:
        print('Непраильный год.Пожалуйста повторите.\n')

def delete_book_by_id(library: Library) -> None:
  
    try:
        book_id = int(input('Введите индентификатор книги которую хотите удалить: '))
        library.delete_book(book_id=book_id)
    except ValueError:
        print('Неправильный индентификатор! пожалуйств повторите\n')


def find_books_in_library(library: Library) -> None:
    
    valid_fields = {"название", "автор", "год"}
    field = input("Искать по (название/автор/год): ").lower()

    if field not in valid_fields:
        print(f"не правильное '{field}'пожалуйста выберите один из {', '.join(valid_fields)}.\n")
        return

    value = input(f"Ввелите {field}: ")
    if field == "год":
        try:
            value = int(value)
        except ValueError:
            print("Год должен быть числом. Пожалуйста, попробуйте снова.\n")
            return

    found_books = library.find_books(**{field: value})
    if found_books:
        for book in found_books:
            print(book)
    else:
        print("Нет книг по вашим критериям.\n")


def display_all_books(library: Library) -> None:
    
    books = library.get_all_books()
    if books:
        for book in books:
            print(book)
    else:
        print('В библиотеке пока нет книг.\n')


def change_book_status(library: Library) -> None:
    
    try:
        book_id = int(input('Введите идентификатор книги, статус которой вы хотите изменить: '))
        print('1: Книга в наличии\n'
              '2: Книга была выдана')
        user_status = int(input('Выберите статус (1/2): '))
        if user_status == 1:
            book_status = True
        elif user_status == 2:
            book_status = False
        else:
            print('Неправильный статус. Выберите оди или два.\n')
            return
        library.change_book_status(book_id=book_id, new_status=book_status)
    except ValueError:
        print('Неверный ввод. Пожалуйста, введите числовые значения для идентификатора и статуса.\n')

def exit_program(_: Library) -> None:
   
    print('Хорошего ДНЯ!')
    exit()