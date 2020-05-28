'''
    Numbers Triangle
'''
def number(n):
	for n in range(n+1):    # (n+1) for print upto given number
		print(str(n)*n)

number(int(input('Enter how many lines:')))
