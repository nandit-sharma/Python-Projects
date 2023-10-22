import time

def type(text):
    for l in text:
        print(l, end ='', flush=True)
        time.sleep(0.1)
def type1(text):
    for l in text:
        print(l, end ='', flush=True)
        time.sleep(0.01)

type1(">>>>>>>>>>>>>>>------------------------------------------WELCOME-------------------------------------------<<<<<<<<<<<<<<<\n>>>>>>>>>>>>>>>-----------------------------------------FIND THE TREASURE-------------------------------------<<<<<<<<<<<<<<<\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")


type("This is a treasure hunting game...\nYou have to enter your choice of answer as per the situation is.\nPress Enter to start the game_")
input()

type("\nSo, You are on the shore, the treasure is in an island located across the sea, you have a boat and a car. What would you pick for starting your journey?  \n")
c1 = input()
if c1.upper() == 'CAR':
    type("Great !! how could you drive car over the sea maybe you are too intelligent for the game.\nThankyou, the game is over ")
    input("\nPress Enter to exit...........")
    exit()
elif c1.upper() == 'BOAT':
    pass
else:
    print("Invalid choice")
    input("\nPress Enter to exit...........")
    exit()

time.sleep(1)

type("\nOkay, So now you've reached the island.\nYou are very hungry and there are some apples and oleanders grown on the trees. What would you decide to eat if one of them is poisonous!\n")
c2 = input()
if c2.upper() == 'OLEANDERS':
    type("Oleanders are poisonous, you died.\nGame over")
    input("\nPress Enter to exit...........")
    exit()
elif c2.upper() == 'APPLES':
    pass
else:
    print("Invalid choice")
    input("\nPress Enter to exit...........")
    exit()

time.sleep(1)

type("\nShehh... you survived !\nNow you've reached the house where the treasure is located. There are three doors infront of you: Red, Blue and Green! which one would you like to choose?\n")
c3 = input()
if c3.upper() == 'RED':
    type("There was exclusive fire, you died instantly.\nGame over")
    input("Press Enter to exit.")
    exit()
elif c3.upper() == 'BLUE':
    type("There was poisonous gas in the room, you died instantly.\nGame over")
    input("\nPress Enter to exit...........")
    exit()
elif c3.upper() == 'GREEN':
    pass
else:
    print("Invalid choice")
    input("\nPress Enter to exit...........")
    exit()
time.sleep(1)


type("\nThat was the correct one!\nThe treasure is in front of you BUT there's a caretaker lion about to attack you. You have a knife, a gun and a poisoned meat.\nYou have few seconds, what would you choose to defeat the lion...\n")
c4 = input()
if c4.upper() == 'KNIFE':
    type("Congratulations, you were killed by the lion. Choosing knife to kill a lion wasn't the best choice.\nGame over")
    input("\nPress Enter to exit...........")
    exit()
elif c4.upper() == 'POISONED MEAT':
    type("Congratulations, you were killed by the lion. Lions are very clever and focused, they can't be fooled easily.\nGame over")
    input("\nPress Enter to exit...........")
    exit()
elif c4.upper() == 'GUN':
    type1(".....................................................CONGRATULATIONS.....................................................\n")
    type("\nYou found the Treasure finally after a lot of struggle.Hope you'd use it wisely. GOOD LUCK!\n")
    input("\nPress Enter to exit...........")
else:
    print("Invalid choice")
    input("\nPress Enter to exit...........")
    exit()

