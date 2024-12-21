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


if __name__ == '__main__':
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)

    print(list_books)
