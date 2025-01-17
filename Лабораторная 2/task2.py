BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    """
    Класс Book представляет собой книгу

    Атрибуты:
        id (int): Идентификатор книги
        name (str): Название
        pages (int): Количество страниц
    """

    def __init__(self, id_: int, name: str, pages: int):
        """
        Инициализирует новый экземпляр класса Book

        Аргументы:
            id_ (int): Идентификатор книги
            name (str): Название
            pages (int): Количество страниц
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __repr__(self):
        """
        Возвращает строковое представление экземпляра класса Book, которое исп. для создания такого же экземпляра

        Возвращает:
            str: Строковое представление экземпляра класса Book
        """
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"

    def __str__(self):
        """
        Возвращает строковое представление экземпляра класса Book, предназначенное для пользователя

        Возвращает:
            str: Строковое представление экземпляра класса Book
        """
        return f"Книга \"{self.name}\""


class Library:
    """
    Класс Library представляет собой библиотеку книг

    Атрибуты:
        books (list of Book): Список книг в библиотеке

    Методы:
        get_next_book_id(): Возвращает идентификатор для добавления новой книги в библиотеку
        get_index_by_book_id(book_id): Возвращает индекс книги в списке по её идентификатору
    """

    def __init__(self, books=None):
        """
        Инициализирует новый экземпляр класса Library.

        Аргументы:
            books (list of Book, optional): Список книг. По умолчанию None, что инициализирует пустой список
        """
        if books is None:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self):
        """
        Возвращает идентификатор для добавления новой книги в библиотеку

        Возвращает:
            int: Идентификатор для новой книги. Если библиотека пуста, возвращает 1
                 Если книги есть, возвращает идентификатор последней книги увеличенный на 1
        """
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id):
        """
        Возвращает индекс книги в списке по её идентификатору

        Аргументы:
            book_id (int): Идентификатор книги.

        Возвращает:
            int: Индекс книги в списке.

        Исключения:
            ValueError: Если книга с запрашиваемым идентификатором не существует.
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()
    print(empty_library.get_next_book_id())

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)
    print(library_with_books.get_next_book_id())

    print(library_with_books.get_index_by_book_id(1))
