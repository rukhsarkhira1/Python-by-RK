'''
Set Methods : 1)add 2)update 3)copy 4)clear 5)discard 6)remove 7)pop
              8)issubset 9)issuperset 10)isdisjoint
              11)union 

              12)difference 13)difference_update

              14)intersection 15)intersection_update

              16)symmetric_difference 17)symmetric_difference_update
        

'''

a={'a','b','c','d','e','f'}
b={'r','k'}

a.add('z')          #adds single element
a.update({11,22})   #to add multiple elements at a time

c=a.copy()          #copies one set to another

c.clear()           #makes the whole set empty

a.discard('d')      #removes single given element
a.remove('b')       #removes single given element

c=a.pop()           #removes random single element

print(b.issubset(a))    # checks whether one set is a subset of another
print(a.issuperset(b))  # checks whether one set is a superset of another
print(a.isdisjoint(b))  # checks whether two sets are completely having different elements from each other

print('Union :',a.union(b),'\n')    #merges all the elements from 2 given sets (No repeated elements)


set1={11,22,33,44}
set2={33,44,55}

diff_set=set1.difference(set2)      #returns different elements , skips the common ones
print("Different elements in set1 than set2 :",diff_set)

set1.difference_update(set2)
print(set1)

common_elements=set1.intersection(set2)     #returns common elements between two sets
print("Common elements :",common_elements)

set1.intersection_update(set2)
print(set1)


sym_diff=set1.symmetric_difference(set2)       #returns only different elements from two given sets , skips the common ones
print(sym_diff)

set1.symmetric_difference_update(set2)
print(set1,set2)


