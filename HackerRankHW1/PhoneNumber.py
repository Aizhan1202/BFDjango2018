# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
import re
numbers = []
n = raw_input()
for i in range(int(n)):
    numbers.append(raw_input())
for n in numbers:
    if ((int(list(n)[0]) == 9 or int(list(n)[0]) == 8 or int(list(n)[0]) == 7)and len(list(n)) == 10):
        print 'YES'
    else:
        print 'NO'
"""
import re
n = raw_input()
for i in range (int(n)):
    if re.match(r'[789]\d{9}$',raw_input()):
        print 'YES'
    else:
        print 'NO'
