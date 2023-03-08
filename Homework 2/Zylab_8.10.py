# 2095022 # EMAD ABBASI
# checking for palindromes
# Bob, race car, malayalam

def is_palindrome(s):
    s = s.replace('', '')  # removing spaces
    s = s.lower()  # lower casing like we upper cased in previous lab

    return s == s[::-1]  # this steps checks if the reverse equals the original string


if __name__ == '__main__':
    s = input()

    if is_palindrome(s):
        print(s, 'is a palindrome')
    else:
        print(s, 'is not a palindrome')
