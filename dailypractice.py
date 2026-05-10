    
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

def show(x,y,z):
    print("X",x)
    print("Y",y)
    print("Z",z)
# show(10,20,30)    -> positional argument
# show()            default positional argument
# show(10)                 \\
# show(10,20)               \\
# show(10,20,30)             \\
# show(10,20,30,40) -> variable length 


s=input("Enter your name:")
print(s)
print(f'Type of {s} is {type(s)}')
print(f'ID of {s} is {id(s)}')
print(f'Max of {s} is {max(s)}')
print(f'Min of {s} is {min(s)}')


# inbuilt function of python in string 
s=input("Enter your name:")
print(s)
print(f'Type of {s} is {type(s)}')
print(f'ID of {s} is {id(s)}')
print(f'Max of {s} is {max(s)}')
print(f'Min of {s} is {min(s)}')

 l=[1,2,3,4,5,6]
# l.remove(3)
# print(l)


l=[1,2,3,4,5,6]
l.sort(reverse=True)
print(l)

#l.pop(3)
#print(l)

#l.sort()
#print(l)

#l.reverse()
#print(l)







#copy()
# clear()
# append()
# extend()
# insert()
# pop()
# remove()
# sort()
# reverse()
# coutn()



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