# Variables and methods

age = 35 # age is the variable, 35 is the value, the data type is integer
print(age)

# variables are mutable, they can vary in value...
age = 36 # age is the variable, 35 is the value, the data type is integer
print(age)

# Methods
age = 35 #Integer
name = "Ian" #String
gpa = 3.7 #Float

print(int(age)) # prints the contents of the variable age as an integer
print (int(35.9)) # this only picks the integer part, it does nto do any rounding

quote = "all fair in love and war"
print(quote.upper()) # prints quote in all upper case
print(quote.capitalize()) # Capitalises the first letter
print(quote.title()) # title case
print(len(quote)) # prints the string length
print(type(quote)) # prints the data type

print("my name is "+ name +" and I am "+str(age)+ "years old." ) # convert age to a string using the str method
 # print("my name is "+ name +" and I am "+age+ "years old." ) # You cant concatenate an int in a string

age += 1 # increment the contents of age by 1
print (age)

Birthday = 1 #assign the incrementor to a variable
age += Birthday # use the variable instead of the value
print(age)
