def myfibonacci(N):
    if N == 0: 
    	return 0
    elif N == 1: 
    	return 1
    else: 
    	return myfibonacci(N-1)+myfibonacci(N-2)

