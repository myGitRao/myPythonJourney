# Function : Reusability, defined by keyword def , return type , input & output
# In maths as x * y = z is function, similarly in python
# Docstring : for 100 lines of code, if someone has written some function,
# you can always check what does the function does by printing the doc string

def myFunction (a,b):
    """This function does addition of 2 numbers
Any comment which is written inside function in first line with triple quotes is known as Docstring"""
    print(a+b)
    return a + b

def myFunction2 (a,b):
    print(a+b)

myFunction(4,7)
print(myFunction2(4,7)) # Prints None as it doesnt hve return type

print(myFunction.__doc__)







