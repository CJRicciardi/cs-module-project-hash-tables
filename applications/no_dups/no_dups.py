def no_dups(s):
    # Your code here
    slist = list(s.split(' '))

    flist = []

    for i in range(len(slist)):
        if slist[i] not in flist:
            flist.append(slist[i])


    out = " ".join(flist)

    # return out
    return out



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))