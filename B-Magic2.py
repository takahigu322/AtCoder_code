#import random

nums = input().split()

a = int(nums[0])
b = int(nums[1])
c = int(nums[2])

K = input()
k = int(K)

# print(type(a))#output=int

# print(k)#output=int

cnt = 0

# print(type(cnt))#output=int

while a >= b:
    cnt += 1
    b *= 2

while b >= c:
    cnt += 1
    c *= 2


if cnt <= k:
    print("Yes")
else:
    print("No")


# for hoge in range(1,k +1):
#	print(hoge)
# print(random.choice(nums))

# print(A)
