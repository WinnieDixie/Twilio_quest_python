import sys

n1 = float(sys.argv[1])
n2 = float(sys.argv[2])

sum = n1 + n2

if(sum <= 0):
    print('You have chose the path of destitution.')
elif(sum <= 100):
    print('You have chosen the path of plenty.')
elif(sum > 100):
    print('You have chosen the path of excess.')
