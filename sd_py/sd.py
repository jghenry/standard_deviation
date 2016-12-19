def standard_deviation(x):

	"""
	This function calculates the standard deviation of a list.
	Input: list of numeric values.
	Output: standard deviation.
	"""
    n = len(x)
    mean = sum(x)/n
    ssq = sum((x_i-mean)**2 for x_i in x)
    stdev = (ssq/n)**0.5
    return(stdev)
    
def standard_error(x):
    return(standard_deviation(x)/len(x)**0.5)
