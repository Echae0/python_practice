sentence = "Python is awesome"
vowel = ['a', 'e', 'i','o', 'u']

count = 0

for i in sentence:
    if i in vowel:
        count += 1

print("모음 개수: ",count)