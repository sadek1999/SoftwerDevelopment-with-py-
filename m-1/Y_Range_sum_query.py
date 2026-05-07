n,q=map(int,input().split())
arr = list(map(int,input().split()))

for _ in range(q):
    x,y=list(map(int,input().split()))
    sum(arr[x-1:y])
    print(sum)

