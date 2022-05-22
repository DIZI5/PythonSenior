# ----- Успадкування Основного класа -----

 class Human:
     height = 180
     satiety = 50

 class Student(Human):
     pass

 class Worker(Human):
     satiety = 80

 nick = Student()
 stas = Worker()

 print(nick.satiety)
 print(stas.satiety)

 class Elfs(Human):
    pass

 class Gnoms(Human):
    pass

 class Mags(Human):
    pass

# Дочірні - класи які успадкованні.

#  ----- Успадкування успадкованних класів -----

 class Grandparent:
     height = 170
     satiety = 100
     age = 60

 class Parent(Grandparent):
     age = 40

 class Child(Parent):
     height = 150
     def __init__(self):
         print(self.height)
         print(self.satiety)
         print(self.age)

 nick = Child()

# ----- Функція super() -----

 class Hello:
     def __init__(self):
         print("Hello!")

 class Hello_World(Hello):
     def __init__(self):
         super().__init__()
         print("World!") 


 hi = Hello_World()

#  ----- Множинне Успадкування -----

# class Computer:
#     def __init__(self):
#         super().__init__()
#         self.memory = 128

# class Display:
#     def __init__(self):
#         super().__init__()
#         self.resolution = "4k"

# class SmartPhone(Display,Computer):
#     def show(self):
#         print(self.memory)
#         print(self.resolution)

# phone = SmartPhone()
# phone.show()