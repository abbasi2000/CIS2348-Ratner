# 2095022 #EMADABBASI
# PASSWORD MODIFIER
# first replacing characters with specials
password = input()
password = password.replace('i', '!')
password = password.replace('a', '@')
password = password.replace('m', 'M')
password = password.replace('B', '8')
password = password.replace('o', '.')
# appending
password += 'q*s'

print(password)

