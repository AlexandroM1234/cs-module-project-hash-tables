# Your code here

with open("robin.txt") as f:
    words = f.read()

word_count = {}

list_word =  words.split(" ")

to_remove = '":;,.-+=/\|[]{(})*^&'
for char in to_remove:
    words = words.replace(char, "")

for word in list_word:
    lowercase = word.lower()
    if lowercase not in word_count:
        word_count[lowercase] = 1
    else:
        word_count[lowercase] += 1

for pairs in word_count.items():
    print (pairs)