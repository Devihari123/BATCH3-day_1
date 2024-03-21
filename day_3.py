'''
n1=int(input("enter the length value:"))
n2=int(input("enter the breath value:"))
if n1==n2:
    print("it is square")
else:
    print("or not")
'''
'''
n=int(input("enter the value:"))
if n%5==0 and n%7==0:
    print("yes")
else:
    print("no")
'''
'''
price=int(input("enter the bike price:"))
total=0
if price>=100000:
    discount=price*(6/100)
    value=price-discount
    tax=value*(15/100)
    total=value+tax
else:
    tax=price*(5/100)
    total=price+tax
print("the onroad cost of bike is:",total)
'''
'''
a=9
b=0
c=3
if a>b and a>c:
    print("a is big")
elif b>a and b>c:
    print("b is big")
else:
=    print("c is big")
'''
'''
marks=int(input("enter the marks:"))
if marks<25:
    print("F")
elif(marks>=25 and marks<45):
    print("E")
elif(marks>=45 and marks<50):
    print("D")
elif(marks>=50 and marks<60):
    print("C")
elif(marks>=60 and marks<80):
    print("B")
elif(marks>=80):
    print("A")
else:
    print("fail")
'''
#----> short hand if else
#*RULES:
#1.statement inside the if condition have to be present at first.
#2.elif cannot be used in short hand if else.
#3.always it have to end with else.
#eg:
#a=9
#b=6
#if(a>b):
 #   print("A")
#else:
#    print("B")
#print("A")if a>b else print("B")
'''
char=input("enter the letter:")
if char=="a" or char=="e" or char=="i" or char=="o" or char=="u":
    print("is a vowel")
else:
    print("its consonant")
'''
'''
char=input("enter the char")
str1="aeiouAEIOU"
if char in str1:
    print("vowel")
else:
    print("consonant")
'''
'''
char=input("enter the char:")
str1="aeiouAEIOU"
print("vowels")if char in str1 else print("consonant")
'''
'''
--->elif ladder using short hand if else
eg:
a=8
b=5
c=9
print("Ais greater")if a>b and a>c else print("B is greater") if b>c and b>a else print("C is greater")
'''
#------> looping concept:
##for loop
##while loop
#FOR LOOP:
 #  1. it is used for iteration,if we know the number of times the loop have to run.
 #   2.it is used to iterate the iterables eg:str,list,tupple,etc.
'''
 SYNTAX FOR LOOP:
     for loop syntax in c:
         for(i=0;i<10:i++){
             print("hello")
             }
    for loop syntax in python:
        for userdefined variable in range(start,end,step):#defuit step value=1.
'''
'''
for i in range(1,11):
    print(i)
    print("hello")   
for i in range(1,5,3):
    print(i)
'''
'''
for i in range(10,0,-1):
    print(i)
'''
'''
---->7 multiplication:
for i in range(21,44):
    print(i*7)
'''
'''
for i in range(1,11):
    print('7','x',i,'=',i*7)
    ans="7x{}={}"
    print(ans.format(i,i*7))
    print(f"7x{i}={i*7}")
'''
'''
eg:
BREAK:which is used to terminate the loop
for i in range (1,10):
    if i==3:
       break
     print(i)
'''
'''
for i in range(1,10):
    print(i)
    if i==6:
        break
'''
'''
for i in range(1,10):
    if(i==6):
        print(i)
        break
'''
'''
#--->CONTINUE STATEMENT:
for i in range(1,10):
    if i ==6:
        continue
    print(i)
'''
'''
---->print the even number between the 21 to 40
for i in range(20,40):
     if i%2==0:
        print(i)
'''
'''
fact=1
for i in range(1,10):
    fact=fact*i
    print("factorial is :",fact)
'''
#write a program to display sum of odd numbers and even
#numbers that fall between 12 and 37(including both numbers).
#--->while loop:
#it is udes when the number of times the loop have to run to iterate the non iterable elements while loop is udes.
#i=0
#while i<11:
#    print(i)
#    i+=1
'''
i=11
while i>0:
    print(i)
    i-=1#dcrement
'''

    



























































