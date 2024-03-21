#--->swaping of variables
#EG:1
#a=7
#b=5
#temp=a
#a=b
#b=temp
#print(a,b)
#EG:2
#a=7
#b=5
#a,b=b,a
#print(a,b)
'''
a=5
b=7
a=a+b
b=a-b
a=a-b
print(a,b)
a=5
b=7
a=a*b
b=a/b
a=a/b
print(int(a),int(b))
'''
#---->Is the constant value assigned to a variable and a variable is consider to be constant when it is defines in caps.
#a=4
#b=5
#print(a)
#print(id(a))
#import keyword
#print(len(keyword.kwlist))
#print(type(keyword.kwlist))
#---->to check if the string is keyword or not
#
#if=8
#print(keyword.iskeyword("sid")) #false
#if=8
#print(if)#error coz if is a keyword
#----->literals:
#a=8#a is a variable
#A=78#A is a constant
# ---->hash:it creates a hash value for constant datatypes and provides error for non constant datatypes.
#n1=89.78
#rint(hash(n1))
#n1=93+2j
#print(hash(n1))
#f1=[7,8,9]
#print(hash(f1))
'''
a=9
b=9
print(id(a))
print(id(b))
'''
#operators are synbols which is used to perform various operations between 2 or more operands.
#* arithmatic
#*logical
#*relational or comparison
#*bitwise
#*assignment
#*identity
#*membership
#---->arithmatic:-,+,*,/,//,**
#eg:
#a=8
#b=6
#c=9
#print(a+b+c)
#input()---->used to get the runtime input
#n1=int(input("enter the value"))
#print((type(n1)))
#n1=eval(input("enter the value"))
#print((type(n1)))
#a=4
#b=2
#print(a/b)
#print(a%b)
#print(3**2)
#ASSIGNMENT OPERATOR:+-=,-=,*=,//=,**=,&=,|=,%=
'''
a=2
a+=8
print(a)
a=9
a*=2
print(a)
'''
#comparison operator:==,<,>,!=,<=,>=
"""
a=8
b=7
print(a>b)
a=7
b=4
print(a&b)
"""
#a=10
#print(~a)
#a=9
#print(~a+2)
#BITWISE OPERATOR:&,|,^,~,<<,>>
'''
AND:
a=7
b=4
print(a&b)
OR:
a=7
b=4
print(a|b)
TILDA:
a=5
print(~a)
print(<<,>>)
print(5>>3)
'''
'''
LOGICAL OPERATORS: and , or , not
and:
a=6
print(a>3and aa,10)
print(a>7 or a<30)
print(a>8 and a<10)
print(not(a>8 and a<10))
IDENTITY:it is used to compare the memory location that the values are stored.
a=8
b=8
print(aisb)
print(a==b)
MEMBERSHIP OPERATORS:
l1=[1,2,3,4,5]
num=3
print(num in L1)
num=8
print(num in L1)
num=26
print(2 in num)#error
CONDITIONAL STATEMENTS:if,elif,else
eg:1
if condition:
    statement
    statement
'''
"""
eg:2
a=6
if a:
   print("hello")
a=6
if a>3:
    print("yes")
else:
    print("no")
a=0
if a:
    print("yes")
else:
    print("no")
a=None
if a:
    print("yes")
else:
    print("no")
a=False
if a:
    print("yes")
else:
    print("no")
a=" "
if a:
    print("yes")
else:
    print("no")
"""
#n=int(input("enter the value:"))
#if n %2==0:
 #   print("n, is even")
#else:
#    print("n, is odd")
#name,age,nationality
#18above,indian
'''
name=input("enter the name:")
age=int(input("enter the age:"))
nationality=input("enter the natio:")
if age>=18 and nationality=="indian":
    print("eligible for vote")
else:
    print("not eligible for vote")
'''

    


    
     
    
