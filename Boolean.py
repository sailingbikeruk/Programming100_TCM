
# Relational and Boolean Operators

#Boolean Expression (True or false)

bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1,bool2,bool3,bool4)
print(type(bool1))

# Relational and Boolean Operators

greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_then_equal_to = 7 <= 7
equals = 7 == 7
not_equals = 7 != 8

test_and = (7 > 5) and (5 < 7) # True - both need to be true to return true
test_and2 = (7 > 5) and (5 > 7) # False = both need to be true

test_or = (7 > 5) or (5 < 7) # True - just one has to be true
test_or2 = ( 7 > 5) or (5 > 7) # True - only one OR the other statement needs to be true
test_not = not True # False