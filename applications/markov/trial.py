words = "Atticus said to Jem one day, “I’d rather you shot at tin cans in the backyard, but I know you’ll go after birds. Shoot all the blue jays you want, if you can hit ‘em, but remember it’s a sin to kill a mockingbird.” That was the only time I ever heard Atticus say it was a sin to do something, and I asked Miss Maudie about it. “Your father’s right,” she said. “Mockingbirds don’t do one thing except make music for us to enjoy. They don’t eat up people’s gardens, don’t nest in corn cribs, they don’t do one thing but sing their hearts out for us. That’s why it’s a sin to kill a mockingbird."

words = list(words.split(' '))
words = [i for i in words if i != '']

starts = []
stops = []

for i in range(len(words)):
    # if words[i][0].isupper() == True:
    #     starts.append(words[i])
    # elif words[i][0] == '\"' and words[i][1].isupper() == True:
    #     starts.append(words[i])
    if words[i][-1] is '.' or words[i][-1] is '?' or words[i][-1] is '!':
        stops.append(words[i])
    elif words[i][-1] is '\"' and (words[i][-2] is '.' or words[i][-2] is '?' or words[i][-2] is '!'):
        stops.append(words[i])
    else:
        pass

print(stops, 'stops')
# print(starts, 'starts')