
words = input('Enter the list: ').split()

are = ['a', 'r', 'e']
idxlst = []
idx = []

for i in range(len(words)):
    for j in range(len(are)):
        idx.append(words[i].find(are[j]))
        if idx[len(idx)-1] == -1 or idx[len(idx)-1] < idx[len(idx)-1]:
            break
        else:
            idxlst.append(words[i])
print(idxlst)

# ******************************
# Make your Code
# ******************************

# print the words that has 'a', 'r', 'e' in sequence

