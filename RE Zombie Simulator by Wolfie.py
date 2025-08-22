#This is a RE Zombie Encounter Simulator created with the help of AI as this is my first project
#The player plays as Leon in this text-based zombie fighting gameplayer = {"health": 100, "ammo": 10} #Dictionary for Leon's stats
player = {"health": 100, "ammo": 10}  # Leon's stats
zombie = {"health": 50, "damage": 20}  # Zombie stats

while player["health"] > 0 and zombie["health"] > 0:
    action = input("Choose: shoot, dodge, heal: ")  
    if action == "shoot":                          
        if player["ammo"] > 0:                    
            zombie["health"] -= 30
            player["ammo"] -= 1
            print("You shot the zombie! Zombie health:", zombie["health"])
        else:                                     
            print("Out of ammo!")
    elif action == "dodge":                       
        print("You dodged! No damage this turn.")
    elif action == "heal":                        
        print("Healed! Your health:", player["health"])
        player["health"] += 20
    else:                                         
        print("Invalid action!")
    if zombie["health"] > 0:                      
        player["health"] -= zombie["damage"]
        print("Zombie attacks! Your health:", player["health"])

if player["health"] > 0:
    print("Zombie defeated! You win.")
else:
    print("Game over.")
