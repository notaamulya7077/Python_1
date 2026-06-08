from car import Car

car1 = Car("Camaro", 2024, "red", False)
car3 = Car("Corvette", 2025, "black", True)
print(car3.year)
print(car3.model)
print(car3.color)
print(car3.for_sale)

car1.stop()
car3.stop()
