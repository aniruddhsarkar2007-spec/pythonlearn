# CHANGE CHARACTER TO ASCII VALUE -ord()
# ASCII TO CHARACTER - chr()
# s=input("Enter string:")
# x=ord(s)
# print(x)
# y=x+1
# print(y)
# print(chr(y))

# ch=input("Enter value")
# print(chr(ord(ch)+2))

# s="python"
# s1=""
# for ch in s:
#     s1=s1+chr(ord(ch)+1)
# print(s1)


# l=[10,20,30,40,50]
# l1=[]
# for i in l:
#     l1.append(i+5)
# print(l1)    

# l=[1,3,2,4,5]
# l1=[]
# for i in l:
#     l1.append(i*i)
# print(l1)    

# t=(1,2,3,4,5)
# l=list(t)
# # print(l)
# l1=[]
# for i in l:
#     l1.append(i+5)
# t=tuple(l1)
# print(t)   

# l=[1,2,3,4,5]
# for i in range (len(l)):
#     x=l[i]+5
#     l[i]=x
# print(l)

# d={"x":10,"y":20,"z":"python"}
# for i in d:
#     print(i,"=",d[i])

# d={"x":10,"y":20,"z":"python"}
# for i in d:
#     print(d[i])

# d={"x":10,"y":20,"z":"python"}
# for i in d.values():
#     print(i)

# d={"x":10,"y":20,"z":"python"}
# for i in d.keys():
#     print(i)


# d={"x":10,"y":20,"z":"python"}
# for i,j in d.items():
#     print(i,"=",j)


# s={10,20,30,"python","java"}
# for i in s:
#     print(i)

# n=int(input("Enter no:"))
# for i in range (1,n+1):
#     # print("*"*i+" "*(n-i))
#     # print(" "*(n-i)+"*"*i)  
#      print(" "*(n-i)+"0 "*i) 


# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="" )
#     print()        

# n=int(input("Enter no: "))
# x=2
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(x,end=" ")
#         x=x+2
#     print()        

# n=eval(input("Enter no:"))
# for i in range (1,n+1):
#     ch="A"
#     for j in range(1,i+1):
#         print(ch,end=" ")
#         ch=chr(ord(ch)+1)
#     print()    


# n=(input("Enter no:"))
# ch="A"
# for i in range (1,n+1):
    
#     for j in range(1,i+1):
#         print(ch,end=" ")

#         ch=chr(ord(ch)+1)
#     print()    


#-------------------TRANSFER STATEMENT----------------------

# n=int(input("Enter a no:"))
# i=1
# while i<=n:
#     if(i==1):
#         pass
#     else:
#         print(i)
#     i=i+1    


# n=int(input("Enter a no:"))
# i=1
# while i<=n:
#     if(i==5):
#         continue
#     else:
#         print(i)
#     i=i+1    

# n=int(input("Enter a no:"))
# i=1
# while i<=n:
#     if(i==5):
#         break
#     else:
#         print(i)
#     i=i+1    


# for i in range (1,10):
#     if(i==5):
#         break
#     else:
#         print(i)
# print("Hello")        


# while True:
#     print("1. Addition\n2. Substraction\n3. Multiplication\n4. Division\n5. OFF\n")
#     n=int(input("Enter any one option mention above:"))
#     num=[1,2,3,4,5]
#     if n in num:
#         if n==1:
#             x=int(input("Enter how many no you want to add:")) 
#             sum=0
#             for i in range (1,x+1):
#                 number=int(input(f"Enter {i} number:")) 
#                 sum=sum+number
#             print("ADDITION iS:",sum)    
#     else:
#         print("Please enter valid no:")

   

while True:
    print("1. Addition\n2. Substraction\n3. Multiplication\n4. Division\n5. OFF\n")
    n=int(input("Enter any one option mention above:"))
    num=[1,2,3,4,5]
    if n in num:
        if n==1:
            x=int(input("Enter how many no you want to add:")) 
            l=[]
            sum=0
            for i in range (1,x+1):
                number=int(input(f"Enter {i} number:")) 
                l.append(number)
                sum=sum+number
            print(f"ADDITION OF GIVEN NO {l} is:",sum)    

        elif n==2:
            pass
        elif n==3:
            pass
        elif n==4:
            pass
        elif n==5:
            break


    else:
        print("Please enter valid no:")




   
