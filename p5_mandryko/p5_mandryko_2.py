word = input("Введіть слова через пробіл ").split(" ")
for i in range(len(word)): 
    if word[i] == word[-1]:
        print("and " + word[i])
    if word[i] == word[-2]:
        print(word[i], end = ' ')
    elif word[i] != word[-1] and word[i] != word[-2]:
        print(word[i], end = ', ')
