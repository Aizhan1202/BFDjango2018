import textwrap
def wrap(string, max_width):
    newStr = textwrap.dedent(string).strip()
    for width in [ max_width ]:
        newStr = textwrap.fill(newStr, width=max_width)
    return newStr

if __name__ == '__main__':
    string, max_width = raw_input(), int(raw_input())
    result = wrap(string, max_width)
    print result