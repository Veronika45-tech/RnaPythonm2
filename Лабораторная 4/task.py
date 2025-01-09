class Smartphone:
    """
    Базовый класс для смартфонов

    Атрибуты:
        brand (str): Бренд смартфона
        model (str): Модель смартфона
        price (float): Цена смартфона
    """
    def __init__(self, brand: str, model: str, price: float):
        """
        Инициализация смартфона

        Аргументы:
            brand (str): Бренд смартфона
            model (str): Модель смартфона
            price (float): Цена смартфона
        """
        self.brand = brand
        self.model = model
        self.price = price

    def __str__(self) -> str:
        """
        Возвращает строковое представление смартфона

        Возвращаемое значение:
            str: Строковое представление смартфона
        """
        return f"Смартфон {self.brand} {self.model}, цена: {self.price} USD"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление смартфона

        Возвращаемое значение:
            str: Официальное строковое представление смартфона
        """
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, price={self.price!r})"

    def display_info(self) -> str:
        """
        Возвращает информацию о смартфоне

        Возвращаемое значение:
            str: Информация о смартфоне
        """
        return f"Бренд: {self.brand}, Модель: {self.model}, Цена: {self.price} USD"


class IPhone(Smartphone):
    """
    Класс для смартфонов iPhone

    Атрибуты:
        brand (str): Бренд смартфона
        model (str): Модель смартфона
        price (float): Цена смартфона
        ios_version (str): Версия iOS
    """
    def __init__(self, model: str, price: float, ios_version: str):
        """
        Инициализация iPhone.

        Аргументы:
            model (str): Модель смартфона
            price (float): Цена смартфона
            ios_version (str): Версия iOS
        """
        super().__init__("Apple", model, price)
        self.ios_version = ios_version

    def __str__(self) -> str:
        """
        Возвращает строковое представление iPhone

        Возвращаемое значение:
            str: Строковое представление iPhone
        """
        return f"iPhone {self.model}, цена: {self.price} USD, iOS версия: {self.ios_version}"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление iPhone

        Возвращаемое значение:
            str: Официальное строковое представление iPhone
        """
        return f"{self.__class__.__name__}(model={self.model!r}, price={self.price!r}, ios_version={self.ios_version!r})"

    def display_info(self) -> str:
        """
        Возвращает информацию о iPhone

        Возвращаемое значение:
            str: Информация о iPhone

        Причина перегрузки:
            Добавление информации о версии iOS
        """
        return f"Бренд: {self.brand}, Модель: {self.model}, Цена: {self.price} USD, iOS версия: {self.ios_version}"


if __name__ == "__main__":
    try:
        iphone = IPhone("13 Pro", 999.99, "iOS 15.0")
        print(iphone)
    except TypeError as e:
        print(f"Ошибка: {e}")

    try:
        iphone.price = -100
    except ValueError as e:
        print(f"Ошибка: {e}")

    try:
        iphone.ios_version = "Android 11"
    except TypeError as e:
        print(f"Ошибка: {e}")
