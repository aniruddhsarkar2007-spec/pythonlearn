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

n=int(input("Enter no:"))
for i in range (1,n+1):
    # print("*"*i+" "*(n-i))
    # print(" "*(n-i)+"*"*i)  
     print(" "*(n-i)+"0 "*i) 