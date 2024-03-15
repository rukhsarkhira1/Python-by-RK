data={1:'RK',2:'Camila',3:'Michael'}

#print(data[1])
#print(data.get(2))
#print(data.get(55,'Not found'))

keys=['Navin','Kiran','Harsh']
values=['python','java','javascript']
data=dict(zip(keys,values))

data['Monica']='CS' #adding
del data['Harsh']   #deleting

#print(data)





prog ={'JS':'Atom','CS':'VS','Python':['pycharm','sublime'],'java':{'JSE':'Netbeans','JEE':'Eclipse'}}

print(prog['Python'][1])    # [0] = pycharm , [1] = sublime
print(prog['java'])
print(prog['java']['JEE'])

