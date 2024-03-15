tup=(1,2,3,4,4,5)
print('Number of occurences :',tup.count(4))
print('Index :',tup.index(5))
print('Length of tuple :',len(tup))

lst=list(tup)
#lst.append('a')
print(lst)
print(type(lst))

tup=tuple(lst)
print(tup)
print(type(tup))

st=set(tup)
print(st)