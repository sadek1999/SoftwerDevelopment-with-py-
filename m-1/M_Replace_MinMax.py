
n= input()

arr=list(map(int,input().split()))


x =arr.index(max(arr))
y=arr.index(min(arr))

arr[x],arr[y] = arr[y],arr[x]

print(*arr)

