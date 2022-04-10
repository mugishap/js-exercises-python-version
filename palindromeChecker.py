palindrome = input("Enter a word to be checked: ")


def strrev(string):
    return string[::-1]


if strrev(palindrome) == palindrome:
    print("Word entered is a palindrome")
else:
    print("Word entered is NOT a palindrome")