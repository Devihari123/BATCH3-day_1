'''
#while loop
#break using while loop
#eg:1--->iterate from 20 to 30 and break the loop in 27.
i=20
while i<31:
     if i==27:
        break
     print(i)
     i+=1---->21 to 26
'''
'''
i=20
while i<31:
    print(i)
    if i==27:
        break
    i+=1---->21 to 27
'''
'''
i=20
while i<31:
    if i==27:
        print(i)
        break
    i+=1---->only 27
'''
#continue
#eg:1
'''
i=20
while i<31:
    if i==27:
        continue
    print(i)
    i+=1
'''
'''
i=20
while i<31:
     i+=1
     if i==27:
      continue
     print(i)
'''
#while to iterate from 12 to 22
#find the sum of all number
'''
i=12
sum=0
while i<23:
    sum=sum+i
    print(sum)
    i=i+1
    '''
#find the average of value from 20 to 25
'''
i=20
sum=0
while i<26:
    sum=sum+i
    avg=sum/6
    i+=1
print(avg)
    
i=20
sum=0
count=0
while i<=30:
    sum=sum+i
    count+=1
    i+=1
print(sum/count)

#-----> nested for loop
for i in range(1,3):
    for j in range(1,4)
        print(i,j)
'''
#eg:2
#****
#****
#****
#****
'''
for row in range(1,5):
    for col in range(1,5):
        print(row,col)
        
for row in range(1,5):
    for col in range(1,5):
        print("*",end=" ")
    print()
    
#---->n nuber of rows and col
row=int(input("enter the row:"))
col=int(input("enter the col:"))
for row in range(row):
    for col in range(col):
        print("row,col",end=" ")
    print()
    
for row in range(1,5):
    for col in range(1,5):
        print(row,end=" ")
    print()

sum=0
for row in range(1,5):
    for col in range(1,5):
        sum=sum+1
        print(sum,end="   ")
    print()
    
#---> to print stars in right angle triangle
for row in range(1,7):
    for col in range(row,7):
        print("*",end=" ")
    print()

for row in range(6):
    for col in range(6):
        if col==0 or col==5 or row==0 or row==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
for row in range(0,5):
    for col in range(1,6):
        if((row==0 and col==3)or (row==1 and(col>=2 and col<=4))or(row==2 and(col>=1 and col<=5))):
            print("*",end=" ")
        else:
             print(" ",end=" ")
    print()
'''
#---->DATA TYPES:
'''
1.primary
2.number--->int,float,complex.
3.string.
4.boolean.
5.none.
6.collection-->list,tupple,set,dictionary.
---->LIST:
if the colect of elements are sorounded by square brackets.
EG:
l1=[4,7,9,"hello",7+9j,[8,9,0]]
----->CHARACTERISTICS OF LIST:
1.list have to be sorounded by[]
2.it is mutable(the elements in the list are changable)
3.every element inside the lidt is indexed.
4.the elements inside list will be oreded format.
5.it can hold duplicate values.6.its heterogrous.
---->TO ACCEES THE ELEMENTS IN LIST
lst1=[1,4,6,7,89.7,7.5,"p","i"]
print{lst1)
------>INDEXING:
1.the collection datatyoes like list,tupple,string,the elements will be
alloted with predefineds unique value called index value.
---->we have 2 types of indexting.
1.positive indexing.--->starts with 0 from left hand side.
2.negative indexing.--->starts with -1 from right hand side.
---->POSITIVE INDEXING:
list=[1,4,6,7,89.7,7.5,"p","i"]
print(list[0])
print(list[4])
print(list[20])--->error
--->negative indexing
list=[1,4,6,7,89.7,7.5,"p","i"]
print(list[-1])
print(list[-5])
---->SLICING:

list=[1,4,1,7,89.7,7.5,"p","i"]
#lst1[start_index:end_index"step]
print(list[0:4])
print(list[6:8])
print(list[5:])
print(list[-7:-1:2])
#print(list[0:7:2])#print(list[0:7]) both are same

#trail=int(input())
'''

l1=[9,8,0,5]
l1.append("hello")
print(l1)













    


















