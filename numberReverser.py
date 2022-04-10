input = int(input("Input a number: "))
rev_num = 0


def reverseTheNumber(number):
    global rev_num
    if (number > 0):
        remainder = number % 10
        rev_num = (rev_num * 10) + remainder
        reverseTheNumber(number // 10)

    return rev_num


print(reverseTheNumber(input))