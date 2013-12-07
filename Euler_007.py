"""

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""
import math

def prime_check(input):
	if input == 2:
		return True
	if input == 3:
		return True
	if input % 2 == 0:
		return False
	if input % 3 == 0:
		return False
		
	max_poss_factor = int(round(math.sqrt(input))) 
	
	for i in range(5, max_poss_factor + 1):
		if input % i == 0:
			return False
	return True


def prime_iterator(limit):
	counter = 2
	current = 5
	
	while counter < limit:
		if prime_check(current) == True:
			counter += 1
			current += 1
		elif prime_check(current) == False: 
			current += 1
	return "current prime" + str(current - 1) + " " + "Prime value" + str(counter)

print prime_iterator(10001)

