#Functions - a reusable block of code

# define a function to print using a f string
def who_am_i(name, age):
    print(f"My name is {name} and I am {age} years old")

who_am_i("Ian",35)

# def a function to add an amount to a given n umber 
def add_one_hundred(num):
    print(num+100)

add_one_hundred(5)
add_one_hundred(200)

# define a fucntion to add two numbers together
def add(x,y):
    print(x + y)

add(2,2)

# define a function that returns the result to the calling code for later use
def multiply(x,y):
    return x * y

result= multiply(5,5)
print(result)

# define a function to find the square root of a given number
def square_root(x):
    print(x ** .5)

square_root(64)