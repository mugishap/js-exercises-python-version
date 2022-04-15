sentence = input("Enter a sentence here:  ")
# sentence = "The quick brown fox"
count = 0
vowels = ('a', 'e', 'i', 'o', 'u')
for x in sentence:
    for y in vowels:
        if y == x:
            count += 1


print("The number of vowels is: {}".format(count))