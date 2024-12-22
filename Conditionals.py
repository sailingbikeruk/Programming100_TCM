# Conditional Statements - if/else

def drink(money):
    if money >= 2:
        return "you've got yourself a drink"
    else:
        return "No drink for you"
    
print(drink(3))
print(drink(1))

def alchohol(age, money):
    if (age >= 21) and (money >=5):
        return "We're gettng a drink"
    elif (age >= 21) and (money < 5):
        return "Come back with more money"
    elif (age < 21) and (money >= 5 ):
        return "Nice try kid!"
    else:
        return "You're too young and too poor"
    
print(alchohol(21,5))
print(alchohol(21,4))
print(alchohol(18,5))
print(alchohol(18,1))