'''
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number 
react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If 
not, print a different appropriate message.
'''
def divideByNum(num,div):
    rem = float(num)%div
    if (div!=2 and div!=4):
        if(rem==0):
            print("The number "+str(num)+ " is Divisible by "+str(div))
        else:
            print("The number "+str(num)+ " is Not Divisible by "+str(div))
    elif (div==2):
        if(rem==0):
            print("The number "+str(num)+ " is Even")
        else:
            print("The number "+str(num)+ " is Odd")
    elif (div==4):
        if(rem==0):
            print("The number "+str(num)+ " is a Multiple by 4!!!")
        else:
            print("The number "+str(num)+ " is Not a Multiple by 4!!!")

number = int(input("Enter the number to be Divided:"))
divisor = int(input("Enter the number to check the Divisibilty test:"))
divideByNum(number,divisor)

        
