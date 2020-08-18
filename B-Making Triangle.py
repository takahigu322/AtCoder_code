N = input()
N = int(N)

huga = list(map(int, input().split()))  # mapでint変換、mapをlist変換,
huga.sort()  # リストの並び替え昇順
print(huga)
ans = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            a = huga[i]
            b = huga[j]
            c = huga[k]

            if a == b or b == c or c == a:
                continue

            if a + b > c:
                ans += 1

print(ans)
