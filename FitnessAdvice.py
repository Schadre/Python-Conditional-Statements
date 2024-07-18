# Ask the user how many minutes they exercise daily and provide healthy advice

daily_minutes = int(input("How many minutes do you exercise daily? Numerical values only "))

if daily_minutes < 30:
    print("I believe it would be benefical if you could increase your daily minutes to 30 minutes of exercise!")
elif daily_minutes == 30:
    print("You have a good daily exercise with 30 minutes as your baseline.")
elif daily_minutes > 30:
    print("You are doing pretty awesome with your daily exercise by going over 30 minutes!")
else:
    print("Make sure you are using numerical values only!")
