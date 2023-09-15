def listToStr(list):
    ret = ''
    for i in range(len(list)):
        str = list[i]
        if(i == len(list) - 1):
            ret += 'and ' + str
        else:
            ret += str + ', '

    print(ret)

spam = ['apples', 'bananas', 'tofu', 'cats']

listToStr(spam)