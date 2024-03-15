'''
List Methods :

            1)append 2)insert 3)extend 4)reverse 5)copy 6)pop
            7)remove 8)clear 9)index 10)sort 11)count
'''
a=[1,2,3,5,6,0,34,21,12,1,1]
b=['a','b']

a.append(7)         #adds a single element at the end of the list
a.insert(3,4)       #adds single element at given index
a.extend(b)         #put one list at the end of another list
print(a)

a.reverse()         #reverses all the elements of the given list
print(a)

c=a.copy()          #copies the whole list to another list
print('C List :',c)

c.pop()             #remove the last single element (if the index is not given)
c.pop(2)            #pops out element of given index
print(c)

c.clear()           #it only clears all the elements from the list
print('List C :',c)

del c               #it deletes the whole list

print(a.index(12))  #returns the position/index of given element

d=[11,56,2,3,4,4,5]
print(d)

d.sort()            #sorts int elements in an ascending order
print(d)            

print(d.count(4))   #counts the occurences of the given element