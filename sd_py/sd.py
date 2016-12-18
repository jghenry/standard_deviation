def standard_deviation(x):
   try: 
        n = len(x)
        mean = sum(x)/n
        ssq = sum((x_i-mean)**2 for x_i in x)
        stdev = (ssq/n)**0.5
    except Exception as e:
        raise
    else:
        return(stdev)
    
def standard_error(x):
    return(standard_deviation(x)/len(x)**0.5)
