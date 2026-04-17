# when the no of iteration is not known we will use while loop


# SYNTAX
# startpoint
# while termenating point:
# _________
# _________
# increment/decrement



# while True:
#     print("hello")

# n=5
# i=1
# while i<n:
#     print(i,end=" ")
#     i=i+1

# n=int(input("enter value"))
# i=1
# while i<=n:
#     if (i<n):
#         print(i,end=",")
#     else:
#         print(i)
#     i=i+1    

# n=int(input("enter value"))
# i=1
# while i<=n:
#     if (i<n):
#         print(i,end="+")
#     else:
#         print(i)
#     i=i+1    

# n=int(input("enter value"))
# sum=0
# i=1
# while i<=n:
#     sum=sum+i
#     if (i<n):
#         print(i,end=",")
#     else:
#         print(i,end="=")
#     i=i+1    
# print(sum)    

# n=int(input("enter value"))
# mul=1
# i=1
# while i<=n:
#     mul=mul*i
#     if (i<n):
#         print(i,end="*")
#     else:
#         print(i,end="=")
#     i=i+1    
# print(mul)    

# n=int(input("Enter number"))
# i=1
# while i<=n:
#     if(i%2==0):
#         if(i<n-1):
#             print(i,end=",")
#         else:
#             print(i)
#     i=i+1


# n=int(input("Enter number"))
# i=1
# while i<=n:
#     if(i%2==0):
#         if(i<n-1):
#             print(i,end="+")
#         else:
#             print(i)
#     i=i+1


# n=int(input("Enter number"))
# sum=0
# i=1
# while i<=n:
#     if(i%2==0):
#         sum=sum+i
#         if(i<n-1):
#             print(i,end="+")
#         else:
#             print(i,end="=")
#     i=i+1
# print(sum)



# n=int(input("Enter number"))
# mul=1
# i=1
# while i<=n:
#     if(i%2==0):
#         mul=mul*i
#         if(i<n-1):
#             print(i,end="*")
#         else:
#             print(i,end="=")
#     i=i+1
# print(mul)


# n=int(input("Enter number"))
# i=1
# while i<=n:
#     if(i%2!=0):
#         if(i<n-1):
#             print(i,end=",")
#         else:
#             print(i)
#     i=i+1


# n=int(input("Enter number"))
# i=1
# while i<=n:
#     if(i%2!=0):
#         if(i<n-1):
#             print(i,end="+")
#         else:
#             print(i)
#     i=i+1


# n=int(input("Enter number"))
# sum=0
# i=1
# while i<=n:
#     if(i%2!=0):
#         sum=sum+i
#         if(i<n-1):
#             print(i,end="+")
#         else:
#             print(i,end="=")
#     i=i+1
# print(sum)    



n=int(input("Enter number"))
mul=1
i=1
while i<=n:
    if(i%2!=0):
        mul=mul*i
        if(i<n-1):
            print(i,end="*")
        else:
            print(i,end="=")
    i=i+1
print(mul)    