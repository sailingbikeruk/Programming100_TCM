# User Input

x = input("Give me a number: " ) # this accepts strings as an input
y = input("Give me another number: ") # this accepts strings as an input
print(x + y) # if you do this you are doing contatenation on two strings
print(int(x) + int(y)) # to do the maths you need to c onvert the strings to integers usign the int() method

# The problem with the method above is that you wuold get an error if someone entered a real (float) number
# it might be better to set the type at the input


x = float(input("Give me a number: " )) # this accepts a real number as an input
y = float(input("Give me another number: ")) # this accepts real number as an input
print(x + y) # now you get the correct answer and an error only of the operator enters a non-number


