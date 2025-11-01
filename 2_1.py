class car:
    def __init__(self, make, model, year, color):
         self.make=make
         self.model=model
         self.year=year
         self.color=color
         self.speed=0

car1=car("Toyota","Camry",2023,"Red")
car2=car("Frod","Mustang",2025,"Black")

print(car1.make)
print(car1.model)
print(car1.year)
print(car1.color)
print(car2.year)
