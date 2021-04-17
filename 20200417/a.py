import sys
import math
from collections import *
from itertools import *
#n = int(input())
x, y, z = map(int, input().split())
#L = list(map(int, input().split()))
#ans = 0
#print(ans)
s = y/x
print(max(0,math.ceil(s * z)-1))