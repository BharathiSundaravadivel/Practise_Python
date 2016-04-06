'''
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
Logic -> This program will only display a palindrome if the words in a sentence remain same backwards and forwards.
For Example -> "Won Now" is a palindrome but "Malay alam" is not.
'''

string = input("Enter a String:")
length = list(map(len,string.split()))
s=''.join(string.split())
print("The String is a Palindrome" if s[::1]==s[::-1] and length[::1]==length[::-1] else "The String is not a Palindrome")
    
