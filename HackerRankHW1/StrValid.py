if __name__ == '__main__':
    s = raw_input()
    strg = list(s)
    b1 = False
    b2 = False
    b3 = False
    b4 = False
    b5 = False
    for s in strg:
        if s.isalnum():
            b1 = True
        if s.isalpha():
            b2 = True
        if s.isdigit():
            b3 = True
        if s.islower():
            b4 = True
        if s.isupper():
            b5 = True

    print b1
    print b2
    print b3
    print b4
    print b5
