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



# n=int(input("Enter number"))
# mul=1
# i=1
# while i<=n:
#     if(i%2!=0):
#         mul=mul*i
#         if(i<n-1):
#             print(i,end="*")
#         else:
#             print(i,end="=")
#     i=i+1
# print(mul)    

# n=int(input("Enter any no:"))
# td=0
# while n>0:
#     td=td+1
#     n=n//10
# print(f"Total no of digits:{td}")


# n=int(input("Enter any no:"))
# sum=0
# while n>0:
#     td=n%10
#     sum=sum+td 
#     n=n//10
# print(f"SUM:{sum}")


#ARMSTRONG NUMBER

# n=int(input("Enter any number:"))
# x,y,td,sum=n,n,0,0
# while n>0:
#     td=td+1
#     n=n//10
# while x>0:
#     ld=x%10
#     sum=sum+ld**td
#     x=x//10
# if y==sum:
#     print("Armstrong")     
# else:
#     print("not armstrong")   


#POLLINDROME 

# n=int(input("Enter any no:"))
# rev,x= 0,n
# while n>0:
#     ld=n%10
#     rev=rev*10+ld
#     n=n//10
# if(x==rev):
#     print("pollindorme")
# else:
#     print("Not")        



#PATTERN

# n=5
# i=1
# while i<=n:
#     print("*"*5)
#     i=i+1

# n=5
# i=1
# while i<=n:
#     print("*"*i+' '*(n-i))
#     i=i+1


# n=5
# i=1
# while i<=n:
#     print(' '*(n-i)+"* "*i)
#     i=i+1



# n=5
# i=0
# while i<n:
#     print("*"*(n-i)+' '*i)
#     i=i+1



# n=5
# i=0
# while i<n:
#     print(" "*i+"*"*(n-i))
#     i=i+1


# n=5
# i=0
# while i<n:
#     print(" "*i+"-  "*(n-i))
#     i=i+1

# n=5
# i=0
# while i<n:
#     print("#"*i+" "*(n-i))
#     i=i+1
# i=i-2
# while i>0:
#     print("#"*i+" "*(n-i))    
#     i=i-1


# n=5
# i=0
# while i<n:
#     print(" "*(n-i)+"#"*i)
#     i=i+1
# i=i-2
# while i>0:
#     print(" "*(n-i)+"#"*i)    
#     i=i-1




n=int(input("enter no"))
i=0
while i<n:
    print(" "*(n-i)+"# "*i)
    i=i+1
i=i-2
while i>0:
    print(" "*(n-i)+"# "*i)    
    i=i-1