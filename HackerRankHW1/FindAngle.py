# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
AB = float(raw_input())
BC = float(raw_input())

print(str(int(round(math.degrees(math.atan2(AB, BC)))))+'°')