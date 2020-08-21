#program to check whether entered number is a pangram or not
def pangram(str):
    str=str.lower()
    lst=list(str)
    lst1=list()
    for i in lst:
        if i.isalpha():
            if i not in lst1:
                lst1.append(i)
    #pangram contains all alphabets
    if len(lst1)==26:
        print('is a pangram')
    else:
        print('not a pangram')
p=input('enter the string:')
pangram(p)
