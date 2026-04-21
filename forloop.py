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

s="python"
s1=""
for ch in s:
    s1=s1+chr(ord(ch)+1)
print(s1)
