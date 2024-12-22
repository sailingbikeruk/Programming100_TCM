# Loops

# For Loops - start to finish of an iterate

vegetables = ["carrots", "cauliflower", "cabbage"]
for veggies in vegetables:
    print(veggies)

for i in range(5):
    print(i)

word = "python"
for letter in word:
    print(letter)

# Whie Loop - execute as long as True

i=1
while i < 10:
    print(i)
    i += 1

password = ""
while password != "Spaghetti":
    password = input("Enter Password")

print("access Granted")