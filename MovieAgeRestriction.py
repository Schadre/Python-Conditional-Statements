# To ensure viewers have an age appropriate experience, movies come with specific ratings. 
# Given a movie's rating (G, PG, PG-13, R) and the age of the person, inform the user if they
# can watch the movie based on their age

viewrs_age = int(input("How old are you?(Numerial data only): "))

if viewrs_age < 7:
    print("You are only allowed to watch movies rated G")
if viewrs_age < 13 and viewrs_age >= 7:
    print("You are only allowed to watch movies rated G and PG")
elif viewrs_age == 13:
    print("You are only allowed to watch movies rated G, PG, and PG-13")
elif viewrs_age > 13 and viewrs_age < 17:
    print("You are only allowed to watch movies rated G, PG, and PG-13, no rated R for you without an adult!")
elif viewrs_age >= 17:
    print("You are allowed to watch all genres which includes G, PG, PG-13, and R")
