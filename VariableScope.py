# types of scope

# local
# global
# non local



# def add():
#     global x
#     x=10
#     print(x)
# add()
# print(x)    


# x=10
# def add():
#     x=50
#     print(x)
#     print(globals()['x'])
# add()    

# do not create scope

# if
# elif
# else
# try
# except
# while
# for


# x=int(input("Enter no:"))
# if(x>0):
#     z=10
# elif x<0:
#     z=50
# else:
#     z=100
# print(z)            


# create new scope

# function
# class


# HIGHER ORDER FUNCTION
# map()
# filter()
# reduces()
# decorator()


# map()

# Syntax:
# iterable1=
# iterable2=

# def functionname(n1,n2,_ _ _ _):
#     fun_body
# map(functionname,iterable1,iterable2)    



# l1=[1,2,3,4]
# l2=[5,6,7,8]
# l3=[1,2,3,4]
# def sum(n1,n2,n3):
#     return n1+n2+n3
# res=list(map(sum,l1,l2,l3))
# print(res)

# Filter
# syntax:
# iterable
# def fun_name(n):
#     conditional_statement
# res=list(filter(fun_name,iterable))

#EVEN

# l=[1,2,3,4,5,6,7,8,9]
# def even(n):
#     if n%2==0:
#         return n
# res=tuple(filter(even,l))    
# print(res)

#ODD

# l=[1,2,3,4,5,6,7,8,9]
# def odd(n):
#     if n%2!=0:
#         return n
# res=tuple(filter(odd,l))    
# print(res)



l=[1,2,3,4,5,6,7,8,9]
def comp(n):
    if n%2==0:
         return("even")
    elif n%2!=0:
        return("odd")
res=tuple(map(comp,l))
print(res)    
    