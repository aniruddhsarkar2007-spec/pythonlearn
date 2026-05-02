n=int(input("Enter any no:"))
for i in range (1,n+1):
    print(" "*(n-i)+"*"*i)

# n=int(input("Enter no:"))
# for i in range (1,n+1):
#     print("*"*i+" "*(n-i))

n=int(input("Enter any no:"))
for i in range (1,n+1):
    print(" "*(n-i)+"*"*i)

    
l=eval(input("Enter any tuple:"))
print(l.index(2))
print(l.count(3))      


s="!!!Python!!!"
print(s.strip("!"))
print(s.lstrip("!"))
print(s.rstrip("!"))


l={"name":"Aniruddh","age":18}
h={"class":"BCA","city":"Bhopal"}
l.update(h)
print(l)


d={"name":"A","class":"bca"}
d.setdefault("age",17)
print(d)

