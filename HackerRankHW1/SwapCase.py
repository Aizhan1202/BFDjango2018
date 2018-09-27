def swap_case(strg):
    words = ''
    for s in strg:
        if s.isupper() == True:
            words += (s.lower())
        else:
            words += (s.upper())
    return words

if __name__ == '__main__':
s = raw_input()
result = swap_case(s)
print result