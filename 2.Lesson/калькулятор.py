print("1.Додавання")
print("2.Віднімання")
print("3.Множення")
print("4.Ділення")
print("")
action = input("Виберіть число від 1-4: ")

if action == "1":
    a = input("Введіть перше число: ")
    b = input("Введіть перше число: ")
    print(a, "+", b, "=", int(a) + int(b))

elif action == "2":
    a = input("Введіть перше число: ")
    b = input("Введіть перше число: ")
    print(a, "-", b, "=", int(a) - int(b))

elif action == "3":
    a = input("Введіть перше число: ")
    b = input("Введіть перше число: ")
    print(a, "*", b, "=", int(a) * int(b))

elif action == "4":
    a = input("Введіть перше число: ")
    b = input("Введіть перше число: ")
    print(a, "/", b, "=", int(a) / int(b))