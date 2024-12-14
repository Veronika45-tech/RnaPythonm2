from task_1 import SmartPhone, Tree, Car


smartphone = SmartPhone("iPhone X", "Apple Inc.", 2023)
tree = Tree(5.0, 10, "Дуб")
car = Car("Toyota", "Camry", 10000, 30.0)

try:
    SmartPhone("iPhone X", "Apple Inc.", 1899)
except TypeError as e:
    print(f"Ошибка при создании SmartPhone: {e}")

try:
    tree.grow(-0.1)
except ValueError as e:
    print(f"Ошибка при вызове grow(): {e}")

try:
    Car("Toyota", "Camry", -1, 30.0)
except ValueError as e:
    print(f"Ошибка при создании Car: {e}")
