s=input().split()
arr=[]

for x in s:
    arr.append(x[::-1])

print(" ".join(arr))    