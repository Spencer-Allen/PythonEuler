"""
Palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91*99. 
Find the largest palindrome made from the product of two 3-digit numbers
"""

def test_palindrome(input):
	string = str(input)
	if string == string[::-1]:
		return True
	else:
		return False
		
def find_largest_factor(input):
	x = input
	while x > input * .9:
		y = input
		while y > input * .9:
			product = x * y
			if test_palindrome(product) == True:
				return product
			print product
			y = y - 1
		x = x - 1

print find_largest_factor(999) 