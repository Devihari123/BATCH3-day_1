# ----> common functions for list
'''
l1=[6,7,8,9,0]
print(len(l1))
print(max(l1))
print(min(l1))

l1=[6,8,9,"p","u"]
print(max(l1)) # ---> error coz its a combination of int and string
print(min(l1)) # ---> error coz its a combination of int and string

l1=[6,7,8,9,0,8.89,-5,0.78]
print(min(l1)) #-5

l1=[6,7,8,9,0,8.89,-5,0.78]
# index() ---> to get index value of specific element
print(l1.index(9))

# some functions which is specifically used for list
# To add element inside list
# insert(index_value,element) ---> to add element at specific index position
l1=[6,6,6,7,8,9,0,8.89,-5,0.78]
l1.insert(2,"cars")
print(l1)

# To delete element from list
l1=[6,6,6,7,8,9,0,8.89,-5,0.78]
#pop() #---> last element will be deleted
l1.pop()
print(l1)

# pop(index_value) ---> used to delete element at specific index element
l1.pop(4) # 4 is index value
print(l1)

# remove(element) ---> used to delete element directly
l1.remove(8.89)
print(l1)
# clear() --> to complete delete all element in list
l1.clear()
print(l1)

# del --> To delete the list
del l1 # or del(l1)
print(l1)

# ---> join 2 lists
l1=[9,0,8]
l2=["p","o","t",34]
#print(l1+l2)

# extend() --> to combine 2 lists
l1.extend(l2)
print(l1)

# ----> copy()
l1=[6,7,8,9,3]
l2=l1.copy()
print(l2)
print(l1)

print(id(l1))
print(id(l2))

# --> Diff b/w shallow and deep copy
# Shallow copy
import copy
l1=[8,9,0,[5,6],[3,2,1]]
l2=copy.copy(l1)
l1.append(890)
print(l1)
print(l2)

# Deep copy ---> used to copy the list with nested list
import copy
l1=[8,9,0,[5,6],[3,2,1]]
print(l1[-1][1]) # --> to index nested list
l2=copy.deepcopy(l1)
l1.append(890)
print(l1)
print(l2)

# Sort --> Arrange elements in list in ascending or descending order
l1=[9,7,45,0,-6,5,12]
l1.sort() # To arrange in ascending order
print(l1)
l1.sort(reverse=True) # To arrange in decending order
print(l1)

l1=['z','i','o','p',9]
l1.sort()
print(l1) # --> error

# ---> list constructor
# list() --> To convert other collection datatype to list
l3=((8,9,0))
print(list(13))
l4=(8,9)
print(list(l4))

# --> Nested list
l1=[8,9,[0,8,7],["p","o",'y'],[8,'t']]
print(l1[-2][1]) # --> o

print(l1[1:4])
print(l1[1:-1])

# --> To delete "t" from l1
l1[-1].remove('t')
print(l1)

# combine these ["p","o",'y'],[8,'t'] lists in l1 to ["p","o",'y',8,'t']
l1[-2].extend(l1[-1])
l1.pop(-1)
print(l1)

# ----> Tuple
# char of tuple
   1) Tuple have to be surrounded by()
   2) The elements inside tuple are not ch
