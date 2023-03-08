# Emad Abbasi #2095022
print('Birthday Calculator')
print('Current day')
current_month = int(input())
current_day = int(input())
current_year = int(input())
print('Month:', current_month)
print('Day:', current_day)
print('Year:', current_year)
# now for the birthdate
print('Birthday')
birth_month = int(input())
birth_day = int(input())
birth_year = int(input())
print('Month:', birth_month)
print('Day:', birth_day)
print('Year:', birth_year)
current_age = int(current_year - birth_year)
if current_month == birth_month and current_day == birth_day:
    print('Happy Birthday!')
elif current_month < birth_month:
    current_age = current_age - 1
elif current_month == birth_month:
    if current_day <= birth_day:
        current_age = current_age + 1
print('You are', current_age, 'years old.')
