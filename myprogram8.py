def some_age(age):
    new_age = age + 15
    return new_age
get_age = int(input("Enter your age: "))
if get_age<85:
    print(some_age(get_age))
else:
    print("Invalid age, Enter correct age!")
