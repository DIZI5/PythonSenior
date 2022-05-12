class Student:
    print("Hi")
    amount_students = 0
    def __init__(self,name,health,age,lvl,power,race):
        self.name = name
        self.health = health
        self.age = age
        self.lvl = lvl
        self.power = power
        self.race = race
        print("I am alive!")
        Student.amount_students += 1

    def show(self):
        print(self.name)
        print(self.health)
        print(self.age)
        print(self.lvl)
        print(self.power)
        print(self.race)
    # def __del__(self):
    #     print("Student Deleted!")


First = Student(name=input("Enter Name: "), health=10, age=input("Enter Age: "), lvl=input("Enter Lvl: "), power=input("Enter Power: "), race=input("Enter Race: "))
First.show()
print("you create first g")

Second = Student(name=input("Enter Name: "), health=10, age=input("Enter Age: "), lvl=input("Enter Lvl: "), power=input("Enter Power: "), race=input("Enter Race: "))
Second.show()
print("you create second g")

# Second = Student(name="Kate",health=43)

# Second.__del__()



print(Student.amount_students)