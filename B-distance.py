num, K = input().split()
num = int(num)
K = int(K)

ans = 0

for n in range(num):
    x, y = input().split()
    x = int(x)
    y = int(y)
    # print(x)
    if x*x + y*y <= K*K:
        ans += 1

print(ans)
