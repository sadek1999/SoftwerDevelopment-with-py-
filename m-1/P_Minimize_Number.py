n = int(input())
# print(type(n),n)
all = list(map(int, input().split()))
operations = 0
x =all
a = True
while a:
    if a:
       for i,y in enumerate(x):
         if y % 2 != 0:
             a = False
             break
         else:
            x[i]=int(y/2)
       if a:
          operations+=1
              
      
    

print(operations)
