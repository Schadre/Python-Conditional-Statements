# Recommend a type of coffee based on user preferences about sweetness and milk

coffee_sweet = str(input("Do you like your coffee sweet? Yes or No ").lower())
milk = str(input("Do you like milk with your coffee ? Yes or No ").lower())

if coffee_sweet == "yes" and milk == "yes":
    print("Here is your very sweet and smoothly milked coffee! Enjoy :)")
elif coffee_sweet == "no" and milk == "yes":
    print("Here is your unsweet coffee with milk! Enjoy :)")
elif coffee_sweet == "yes" and milk == "no":
    print("Here is your very sweet coffee with no milk! Enjoy :)")
elif coffee_sweet == "no" and milk == "no":
    print("Here is your black cofee! Enjoy :) ")
else:
    print("Yes or No answers only, please.")

