import re

def word_count(s):
    # Your code here
    bad = ['\"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
    
    for i in bad:
        s = s.replace(i, '')

    s = s.lower()
    
    regex = re.compile(r'[\n\r\t]')

    s = regex.sub(" ", s)

    words = {}

    wordList = list(s.split(' '))

    wordList = [i for i in wordList if i != '']

    # wordList = wordList.remove('')

    # if '' in wordList:
    #     wordList.remove('')

    for w in wordList:
        if w in words:
            words[w] += 1
        else:
            words[w] = 1

    return words
    # return 'pass'



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('a a\ra\na\ta \t\r\n'))