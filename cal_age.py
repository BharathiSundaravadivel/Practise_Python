from datetime import date
def caluclateCentYear(curr_age,name,num):
        diff_in_age = 100 - curr_age
        curr_year=int(date.today().year)
        cent_age = curr_year + diff_in_age
        if (num==0):
                print("Number Cannot be Zero")
                return
        else:
                print ("\nPrinting "+str(num)+" Times\n")
                printNum(num,name,cent_age)
                printNumMultLine(num,name,cent_age)
                return
    

def printNum(number,name,cent_age):
        i=1
        while(i<=number):
                        print ("Hello "+name+", You will turn Hundred in " + str(cent_age)+"\n")
                        i+=1
        print("Printed the Lines "+": "+str(number) + " times\n")
        
def printNumMultLine(number,name,cent_age):
        i=1
        while(i<=number):
                        print ("Hello "+name+",\nYou will turn Hundred in\n" + str(cent_age)+"\n")
                        i+=1
        print("Printed the Lines "+": "+str(number) + " times in Multiple Lines")
        

name = input("Enter your Name:")
cur_age = int(input("Enter Your Age:"))
num =int(input("Enter a number:"))
caluclateCentYear(cur_age,name,num)
