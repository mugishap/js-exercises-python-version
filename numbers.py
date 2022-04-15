numbers = input("Enter numbers: ")
array = numbers.split(",")
newArr = []
for x in array:
    newArr.append(int(x))

newArr.remove(max(newArr))
newArr.remove(min(newArr))
print("The second largest in the array is: {}".format(max(newArr)))
print("The second smallest in the array is: {}".format(min(newArr)))
