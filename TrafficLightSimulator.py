# Write a program that prompts the user to input the color of a traffic light(red, yellow, green)
# and outputs the action a driver should take. 
traffic_light = str(input("Please enter a traffic light color: Red, Yellow, or Green: ").lower())

if traffic_light == "red":
    print("Please stop the vehicle, immediately or I am calling the cops!!!")
elif traffic_light == "yellow":
    print("Slow down there buddy!!!")
elif traffic_light == "green":
    print("Go, Go, Gooooooo! Beep Beep")
else:
    print("Please choose: Red, Yellow, or Green only.")