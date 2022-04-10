# word = input("Enter a word: ")
# global newStr

# def sort(string):
#     letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
#     for x in letters:
#         for y in string:
#             if x == y:
#                 newStr += x
#     return newStr

# print(sort(word))

# Different approach

word = input("Enter a word: ")
print(''.join(sorted(word)))