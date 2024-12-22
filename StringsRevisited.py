# More about Strings

my_name = "Ian"
print(my_name) # print the value in my_name
print(my_name[0]) # print the value of the first character in the string
print(my_name[-1]) # print the value of the last character in the string

sentence = "This is a sentence"
print(sentence)
print(sentence[:4]) # this weill print the first four chacters (0-3)
print(sentence.split()) # this will print each word separtely using a delimiter ... the default deliniter is a space.

sentence_split = sentence.split() # assigns the output to a variable
print(type(sentence_split)) # type is a list
print(sentence_split[0]) # address a single item in the list

sentence_join =  ' '.join(sentence_split) #Joins the items in a list using the chosen delimiter
print(sentence_join)

#Useful for IP addresses
'========= IP Addresses ========='
IP = "192.168.1.10"
print(IP)
print(IP[:4]) # this weill print the first four chacters (0-3)
print(IP.split('.')) # this will print each word separtely using a delimiter ... the default deliniter is a space.

IP_split = IP.split('.') # assigns the output to a variable
print(IP_split[-1]) # get the last octet

# =====================================

# usign escape characters and single\double quotes
quote = 'he said, "give me all your money"'
print(quote)
quote = "he said, \"give me all your money\""
print(quote)

#=======================================
#strip characters
too_much_space = "                   hello"
print(too_much_space.strip())

# case sensitive comparisons
print("A" in "Apple") # return True
print("a" in "Apple") # return False

# commented out to prevent input
'''
letter = "A"
word = "Apple"
print(letter.lower() in word.lower())
user_input = input("yes or no :")
if user_input.lower().strip() == "yes":
    print("You Agree")
else:
    print("You Disagree")
'''

# formatting print statements
movie = "The Hangover"
print("My favourite movie is {}.".format(movie))
print("My favourite movie is %s." % movie)
print(f"My favourtie movie is {movie}.")