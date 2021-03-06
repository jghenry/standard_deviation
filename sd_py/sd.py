#calculates standard deviation from a list of numeric values
def standard_deviation(x):
    n = len(x)
    mean = sum(x)/n
    ssq = sum((x_i-mean)**2 for x_i in x)
    stdev = (ssq/n)**0.5
    return(stdev)

#calcualtes standard error from a list of values	
def standard_error(x):
    return(standard_deviation(x)/len(x)**0.5)
