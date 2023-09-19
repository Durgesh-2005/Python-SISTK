# To take input from the user
a = int(input('Enter value of a: '))
b = int(input('Enter value of b: '))
#if a is 10 & b is 52 
a=a+b  #from 10 to 62
b=a-b  #from 52 to 10
a=a-b  #from 62 to 52
print('The value of a after swapping: {}'.format(a))
print('The value of b after swapping: {}'.format(b))
