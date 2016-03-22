from datetime import date
def caluclateCentYear(curr_age):
	diff_in_age = 100 - curr_age
	curr_year=int(date.today().year)
	cent_age = curr_year + diff_in_age
	return cent_age

name = input("Enter your Name:")
cur_age = int(input("Enter Your Age:"))
des_age = caluclateCentYear(cur_age)
print ("Hello "+name+", You will turn Hundred in " + str(des_age))
