# Lists - square brackets [] - each thing is an item
# Lists are mutable i.e. they can be changed, items can be added deleted or modified

movies = ["Avengers", "Avengers Assemble", "Iron Man", "Spiderman" ]
print(movies[1]) # returns the second item in the list - index in python starts at zero
print(movies[0]) # returns the first item in a list

print(movies[1:3]) # this doesnt return numbner three it effectvely says start at and do while < 3
print(movies[1:4]) # this returns three movies
print(movies[1:]) # return everything from position one onwards
print(movies[:1]) # return everything before position 1
print(movies[-1]) # returns last item

for movie in movies: # this will print each item in the list on a new line
    print(movie)

print(len(movies)) # returns the count of items in the list

#add a movie
movies.append("Ant Man")
print(movies)

# add a movie in a particular spot
movies.insert(2,"Red Witch")
print(movies)

# remove last item
movies.pop() # removes last item 
print(movies)

#remove a specific item
movies.pop(0) #rmeove the item in lcoation 0
print(movies)

# Combine Lists
my_movies = movies
her_movies = ["Transformers", "Hellraiser","Exorcist"]
our_movies = my_movies + her_movies
print(our_movies)

#Liss in Lists
grades = [["Bob",82],["Alice",90],["Jeff",73]]
bobs_grades = grades[0][1]
print(bobs_grades)

# modify lists in list
grades[0][1] = 83
print(f"Bobs new grade is {grades[0][1]}")