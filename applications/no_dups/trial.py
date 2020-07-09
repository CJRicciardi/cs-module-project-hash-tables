start = [1, 2, 3, 4, 5, 6]

test = [3, 7, 6, 8]

for i in range(len(test)):
    if test[i] not in start:
        start.append(test[i])

print(start)