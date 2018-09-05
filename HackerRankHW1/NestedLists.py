lowest = []
secLowest = []
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    if len(lowest) == 0:
        lowest = [[name, score]]
     #   print lowest[0][1]
    elif score < lowest[0][1]:
        secLowest = lowest
        lowest = [[name, score]]
    elif score == lowest[0][1]:
        lowest.append( [name, score] )
    elif len(secLowest) == 0:
        secLowest = [ [name, score] ]
    elif score < secLowest[0][1]:
        secLowest = [[name, score] ]
    elif score == secLowest[0][1]:
        secLowest.append( [name, score] )
names = [item[0] for item in secLowest]
for name in sorted(names):
    print name
