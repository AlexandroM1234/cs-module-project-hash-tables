import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# Read file is one giant string so we have to split them
# Returns a list of strings
split_words = words.split()

# TODO: analyze which words can follow other words
# Your code here
# Set up a dictionary with the first word as they then value is a list of possible next words
dataset = {}
# Loop throught the list of stringg
for i in range(len(split_words)-1):
    word = split_words[i]
    next_word =  split_words[i+1]
    # if word is not in the dataset word is the key next word is the value
    if word not in dataset:
        dataset[word] = [next_word]
    # if it is in the dataset append the next word to the current word
    else:
        dataset[word].append(next_word)
# Make a list of start words
# If first/second character is capitalized, put into list
# Loop over our split_words and put any start word into a list

# You can add a .keys() to your Hashtable class
start_words =[]
for key in dataset.keys():
    if key[0].isupper() or len(key) > 1 and key[1].isupper():
        start_words.append(key)
word = random.choice(start_words)

# TODO: construct 5 random sentences
# Your code here
stopped = False

stopped_words = "?.!"
while not stopped:
    print(word, end=" ")
    # choose a random following word
    # if its a stop word set stopped to True
    if word[-1] in stopped_words or len(word) > 1 and word[-2] in stopped_words:
        stopped = True
    following_words = dataset[word]
    word = random.choice(following_words)

