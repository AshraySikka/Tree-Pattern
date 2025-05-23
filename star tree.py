height=int(input("Enter the Height of the tree: "))
copyp=space=height-2
copys=star=1
copyh=height
while height>1:
    for i in range (space):
        print(" ", end='')
    for j in range (star):
        print("*", end='')
    height-=1
    space-=1
    star+=2
    print('')

for i in range(star-2):
    print(" ",end='')
    if i==(star-(copyh+2)):
        print('*', end='')

print('Option 2:\n')

for i in range(copyh,1,-1):
    print(' ' * copyp,'*' * copys)
    copyp-=1
    copys+=2
for i in range(star-2):
    print(" ",end='')
    if i==(star-(copyh+1)):
        print('*', end='')
