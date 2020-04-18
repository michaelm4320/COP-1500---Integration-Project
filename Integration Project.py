#Michael Martinez
#Integration Project
#This is an RPG that takes the player on a short adventure.
#The player will make choices and fight monsters.

#I imported time to make the story flow nicely.
#Website used for help with time
#https://www.pythoncentral.io
import time

def main():
  # Players HP
  numHP = int(10)
  healthPoints = "*" * numHP
  missingHP = int(10 - numHP)
  missingPointsDash = "-" * missingHP

  wordA = "BEGIN"
  wordB = "DEMO"
  print("This is an RPG integration project."
        " Type BEGIN to begin the story or type DEMO for a small "
        "demonstration.")
  #This point increases as the player makes correct choices.
  point = int(0)
  #This variable increases if the player doesn't attack the dragon.
  babyDragon = int(0)


  # Player chooses to either start the story or demo.
  choice = input().upper()
  while True:
    if choice == wordA:
      break
    if choice == wordB:
      test()
      break
    print("Incorrect choice, please try again")
    choice = input().upper()

  print("You wake up in a middle of the beach and forget who you are. After much"
        " thought, you finally remember your name was...")
  playerName = input().upper()
  print("Your name was", playerName + ".")
  print("You checked your surrounding and noticed there's also a forest behind"
        " you. You're not sure whether you should stay and check the beach or"
        " head down to the forest.")
  print("[BEACH or FOREST]")

  pick1 = "BEACH"
  pick2 = "FOREST"
  choice1 = input().upper()

  while True:
    if choice1 == pick1:
      print("You decided to explore the beach first when suddenly, you found a"
            " crab!")
      print("[ATTACK or IGNORE]")
      pick3 = "ATTACK"
      pick4 = "IGNORE"
      choice2 = input().upper()
      while True:
        if choice2 == pick3:
          print("You attacked the crab, but took some damage in the process.")
          time.sleep(3)
          print("You took 3 points of damage!")
          numHP -=3
          currentHealth(numHP)
          print("Conveniently enough, you found a potion and some gold!")
          choice1 = "FOREST"
          point += 1
          break
        if choice2 == pick4:
          print("The crab didn't like that and attacked without hesitation!")
          time.sleep(3)
          print("You took 3 points of damage!")
          numHP -=3
          currentHealth(numHP)
          print("Frustrated, you decided that you had enough with the beach.")
          choice1 = "FOREST"
          break
        else:
          print("Incorrect choice, please try again")
          choice2 = input().upper()
    if choice1 == pick2:
      print("You decided to head into the forest.")
      break
    elif choice1 != pick1 or pick2:
      print("Incorrect choice, please try again")
      choice1 = input().upper()

  #The player is in the forest.
  time.sleep(3)
  print(" ")
  print("The area is filled with large trees and different creatures. As you"
        " continue your journey, you encountered a fairy.")
  time.sleep(3)
  print(" ")
  print("Fairy: There you are! I was looking all over for you! Do you remember"
        " why you're here?")
  print("[YES or NO]")

  pick5 = "YES"
  pick6 = "NO"
  choice3 = input().upper()
  while True:
    if choice3 == pick5:
      print("Fairy: Then let's not waste any time! Let's go!")
      break
    if choice3 == pick6:
      print("Your duty is to slay the dragon. And I'm supposed to guide you"
            " there. The dragon lies deep within the cave so there's no time to"
            " lose. Let's go!")
      break
    print("Incorrect choice, please try again")
    choice = input().upper()

  time.sleep(3)
  print(" ")
  print("You and the fairy make way deep into the forest. Up ahead you notice"
        " a baby dragon, snarling at your presence. You ask the fairy if this"
        " was the dragon you were supposed to slain.")
  time.sleep(3)
  print(" ")
  print("Fairy: This must be the dragon's offspring, it's dangerous so it"
        " must be destroyed")
  print("[ATTACK or APPROACH]")
  #Player makes their final decision.
  pick7 = "ATTACK"
  pick8 = "APPROACH"
  choice4 = input().upper()
  while True:
      if choice4 == pick7:
          print("You drew your sword and attacked the baby dragon. The"
                " creature however managed to scratch you before you dealt"
                " the final blow.")
          time.sleep(1)
          print("You took 5 points of damage!")
          numHP -= 5
          currentHealth(numHP)
          break
      if choice4 == pick8:
          print("You approached the baby dragon and the creature bit you!")
          time.sleep(1)
          print("You took 4 points of damage!")
          numHP -= 4
          currentHealth(numHP)
          print("It appears the dragon is lonely and afraid. The dragon is "
                "puzzled that you did not retaliate and stepped back to"
                " observe you carefully. \nYou smiled at the dragon and held"
                " at your hand, the creature approaches again and decided to"
                " follow you.")
          babyDragon += 1
          break
      print("Incorrect choice, please try again")
      choice = input().upper()
  if point == 1:
    print("You drank your potion to recover your wounds")
    time.sleep(4)
    print("You recovered 5 points of health!")
    numHP += 5
    currentHealth(numHP)
  if babyDragon == 1:
    print("The three of you traveled deeper into the forest and found"
            " the cave that you were searching for.")
    print(" ")
    time.sleep(4)
  else:
    print("You and the fairy continued to head deeper into the forest."
            " As you traveled, you stumble upon the cave that you"
            " were searching for.")
    print(" ")
    time.sleep(4)
  print("Fairy: The dragon is inside, be careful.")
  print(" ")
  time.sleep(4)
  #The player is in the cave.
  print("As you enter the cave, you hear a loud growl and the cave begins"
        " to shake. Facing before you is the dragon!")
  print(" ")
  time.sleep(4)
  print("Dragon: Human, you dare enter my home? I shall"
        " burn you into a pile of ash!")
  print(" ")
  time.sleep(4)
  print("The dragon burned you with it's powerful flames!")
  time.sleep(4)
  print("You took 7 points of damage!")
  numHP -= 7
  currentHealth(numHP)
  #Game over would trigger if player has 0 or less HP.
  if numHP <= 0:
      time.sleep(2)
      gameOver()
  time.sleep(1)
  #Ending of game
  print("Dragon: Impossible! You still stand?!")
  print(" ")
  time.sleep(3)
  print("The dragon lets out a mighty roar!")
  print(" ")
  time.sleep(3)
  print("Dragon: I'LL CRUSH YOU!")
  print(" ")
  time.sleep(3)
  print("You could barely stand. The dragon raises it's claw to lunge"
        " it's final attack.")
  print(" ")
  time.sleep(3)
  print("Before the dragon strikes, the baby dragon runs towards you to stop"
        " the attack. The dragon stopped.")
  print(" ")
  time.sleep(3)
  print("Dragon: My son! My dear son! I was looking all over for you!")
  print(" ")
  time.sleep(3)
  print("Baby Dragon: Stop father! Human led me here!")
  print(" ")
  time.sleep(3)
  print("The dragon faced towards you and bowed it's head.")
  print(" ")
  time.sleep(3)
  print("Dragon: Forgive me human. I was searching for my son and thought"
        " the humans killed him. We shall leave towards the mountains"
        " and not disturb the humans again.")
  print(" ")
  time.sleep(3)
  print("The dragon's flew away and returned home.")
  print(" ")
  time.sleep(3)
  print("Congratulations! Quest Completed!")

##########################################################################

#Function test is ran if player types DEMO.
def test():
  time.sleep(1)


  #Player name
  print("Enter your name.")
  playerName = input().upper()

  print("PLAYER NAME:", playerName)
  time.sleep(1)

  #Example of player making a choice. I want the player to make choices
  #Also be prompted to type again if entered incorrectly.
  #Website I used for help with if else statements 
  #https://www.w3schools.com/python/python_conditions.asp
  #Website used for learning to use while statements
  #https://stackoverflow.com
  word1 = "HELLO"
  word2 = "BYE"

  print("Type HELLO or BYE for different results.")
  choice1 = input().upper()

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
    choice1 = input().upper()
  time.sleep(3)

  #This is the players Health Points (HP). 
  #Player will have a max 10 HP and it decreases each time player takes damage.
  #The dashes shows HP is missing.
  print("Set a current value for your Health Points (HP). Value must be"
        " between 1 through 10. (Recommend between 1 through 9 to illustrate"
        " recovery.")
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
  time.sleep(3)

  #Player full recovery example no matter the current value.
  print("Here is an example full recovery (Your health must be less than 10 to"
        " notice the difference.)")
  print(" ")
  time.sleep(3)
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


##########################################################################


main()