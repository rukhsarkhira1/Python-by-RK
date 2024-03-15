list1=['rk','alice','lilly']
list2=[1,55,8.6,74,12,4,89,36]
mix=[list1,list2]


#print(list1[0:])
#print(list2[-2])

list1.append(450)
list1.insert(1,'Hello')
list1.extend([2,5,96,87,41,52])

list1.remove('alice')
list1.pop()
list1.pop(-2)
del list1[8:]

#print(list1)

#print(min(list2))
#print(max(list2))
#print(sum(list2))

list2.sort()    #ascending
list2.reverse() #decending

#print(list2)
#print(list2.index(55))

a=[1,3,5,5,5]
b=a.copy()
print(b)

print(b.count(5))   #count the occurences of 5

c=[100,200,300]
a.extend(c)
print(a)

d=[a+c]
print(d)




