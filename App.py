import datetime

user_age = int(input("Enter your birth year:  "))
current_age = datetime.datetime.now().year
birth_year = current_age - user_age

print(f"your age is {birth_year} years old")