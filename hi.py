# for i in range (0,2):
#     print(i)

x=int(input("Enter how many number you want to subtract:"))
arr=[]
for i in range (0,x):
     number=int(input(f"Enter {i} number:"))
     arr.append(number)
r=arr[0]
for i in arr[1:]:
     r=r-i
print(r)
 