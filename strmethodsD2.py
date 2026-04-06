#STRING METHODS
# s=input("Enter any string:")
# print(s.lower())
# print(s.upper())
# print(s.title())
# print(s.swapcase())
# print(s.startswith("P"))
# print(s.endswith('n'))
# print(s.capitalize())
# print(s.index("h"))
# print(s.spllit())
# print(s.join())



# DYNAMIC COUNT

# s=input("Enter any string:")
# ch=input("Enter any character:")
# print(s.count(ch))
 

# start=int(input("Enter start point:"))
# stop=int(input("Enter stop point:"))
# print(s.index(input("Enter any character:"),int(input("Enter start point:"),int(input("Enter stop point:")))))


# SYNTAX OF SPLIT
# string.split(From where to break,How many times to break)

# s="this is python"
# print(s.split())
# print(s.split('p'))
# print(s.split(' ',2))
# print(s.split(' ',0))

#-----------JOIN--------------
#ITERABLE MEANS COLLECTION

# s1="PYTHON"  
# s2="JAVA"
# s3="PHP"   
# x=','.join([s1,s2,s3])
# print(x)


s="!!!Python!!!"
print(s.strip("!"))
print(s.lstrip("!"))
print(s.rstrip("!"))