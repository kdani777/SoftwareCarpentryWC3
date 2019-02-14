#Mundane Math - Script adds together all the even numbers between 1 and 100
#Will be a for loop from 1-100, with conditional, if i is even it will be added to a special list of even numbers
#The if statement will test for a remainder either equal to 0 (even) or 1 (odd) and concatenate accordingly

import math
numbers = range(100)
scale = 2.0
even = 0
even_list = ''
odd = 0
odd_list = '' #Why can't we concatenate an integer or floating point number to a list?

#need to cast i as float like x=float(i) where i=i from the range
for i in range(0,101):
	x=float(i)
	if (x % 2)== 0: # % Modulus operate - Gives remainder of left value divide by right value
		even += x
		even_list += str(x)
	else:
		odd += x
		odd_list += str(x)

print("The sum of all even numbers from 0 to 100 is" , even)
#print(even_list)
print("The sum of all odd numbers from 0 to 100 is" , odd)
#print(odd_list)
