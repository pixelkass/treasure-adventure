def treasure_adventure():
          treasure_found = False
          door_art = """
       BLUE                           RED                          YELLOW
      ______                         ______                         ______
   ,-' ;  ! `-.                   ,-' ;  ! `-.                   ,-' ;  ! `-.
  / :  !  :  . \\                 / :  !  :  . \\                 / :  !  :  . \\
 |_ ;   __:  ;  |               |_ ;   __:  ;  |               |_ ;   __:  ;  |
 )| .  :)(.  !  |               )| .  :)(.  !  |               )| .  :)(.  !  |
 |"    (##)  _  |               |"    (##)  _  |               |"    (##)  _  |
 |  :  ;`'  (_) (               |  :  ;`'  (_) (               |  :  ;`'  (_) (
 |  :  :  .     |               |  :  :  .     |               |  :  :  .     |
 )_ !  ,  ;  ;  |               )_ !  ,  ;  ;  |               )_ !  ,  ;  ;  |
 || .  .  :  :  |               || .  .  :  :  |               || .  .  :  :  |
 |" .  |  :  .  |               |" .  |  :  .  |               |" .  |  :  .  |
 |____;----.____|               |____;----.____|               |____;----.____|
"""
          while treasure_found == False:
                    print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
                    print("Welcome to Treasure Adventure.")
                    print("Your mission is to find the treasure.") 
                    
                    l_or_r = input("You are presented with two paths...\nDo you want to follow the path to the right? Or the path on the left?\nChoose carefully... (type 'left' or 'right')\n")
                    if l_or_r == "left":
                              swim_or_wait = input("After followingi the path for some time, you arrive at a river.\nDo you swim accross? Or do you wait? (type 'wait' or 'swim')\n")
                              if swim_or_wait == "wait":
                                        print(door_art)
                                        door = input("Three doors arrise from the ground and appear before you.\nOne blue, one red, and one yellow?\nWhich door do you enter? (type 'blue', 'yellow' or 'red')\n")
                                        if door == "blue":
                                                  print("The moment you open the door, you are blinded by light.\nIt was over before you knew it...\nBetter luck next time!")
                                                  try_again = input("Try again? Y or N\n").lower()
                                                  if try_again == "y":
                                                      treasure_adventure()
                                                  else:
                                                      print("Thanks for playing!")
                                        elif door == "red":
                                                  print("You open the red door.\nA dragon's head makes its way out of the door and devours you in an instant.\nBetter luck next time!")
                                                  try_again = input("Try again? Y or N\n").lower()
                                                  if try_again == "y":
                                                      treasure_adventure()
                                                  else:
                                                      print("Thanks for playing!")
                                        elif door == "yellow":
                                                  print("As you open the door, a yellow glow greets your face.\nA room! A room full to the brim with treasure!!!\nAll yours for the taking!")
                                                  play_again = input("Would you like to play again? Y or N\n").lower()
                                                  if play_again == "y":
                                                      treasure_found = False
                                                      treasure_adventure()
                                                  elif play_again != "y":
                                                      treasure_found = True
                                                      print("Thanks for playing!")
                                                  
                                        elif door != "blue" and door != "red" and door != "yellow":
                                                  print("You did not open any of the doors properly.\nDoing this activated a trap that sent spikes out from the floor under your feet.\nBetter luck next time! ")
                                                  try_again = input("Try again? Y or N\n").lower()
                                                  if try_again == "y":
                                                      treasure_adventure()
                                                  else:
                                                      print("Thanks for playing!")
                    
                              else:
                                        print("You start swimming accross the river. Suddenly, you notice a huge fish behind you chasing you!\nYou try with all your might to swim faster and escape, but it is to no avail...\nThe fish just got a bit fatter. Better luck next time!")
                                        try_again = input("Try again? Y or N\n").lower()
                                        if try_again == "y":
                                            treasure_adventure()
                                        else:
                                            print("Thanks for playing!")                   
                    else:
                              print("You start walking down the path.\nSuddenly, everything goes dark....\nYou fell down a hole that was hidden under that path\nRest in peices.")
                    
          
          
treasure_adventure()



