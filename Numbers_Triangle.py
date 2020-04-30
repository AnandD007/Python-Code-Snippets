'''
    Numbers Triangle
'''
def number(n):
	count=1
	for n in range(n+1):    # (n+1) for print upto given number
		print(str(n)*n)
		for j in range(0,n):
			count=count+1
number(int(input('Enter how many lines:')))
