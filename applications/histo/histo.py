# Your code here
with open("robin.txt") as f:
    words = f.read()

bad = ['\"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&', '!', '?']


for i in bad:
    words = words.replace(i, '').lower()

words = words.replace('\n', ' ')

words = list(words.split(' '))

words = [i for i in words if i != '']

count = {}

for i in words:
    if i not in count:
        count[i] = '#'
    else:
        count[i] += '#'

vsort = sorted(count.keys(), key=lambda s: len(count.get(s)))

rsort = [i for i in reversed(vsort)]

for i in range(len(rsort)):
    print(f"{rsort[i]:{15}}: {count[rsort[i]]}")
