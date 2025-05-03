print("!!!WELCOME TO TREASURE ISLAND!!!")

path = input('you\'re at the cross road. Where do you want to go? Type "left" or "right"\n').lower()

if path == "left":
    waitorswim = input('you\'ve come to lake. There is an island in the middle of the lake. Type "wait" to wait for _Boat_. Type "swim" to swim across.\n').lower() 
    if waitorswim == "wait":
        color = input("You arrived at island unharmed. There is a house with 3 doors. One 'Red', one 'Yellow' and one 'Blue'. Which color do you choose?\n").lower()
        if color == "yellow":
            print("You found the Treasure. You WON!!!")
        elif color == "red":
            print("You enter a room of Lava. Game Over.")
        elif color == "blue":
            print("You enter a room of Beasts. Game Over.")
        else:
            print("You choose a door that dosen't exist. Game Over.")
    else:
        print("There are Crocodiles in lake. Game Over")
else:
    print("You are on Wrong Path. Game Over")