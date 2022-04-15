sentence = input("Enter a sentence:  ")
# sentence = "Web Development Tutorial"
longest = max(sentence.split(), key=len)
print("The longest string is: " + longest)
print("Its length is: {}".format(len(longest)))