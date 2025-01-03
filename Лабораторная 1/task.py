class SmartPhone:
    """
    Класс, представляющий смартфон
    Атрибуты:
    - model (str): Модель смартфон
    - manufacturer (str): Производитель смартфона
    - year_of_manufacture (int): Год выпуска смартфона
    """

    def __init__(self, model: str, manufacturer: str, year_of_manufacture: int):
        """
        Конструктор класса SmartPhone
        Параметры:
        - model: Модель смартфон
        - manufacturer: Производитель смартфона
        - year_of_manufacture: Год выпуска смартфона
        >>> smartphone = SmartPhone("iPhone X", "Apple Inc.", 2023)
        """
        if not isinstance(model, str) or len(model.strip()) == 0:
            raise TypeError("Модель смартфона должен быть непустой строкой.")
        if not isinstance(manufacturer, str) or len(manufacturer.strip()) == 0:
            raise TypeError("Производитель смартфона должен быть непустой строкой.")
        if not isinstance(year_of_manufacture, int) or year_of_manufacture < 1900:
            raise ValueError("Год выпуска смартфона должен быть больше или равен 1900.")

        self.model = model
        self.manufacturer = manufacturer
        self.year_of_manufacture = year_of_manufacture

    def get_model(self) -> str:
        """
        Метод для получения модели смартфона
        :return: Модель смартфона
        """
        return self.model

    def get_manufacturer(self) -> str:
        """
        Метод для получения производителя смартфона
        :return: Производитель смартфона
        """
        return self.manufacturer

    def get_year_of_manufacture(self) -> int:
        """
        Метод для получения года выпуска смартфона
        :return: Год выпуска смартфона
        >>> smartphone = SmartPhone("iPhone X", "Apple Inc.", 2023)
        >>> smartphone.get_year_of_manufacture()
        2023
        """
        return self.year_of_manufacture


class Tree:
    """
    Класс описывает дерево с основными характеристиками и методами

    Параметры:

    height : float
        Высота дерева в метрах
    age : int
        Возраст дерева в годах
    species : str
        Вид дерева

    Методы:
    
    grow(height_increase=0.05):
        Увеличивает высоту дерева на заданную величину
    get_info() -> dict:
        Возвращает информацию о дереве в формате словаря
    """

    def __init__(self, height: float, age: int, species: str):
        if height <= 0 or age < 0:
            raise ValueError("Высота и возраст дерева должны быть положительными числами.")
        self.height = height
        self.age = age
        self.species = species
        self.state = "живое"  # Может принимать значения "живое" или "срубленное".

    def grow(self, height_increase: float = 0.05) -> None:
        """
        Метод увеличивает высоту дерева на заданный прирост

        Аргументы:
        ----------
        height_increase : float, optional
            Прирост высоты за год (по умолчанию 0.05 метра)

        Исключения:

        ValueError:
            Если высота прироста отрицательная
        """
        if height_increase < 0:
            raise ValueError("Прирост высоты не может быть отрицательным числом.")
        self.height += height_increase

    def get_info(self) -> dict:
        """
        Метод возвращает информацию о дереве в формате словаря

        Возвращаемое значение:
        info : dict
            Словарь с информацией о высоте, возрасте, виде и состоянии дерева
        """
        return {
            "height": self.height,
            "age": self.age,
            "species": self.species,
            "state": self.state
        }


class Car:
    """
    Представляет автомобиль с маркой, моделью, пробегом и уровнем топлива

    Атрибуты:
        mark (str): Марка автомобиля
        model (str): Модель автомобиля
        mileage (int): Общий пройденный путь автомобилем в километрах. Должен быть неотрицательным
        fuel_level (float): Текущий уровень топлива в литрах. Должен находиться между 0 и емкостью бензобака
    """

    TANK_CAPACITY = 60  # литры
    KM_PER_LITER = 10  # Количество километров, которое автомобиль может проехать на 1 литр топлива

    def __init__(self, mark: str, model: str, mileage: int = 0, fuel_level: float = 0.0):
        """
        Инициализирует объект Car

        Аргументы:
            mark (str): Марка автомобиля
            model (str): Модель автомобиля
            mileage (int, optional): Начальный пробег. По умолчанию равен 0
            fuel_level (float, optional): Начальный уровень топлива. По умолчанию равен 0.0.

        Исключения:
            ValueError: Если пробег отрицательный или уровень топлива выходит за пределы допустимого диапазона.
        """
        self.mark = mark
        self.model = model
        if mileage < 0:
            raise ValueError("Пробег не может быть отрицательным")
        self.mileage = mileage
        if fuel_level < 0 or fuel_level > self.TANK_CAPACITY:
            raise ValueError(f"Уровень топлива должен быть между 0 и {self.TANK_CAPACITY}.")
        self.fuel_level = fuel_level

    def drive(self, distance: int) -> None:
        """
        Ведет автомобиль на указанное расстояние, обновляя пробег и уровень топлива.

        Аргументы:
            distance (int): Расстояние в километрах, которое необходимо проехать. Должно быть положительным.

        Исключения:
            ValueError: Если расстояние не положительное.
        """
        if distance <= 0:
            raise ValueError("Расстояние должно быть положительным")

        self.mileage += distance
        fuel_consumption = distance / self.KM_PER_LITER

        if fuel_consumption > self.fuel_level:
            raise ValueError("Недостаточно топлива для преодоления данного расстояния")

    def refill_tank(self) -> float:
        """
        Заправляет бензобак автомобиля до максимальной емкости

        Возвращает:
            float: Новый уровень топлива после заправки
        """
        self.fuel_level = self.TANK_CAPACITY
        return self.fuel_level

    def get_info(self) -> dict:
        """
        Возвращает информацию об автомобиле в виде словаря

        Возвращает:
            dict: Словарь, содержащий марку, модель, пробег и уровень топлива автомобиля
        """
        return {
            "mark": self.mark,
            "model": self.model,
            "mileage": self.mileage,
            "fuel_level": self.fuel_level
        }


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
