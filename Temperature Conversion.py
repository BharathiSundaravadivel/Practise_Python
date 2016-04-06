'''Write two functions that will convert temperatures back and forth from the Celsius and Fahrenheit temperature scales.
The formulas for making the conversion are as follows:

  Tc=(5/9)*(Tf-32)
  Tf=(9/5)*Tc+32
where Tc is the Celsius temperature and Tf is the Fahrenheit temperature.
If you finish this assignment quickly, add a function to calculate the wind chill.'''

x = 1
while(x == 1):
    choice = input("To Convert a temperature to the desired format, choose (F) for Fahrenheit or (C) for Celsius \nEnter (E) to exit (Program will continue otherwise!!!)\n")
    proper_choice = choice.upper()
    if(proper_choice == "C"):
        temperature= float(input("Enter Temperature:"))
        temp_cel = (5/9)*(temperature-32)
        print("The Temperature in Celsius is "+ str(temp_cel)+"\n\n")
    elif(proper_choice == "F"):
        temperature= float(input("Enter Temperature:"))
        temp_fht = ((9/5)*temperature)+32
        print("The Temperature in Fahrenheit is "+ str(temp_fht)+"\n\n")
    elif(proper_choice == "E"):
        x = 0
    else:
        print("Enter a Valid Choice \n")
