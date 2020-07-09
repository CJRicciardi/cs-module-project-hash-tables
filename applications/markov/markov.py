import random
import re

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
regex = re.compile(r'[\n\t\r]')
words = regex.sub(' ', words)
words = list(words.split(' '))
words = [i for i in words if i != '']

bad = ['\"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']

follow = {}

for i in range(len(words)-1):
    if words[i] not in follow:
        follow[words[i]] = [words[i + 1]]
    else:
        follow[words[i]].append(words[i + 1])

starts = []
stops = []

for i in range(len(words)):
    if words[i][0].isupper() == True:
        starts.append(words[i])
    elif words[i][0] == '\"' and words[i][1].isupper() == True:
        starts.append(words[i])
    elif words[i][-1] is '.' or words[i][-1] is '?' or words[i][-1] is '!':
        stops.append(words[i])
    elif words[i][-1] is '\"' and (words[i][-2] is '.' or words[i][-2] is '?' or words[i][-2] is '!'):
        stops.append(words[i])
    else:
        pass

# print(stops)

# TODO: construct 5 random sentences
# Your code here
for i in range(5):
    print(f'\nSentence {i+1}:')
    s = random.choice(starts)
    while s not in stops:
        print(s, end=' ')
        s = random.choice(follow[s])
    print(s)