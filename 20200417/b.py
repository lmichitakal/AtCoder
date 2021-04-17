import sys
import math
from collections import *
from itertools import *
#n = int(input())
n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
#l = [int(input()) for i in range(n)]
A = set(A)
B = set(B)
ans = []
#print(ans)
for b in B:
    if b in A:
        continue
    else:
        ans.append(b)
for b in A:
    if b in B:
        continue
    else:
        ans.append(b)
if len(ans) == 0:
    print()
    sys.exit()
ans.sort()
ans =[str(x) for x in ans]
print(" ".join(ans))