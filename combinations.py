word = input("Enter a word and its combinations will be generated:\t")


def combinationGenerator(string, index, n, answer):
    if (index == n):
        print(answer)
        return
    combinationGenerator(string, index + 1, n, answer + string[index])
    combinationGenerator(string, index + 1, n, answer)


combinationGenerator(word, 0, len(word), '')
