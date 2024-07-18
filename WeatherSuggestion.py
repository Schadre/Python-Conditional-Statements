# Based on the temperature entered by the user, suggest an outfit to wear. Be creative
the_current_temp = int(input("What is the tempurate outside? "))

if the_current_temp > 80:
    print("It's too hot for anything but a bathing suit my friend")
elif the_current_temp <= 80 and the_current_temp >= 70:
    print("This is nice weather to enjoy linens in without sweating or feeling attacked by global warming")
elif the_current_temp <= 60:
    print("It's time for the winter coat!")


# Based on the weather entered by the user, sugget an outfit to wear. Be Creative
the_current_weather = str(input("What is the current weather? ").lower())

if the_current_weather == "sunny":
    print("Time to put on a beach outfit and enjoy the beach baby!")
elif the_current_weather == "rainy":
    print("Let's grab an unbrella, those yellow boots, the yellow coat to match and aviod IT the clown while we play with paper boats!")
elif the_current_weather == "cloudy":
    print("It's cloudy with a chance of meatballs, put on your favorite spaghetti outfit and let's go eat!")
else:
    print("The weather options are Sunny, Rainy, and Cloudy. Anything more than this requires too much thinking and I am just a computer, okay.")