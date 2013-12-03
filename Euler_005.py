"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def Divisibility_Test(input):
	x = input
	i = input / 2
	while i < input:
		if x % i != 0:
			x += input 
			i = 11
			continue
		else: i+=1 
		
	return x
	
print Divisibility_Test(20)