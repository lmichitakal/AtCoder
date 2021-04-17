import sys
import math
from collections import *
from itertools import *
#n = int(input())
a, b = map(int, input().split())
#L = list(map(int, input().split()))
#l = [int(input()) for i in range(n)]
#ans = 0
#print(ans)
s = b-a
ans =1
for i in range(1,b+1):
    if a%i == 0:
        x = a
    else:
        x = math.ceil(a/i) * i
    if x + i <= b:
        ans = i
print(ans)