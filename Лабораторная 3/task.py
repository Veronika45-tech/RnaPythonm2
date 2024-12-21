class Book:
    """
    Базовый класс книги

    Атрибуты:
        name (str): Название
        author (str): Автор
    """
    def __init__(self, name: str, author: str):
        """
        Инициализация книги

        Аргументы:
            name (str): Название
            author (str): Автор
        """
        self._name = name
        self._author = author

    @property
    def name(self):
        """
        Возвращает название

        Возвращаемое значение:
            str: Название
        """
        return self._name

    @property
    def author(self):
        """
        Возвращает автора

        Возвращаемое значение:
            str: Автор
        """
        return self._author

    def __str__(self):
        """
        Возвращает строковое представление книги

        Возвращаемое значение:
            str: Строковое представление
        """
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        """
        Возвращает официальное строковое представление книги

        Возвращаемое значение:
            str: Официальное строковое представление
        """
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """
    Класс для печатной книги

    Атрибуты:
        name (str): Название книги
        author (str): Автор
        pages (int): Количество страниц
    """
    def __init__(self, name: str, author: str, pages: int):
        """
        Инициализация печатной книги

        Аргументы:
            name (str): Название книги
            author (str): Автор
            pages (int): Количество страниц
        """
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        """
        Возвращает количество страниц

        Возвращаемое значение:
            int: Количество страниц
        """
        return self._pages

    @pages.setter
    def pages(self, value):
        """
        Устанавливает количество страниц с проверкой

        Аргументы:
            value (int): Количество страниц

        Исключения:
            TypeError: Если значение не является целым числом
            ValueError: Если значение не является положительным числом
        """
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = value

    def __str__(self):
        """
        Возвращает строковое представление печатной книги

        Возвращаемое значение:
            str: Строковое представление печатной книги
        """
        return f"Книга {self.name}. Автор {self.author}. Количество страниц: {self.pages}"

    def __repr__(self):
        """
        Возвращает официальное строковое представление печатной книги

        Возвращаемое значение:
            str: Официальное строковое представление печатной книги
        """
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    """
    Класс для аудиокниги

    Атрибуты:
        name (str): Название
        author (str): Автор
        duration (float): Продолжительность в часах
    """
    def __init__(self, name: str, author: str, duration: float):
        """
        Инициализация аудиокниги

        Аргументы:
            name (str): Название
            author (str): Автор
            duration (float): Продолжительность в часах
        """
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        """
        Возвращает продолжительность аудиокниги

        Возвращаемое значение:
            float: Продолжительность в часах
        """
        return self._duration

    @duration.setter
    def duration(self, value):
        """
        Устанавливает продолжительность аудиокниги с проверкой

        Аргументы:
            value (float): Продолжительность в часах

        Исключения:
            TypeError: Если значение не является числом
            ValueError: Если значение не является положительным числом
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность должна быть числом")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self._duration = value

    def __str__(self):
        """
        Возвращает строковое представление аудиокниги

        Возвращаемое значение:
            str: Строковое представление аудиокниги
        """
        return f"Книга {self.name}. Автор {self.author}. Продолжительность: {self.duration} часов"

    def __repr__(self):
        """
        Возвращает официальное строковое представление аудиокниги

        Возвращаемое значение:
            str: Официальное строковое представление аудиокниги
        """
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"


if __name__ == "__main__":
    paper_book = PaperBook("Последнее желание", "Анджей Сапковский", 288)
    audio_book = AudioBook("Forever Young", "Alphaville", 4.25)

    print(paper_book)
    print(audio_book)
