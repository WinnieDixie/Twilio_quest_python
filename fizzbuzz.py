import sys

inputs = sys.argv

for i in range(len(inputs)):
    if(i > 0):
        num = int(inputs[i])
        if num % 3 == 0 and num % 5 == 0:
            print('fizzbuzz')
        elif num % 5 == 0:
            print('buzz')
        elif num % 3 == 0:
            print('fizz')
        else:
            print(num)
            
#inputs = list of all arguments to my script

#for each input in the list, do the following:
    #convert the input to a number
    #set my print string equal to a blank/empty string
    #if the number is divisible by 3, append "fizz" to the output string
    #if the number is divisible by 5, append "buzz" to the output string
    #if by now the output string is still blank, set it to the input number
    #print the output string
