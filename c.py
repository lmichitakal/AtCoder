def main(n, m, k, A, B):
    a = [0]
    b = [0]

    for i in range(n):
        a.append(a[i] + A[i])
    for i in range(m):
        b.append(b[i] + B[i])

    ans, j = 0, m
    for i in range(n+1):
        if a[i] > k:
            break
        else:
            while b[j] > k - a[i]:
                j -= 1
            ans = max(ans, i + j)

    return ans

if __name__ == "__main__":
    n, m, k = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = main(n,m,k,A,B)
    print(ans)