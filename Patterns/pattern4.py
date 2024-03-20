'''
*
##
123

'''
for i in range(3):
    for j in range(i+1):
        if i<1:
            print("*",end="")         
        elif i<2:
            print("#",end="")
        elif i<3:
            print(j+1,end="")
    print()