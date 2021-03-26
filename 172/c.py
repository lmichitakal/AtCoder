n, m, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = [0]
b = [0]

for i in range(n):
    a.ppend(a[i] + A[i])
for j in range(m):
    b.ppend(b[j] + B[j])

ans, j = 0, m

for i in range(n):
    if a[i] > k:
        break
    else:
        while a[i] + b[j] > k:
            j -= 1
        ans = max(ans, i + j)

print(ans)