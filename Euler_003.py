"""

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""
import math

def prime_factorizer(input):
	#creates a list of factors of the input number
	factors = []
	d = round(math.sqrt(input))
	
	while d > 1:
		if input % d == 0:
			factors.append(int(d))
		d = d - 1
	#checks each factor for prime-ness and removes ones that fail
	for x in factors[:]:
		g = round(math.sqrt(x)) 
		while g > 1:
			if x % g == 0:
				factors.remove(x)
			g = g - 1
	return factors
		 

print prime_factorizer(600851475143)
