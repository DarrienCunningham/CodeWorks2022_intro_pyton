# Project 3 - Control Statements

1. Read the meaty.py file and write below what each line of code does. Line 1 is giving you a prompt with a "yes" or "no" question, lines 3 and 4 are saying, if the answer is "yes" then you'll be shown the meat menu, lines 5 and 6 are saying if the answer is "no" then it will show the veggie menu, lines 7 and 8 are for if the user doesn't respond with "yes" or "no."

2. Write a code that will ask the user to enter two numbers and check if they are equal.
a = input("Enter the first number: ")
b = input("Enter the second number: ")
if a == b:
  print "Both inputs are equal"
else:
  print "Your input is not equal."

3. Write a code that will ask the user to enter an integer and checks if it is even or odd.
num = int(input("Enter a number: "))
if (num % 2) = 0
 print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))

4.  Write a code that will ask the user to enter their annual income and returns their federal tax bracket and how much they would pay in taxes.
10% <- $0 to $9,950
12% <- $9,951 to $40,525
22% <- $40,526 to $86,375
24% <- $86,376 to $164,925
32% <- $164,926 to $209,425
35% <- $209,426 to $523,600
37% <- $523,601 or more

num = int(input("Enter your annual income: "))
if num > 0 num <=9950:
print("You're in the 1st bracket. you will pay "+ str(num ))
elif num > 9951 and num <= 40525:
print("You're in the 2nd bracket. you will pay "+ str(num ))
elif num > 40526 and num <= 86375:
print("You're in the 3rd bracket. you will pay "+ str(num ))
elif num > 86376 and <= 164925
print("You're in the 4th bracket. you will pay "+ str(num ))
elif num > 164927 and num <= 209425
print("You're in the 5th bracket. you will pay "+ str(num ))
elif num > 209426 and num <= 523600
print("You're in the 6th bracket. you will pay "+ str(num ))
elif num > 523601
print("You're in the 7th bracket. you will pay "+ str(num ))


5. Write a program to accept a number from 1 to 7 and display the name of the day like 1 for Sunday , 2 for Monday and so on.
num = int(input("Enter a number between 1 and 7: "))
if num == 1:
print(Sunday")
if num == 2:
print("Monday")
if num == 3:
print(TUesday")
if num == 4:
print("Wednesday")
if num == 5:
print("Thursday"
if num == 6:
print ("Friday")
if num == 7:
print("Saturday")
