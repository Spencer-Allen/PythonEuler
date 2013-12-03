"""

The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""


def find_sum_of_squares(input):
	input += 1
	holder = 0
	for x in range(0,input):
		holder += (x ** 2)  
	return holder
	
def find_square_of_sum(input):
	sum = (input * (input + 1))/2
	return sum ** 2
	

print find_square_of_sum(100) - find_sum_of_squares(100)
