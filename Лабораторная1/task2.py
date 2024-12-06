from task_1 import Phone, Tree, Car


phone = Phone("iPhone X", "Apple Inc.", 2023)
tree = Tree(5.0, 10, "Дуб")
car = Car("Toyota", "Camry", 10000, 30.0)

try:
    Phone("iPhone X", "Apple Inc.", 1899)
except ValueError as e:
    print(f"Ошибка при создании Phone: {e}")

try:
    tree.grow(-0.1)
except ValueError as e:
    print(f"Ошибка при вызове grow(): {e}")

try:
    Car("Toyota", "Camry", -1, 30.0)
except ValueError as e:
    print(f"Ошибка при создании Car: {e}")
