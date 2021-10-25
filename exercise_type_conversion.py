import datetime

current_year = datetime.date.today().year

birth_year = int(input('what is your birth year?'))

age = current_year - birth_year
print(f'your age is: {age}')
