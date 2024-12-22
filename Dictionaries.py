# Dictionaries - a list of key value pairs - use {}

drinks = {"White Russian":8, "Old Fashioned":12, "Lemon Drop":5} #create a dictionary
print(drinks)

employees = {"Finance": ["Bob","Linda", "Tina"],"IT": ["Gene","Louise","Teddy"],"HR":["Jimmy jr", "Mort"]}
print(employees)
employees['legal'] = ["Mr Frond"] # add a key\value pair to an existing dictionary
print(employees)
employees.update({"sales":["Andy","Ollie"]}) #add a key \value pair to a dictionary a different way
print(employees)

drinks["White Russian"] = 9 # update and exiting value usign the key
print(drinks)

print(drinks.get("White Russian"))

