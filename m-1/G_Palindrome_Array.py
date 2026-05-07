t = int(input())

element=input().split()
arr=[]

for i in range(t):
   arr.append(int(element[i]))


if(arr == arr[::-1]):
   print("YES")
else:
   print("NO")  
    