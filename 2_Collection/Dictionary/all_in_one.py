'''
Dictionary methods :
                    1)keys 2)values 3)items 4)get 5)pop 6)popitem
                    7)update 8)clear

'''

dict1={'a':'apple','b':'banana','c':'cat'}
dict2={'d':'dog','e':'elephant'}

print(dict1.keys())             #To get only keys
print(dict1.values())           #To get only values
print(dict1.items())            #To get both keys & values

print(dict2.get('k','Not Found !'))       #To get a value for given key

dict2['f']='Frog'                         #To add single value
dict2.update({'K':'Kite','L':'Lion'})     #To add multiple value
print(dict2)

dict2.pop('K')      #Removes single item of given key
print(dict2)

dict2.popitem()     #Removes the last item from the dictionary
print(dict2)



