#Michael Martinez
#Integration Project
#This is an RPG that takes the player on a short adventure. The player will make choices and fight monsters.

#I imported time to make the story flow nicely.
#Website used for help with time - https://www.pythoncentral.io/pythons-time-sleep-pause-wait-sleep-stop-your-code/
import time

#Function test is run if player types DEMO.
def test():
  time.sleep(1)


  #Player name
  print("Enter your name.")
  playerName = input()

  print("PLAYER NAME:", playerName)
  time.sleep(1)

  #Example of player making a choice. I want the player to make choices and also be prompted to type again if entered incorrectly.
  #Website I used for help with if else statements - https://www.w3schools.com/python/python_conditions.asp
  #Website used for learning to use while statements - https://stackoverflow.com/questions/12828771/how-to-go-back-to-first-if-statement-if-no-choices-are-valid
  word1 = "HELLO"
  word2 = "BYE"

  print("Type HELLO or BYE for different results.")
  choice1 = input()

  while True:
    if choice1 == word1:
      time.sleep(1)
      print("Hello", playerName + "! Nice to meet you!")
      break
    if choice1 == word2:
      time.sleep(1)
      print("Have a great day", playerName +"!")
      break
    print("Sorry", playerName + ". Can you say that again?")
    choice1 = input()
  time.sleep(1)

  #This is the players Health Points (HP). The player will have a maximum of 10 HP and it decreases each time player takes damage.
  #The dashes shows HP is missing.
  print("Set a current value for your Health Points (HP). Value must be between 1 through 10. (Recommend between 1 through 9 to illustrate recovery.")
  while True:
    numInput = int(input())
    if numInput <= 10 and numInput > 0:
      numHP = numInput
      healthPoints = "*" * numHP
      missingHP = int(10 - numHP)
      missingPointsDash = "-" * missingHP
      print("HP:", numHP, "/ 10 [" + healthPoints + missingPointsDash + "]")
      break
    print("Incorrect value. Please try again.")

  print(" ")
  time.sleep(1)

  #Player full recovery example no matter the current value.
  print("Here is an example full recovery (Your health must be less than 10 to notice the difference.)")
  print(" ")
  time.sleep(1)
  numHP = numHP + missingHP
  healthPoints = "*" * numHP
  missingHP = int(10 - numHP)
  missingPointsDash = "-" * missingHP
  print("HP:", numHP, "/ 10 [" + healthPoints + missingPointsDash + "]")
  print(" ")
  
  print("That's all for the demo. Try the story next!")
  quit()
  
###########################################################################
#Minor defined functions.
def currentHealth(hp):
  time.sleep(1)
  numHP = int()
  numHP = numHP + hp
  healthPoints = "*" * numHP
  missingHP = int(10 - numHP)
  missingPointsDash = "-" * missingHP
  print("HP:", numHP, "/ 10 [" + healthPoints + missingPointsDash + "]")
  print(" ")
  return hp

def gameOver():
  print("GAME OVER!")
  quit()

###########################################################################

#Players HP outside of defined functions.
numHP = int(10)
healthPoints = "*" * numHP
missingHP = int(10 - numHP)
missingPointsDash = "-" * missingHP
  
wordA = "BEGIN"
wordB = "DEMO"
print("This is an RPG integration project. Make sure to leave CAPS LOCK on. Type BEGIN to begin the story or type DEMO for a small demonstration.")

#Player chooses to either start the story or demo.
choice = input()
while True:
  if choice == wordA:
    break
  if choice == wordB:
    test()
    break
  print("Incorrect choice, please try again")
  choice = input()
  
#Story begins here.
print("You wake up in a middle of the beach and forget who you are. After much though, you finally remember your name was...")
playerName = input()
print("Your name was", playerName + ".")
print("You checked your surrounding and noticed there's also a forest behind you. You're not sure whether you should stay and check the beach or head down to the forest.")
print("[BEACH or FOREST]")

pick1 = "BEACH"
pick2 = "FOREST"
choice1 = input()

while True:
  if choice1 == pick1:
    print("You decided to explore the beach first when suddenly, you found a crab!")
    print("[ATTACK or IGNORE]")   
    pick3 = "ATTACK"
    pick4 = "IGNORE"
    choice2 = input()
    while True:
      if choice2 == pick3:
        print("You attacked the crab, but took some damage in the process.")
        time.sleep(1)
        print("You took 3 points of damage!")
        numHP -=3
        currentHealth(numHP)
        print("Conveniently enough, you found a potion and some gold!")
        choice1 = "FOREST"
        break
      if choice2 == pick4:
        print("The crab didn't like that and attacked without hesitation!")
        time.sleep(1)
        print("You took 3 points of damage!")
        numHP -=3
        currentHealth(numHP)
        print("Frustrated, you decided that you had enough with the beach.")
        choice1 = "FOREST"
        break
      else:
        print("Incorrect choice, please try again")
        choice2 = input()
  if choice1 == pick2:
    print("You decided to head into the forest.")
    break
  elif choice1 != pick1 or pick2:
    print("Incorrect choice, please try again")
    choice1 = input()

#Forest
time.sleep(1)
print(" ")
print("The area is filled with large trees and different creatures. As you continue your journey, you encountered a fairy.")
time.sleep(1)
print(" ")
print("Fairy: There you are! I was looking all over for you! Do you remember why you're here?")
print("[YES or NO]")

pick5 = "YES"
pick6 = "NO"
choice3 = input()
while True:
  if choice3 == pick5:
    print("Fairy: Then let's not waste any time! Let's go!")
    break
  if choice3 == pick6:
    print("Your duty is to slay the dragon. And I'm supposed to guide you there. The dragon lies deep within the cave so there's no time to lose. Let's go!")
    break
  print("Incorrect choice, please try again")
  choice = input()

time.sleep(1)
print(" ")
print("To be continued...")

