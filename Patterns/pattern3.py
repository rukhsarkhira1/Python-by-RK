'''
54321
4321
321
21
1

'''
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(i,end="")
        i-=1
        
    print()