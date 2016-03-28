'''
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
'''
def divisor(num):
    if (num > 1):
                        
            div_list=[x for x in range(1,num+1) if (num%x ==0)]
            if (len(div_list)==2):
                    print ("The number is prime as the only divisors are 1 and "+ str(num))
            else:
                    print("The divisor list is: "+ str(div_list))
    else:
            print ("The number 1 is neither Prime nor Composite and its only divisor is 1")

try:
        number = int(input('Enter a number:'))
        assert(number>0)
        divisor(number)
except ValueError:
        print('Please enter only NUMERIC values!!!')
except AssertionError:
        print('Please enter a Number Greater than 0!!!') 
