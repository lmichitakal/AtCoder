import sys
import math
from collections import *
from itertools import *
mod = 10**9 + 7
n, p = map(int, input().split())
#L = list(map(int, input().split()))
#l = [int(input()) for i in range(n)]
#ans = 0
#print(ans)
print((p-1)*pow(p-2,n-1,mod)%mod)