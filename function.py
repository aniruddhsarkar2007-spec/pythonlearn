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
