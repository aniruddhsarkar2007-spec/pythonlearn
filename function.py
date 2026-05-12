# FUNCTION
# write ones call multiple time
# code reusable

# Syntax:
#   --------------
#     Decleration
#   --------------  
#     Calling
#   -------------- 


# required: def,function_name,(),:

# optional: parameter,argument,return (for termenating the function)    
 
 
# def add():
#     print("Addition is:",5+6)
#     return
# add()
# print(add())
#pep8
 

# In built function

# print()
# id()
# input()
# type()
# len()

# User Defined function

# with return-
# with argument
# without argument


# without return-
# with argument
# without argument

# Without argument with return
# def add():
#     return "hello"
# add()
# print(add())


# def great():
#     return "Welcome"
# great()
# print(great())

# # Without argument without return
# def i():
#     print("hello")
# i()
# print(i())

# def great():
#     print("Welcome")
# great()
# print(great())    


# # With argument with return
# def i(a,b):
#     x=a+b
#     return(x)
# i(3,4)
# print(i(3,4))

# def great (name):
#     return f"welcome{name}"
# x=input("Enter name:")
# print(great(x))



# With argument without return
# def i(a,b):
#     x=a+b
#     print(x)
# i(3,4)
# print(i(3,4))

# def great (name):
#     print(f"welcome{name}")
# x=input("Enter name:")
# great(x)


# Relation between parameter and argument:-

# positional argument
# default positional argument
# variable length argument            (*args)     COMES UNDER PACKING AND UNPACKING
# keyword positional argument
# keyword default positional argument
# variable length keyword argument    (**kwargs)  COMES UNDER PACKING AND UNPACKING 

# PACKING-*args
# UNPACKING-**kwargs

# def show(x,y,z):
#     print("X",x)
#     print("Y",y)
#     print("Z",z)
# show(10,20,30)    -> positional argument
# show()            default positional argument
# show(10)                 \\
# show(10,20)               \\
# show(10,20,30)             \\
# show(10,20,30,40) -> variable length 


# 8/5/26
# default positional argument

# def add(x=0,y=0,z=0):
#     print(x+y+z)
# add()   
# add(10) 
# add(10,20)
# add(10,20,30)

# variable length argument   (*args)

# Syntax:
# def functionname (*args):
#     print(args)
#     print(type(args))
# functionname(args)
# functionname(args1,args2,args3)    


# def display(*n):
#     print(n)
#     print(type(n))
# display()
# display(10,20)
# display(10,20,"python","java ")    \

# def display(*n):
#     sum=0
#     for i in n:
#         sum=sum+i
#     print(sum)
# display(10,20,30,40,50,60)
# display()          


#   * holds value in format of tuple
# def display(*n):
#     print(n)
#     print(type(n))
# values=eval(input("Enter all val:"))    
# display(*values)

# * works on packing and unpacking in list and tuple 


# keyword positional argument

# def add(x=0,y=0,z=0):
#     print("X:",x)
#     print("Y:",y)
#     print("Z:",z)
# add(z=10,y=50,x=20)    
# add()
# add(x=19)
# add(z=10,x=20)


# def add(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
# add()
# add(x=10,y=20,z=100,p=30,q=21)    


# def add(**kwargs):
#     sum=0
#     for i in d:
#         sum+=kwargs.get(i)
#     print(sum)
# d={"x":10,"y":23,"z":33}
# add(**d)


# REDUCE FUNCTION

#suntax:
# iterable
# def fun_name(n1,n2):
#     fun_body
# res = functools.reduce(fun_name,iterable)    


# import functools
# l=[1,2,3,4,5]
# def add(a,b):
#     return a+b
# res=functools.reduce(add,l,0)
# res=functools.reduce(add,l)
# print(res)


# # Max
# import functools
# l=[19,34,554,65,765,43]
# def max(a,b):
#     if(a>b):
#         return a
#     else:
#         return b
# res = functools.reduce(max,l)
# print(res)    

# Min
import functools
l=[19,34,554,65,765,43]
def min(a,b):
    if(a<b):
        return a
    else:
        return b
res = functools.reduce(min,l)
print(res)    