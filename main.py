
words = input('Enter the list: ').split()

are = ['a', 'r', 'e']
idxlst = []

for i in range(len(words)):
    idxlst.append(words[i].find(are[j]) for j in range(len(are)))
print(idxlst)

# ******************************
# Make your Code
# ******************************

# print the words that has 'a', 'r', 'e' in sequence

