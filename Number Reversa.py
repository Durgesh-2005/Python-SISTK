#Program to display the reversal of a number
Number = int(input("Enter a number: "))
Reverse = 0
while(Number > 0):
    Reminder = Number%10
    Reverse =(Reverse*10) + Reminder
    Number = Number//10
print("\nReverse of Entered Number is:",Reverse) 