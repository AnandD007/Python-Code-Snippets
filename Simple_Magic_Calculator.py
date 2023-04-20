'''
Simple Calculator using eval() function:
Note: eval() function is something we shouldn't be using (in general) in our python code, 
because it can evaluate anything that is passed as its parameter, meaning it can actually 
calculate all multiplication, division, addition and subtraction as well as exponential and the 
calculating remainder as well. But it has a dark side too that we need to avoid, that is eval() 
function can actually run any python command that passed as its parameter even if its as simple 
as print() it will execute the command so as the security point of view we shouldn't be using it 
so we used Regex here to eliminate all the letters and keep only numerical characters.
'''
import re

#First, we imported the Regex library, and some output for a user and define a variable like 
#run = True and previous = 0. In while we called our performMath() function we created before.
#Since while is checking run so it’s an infinite loop.

print("Our Magical Calculator")
print("Type x to close")

previous = 0
run = True
def performMath():     # In the first two lines of performMath() we used global keywords so that
    global run         # the run and previous variable we will use in the function we referred as
    global previous    # a global variable instead of function local variable.
    equation = ""
    if previous == 0:
        equation = input("Enter Equation: ")
    else :
        equation = input(str(previous))


    if equation == 'x':
        print("GoodBye!!!")
        exit(0)
    else:
        equation = re.sub('[a-zA-Z,:()" "]',"",equation)
        
    if previous == 0:
        previous = eval(equation)
        print("\nResult:",previous)
    else:
        previous = eval(str(previous) + equation)

while run:
    performMath()
    
  #performMath() is our important component of the program as it the one 
  # performing all the operations.
