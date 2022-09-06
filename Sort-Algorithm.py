test = ["saliba", 'stew', "sunday", "staff", "aminu", "annam"]
test1 = ['john', 'family', 'stew', 'bizini', "Anderson", "Jenny"]

def charSort(word1, word2):
    if (len(word1) <= len(word2)):
        for i in range(len(word1)):
            if word1[i].lower() == word2[i].lower():
                continue
            elif (word1[i].lower() > word2[i].lower()):
                return [word2, word1]
            else:
                return [word1, word2]
    else:
        return charSort(word2, word1)

def sorted(List):
    print(List)
    for i in range(len(List) - 1):
        for j in range(len(List) - 1):
            List[j], List[j+1] = charSort(List[j], List[j+1])
    
    print(List)

sorted(test)
sorted(test1)