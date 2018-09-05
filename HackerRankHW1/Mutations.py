def mutate_string(string, position, character):
    newStr = string[:position] + character + string[position+1:]
    return newStr

if __name__ == '__main__':
    s = raw_input()
    i, c = raw_input().split()
    s_new = mutate_string(s, int(i), c)
    print s_new