"""

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""

def multiple_sum_finder(max):
    y = 0
    
    for x in range(0,max):
    	if x % 3 == 0:
    		y += x
    	elif x % 5 == 0:
    		y += x
    
    return y
    
print multiple_sum_finder(1000)

    