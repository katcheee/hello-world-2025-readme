# SOMETHING'S NOT RIGHT AT HOME
# Mystery game with multiple endings

import random   # for dice rolling
import sys      # for system functions

# player object - stores all game data
player = { 
    "name": "p1", 
    "score": 0,
    "clues": [],    # list to store clues found
    "location": "entrance"
}

def rollDice(minNum, maxNum, difficulty):
    # any time a chance of something might happen, let's roll a die
    result = random.randint(minNum, maxNum)
    print ("You roll a: " + str(result) + " out of " + str(maxNum))
    
    if (result >= difficulty):
        return True
    else:
        return False

def gameOver(ending):
    # different endings based on clues found
    print("-------------------------------")
    
    if (ending == "pet"):
        print("ARTHUR CAUSED THE MESS!")
        print("Your dog got loose and had an adventure.")
        print("He's hiding in the basement, covered in dust and potato chips.")
        player["score"] += 100
        
    elif (ending == "dream"):
        print("IT WAS ALL A DREAM!")
        print("You check the time - impossible to be home yet!")
        print("You wake up on the bus, still heading home.")
        player["score"] += 50
        
    elif (ending == "spooky"):
        print("SOMETHING SUPERNATURAL!")
        print("No logical explanation fits the evidence.")
        print("Strange forces are at work in your house...")
        player["score"] += 75
    
    print("Final score: " + str(player["score"]))
    return

def livingRoom():
    # describ what players sees
    print("You enter the living room.")
    print("Couch cushions are on the floor.")
    print("Picture frame is knocked over.")
    print("TV is on showing static.")
    
    # add clue if not already found
    if ("couch_mess" not in player["clues"]):
        player["clues"].append("couch_mess")
        player["score"] += 10
    
    # show options and get input
    print("options: [ kitchen , upstairs , call arthur , check time ]")
    pcmd = input(">")
    
    # navigate based on choice
    if (pcmd == "kitchen"):
        kitchen()
    elif (pcmd == "upstairs"):
        upstairs()
    elif (pcmd == "call arthur"):
        callArthur()
    elif (pcmd == "check time"):
        checkTime()
    else:
        print("I don't understand that")
        livingRoom()

def kitchen():
    print("You walk into the kitchen.")
    print("Cabinet doors are open.")
    print("Dog food bowl is empty.")
    print("Trash can is knocked over.")
    print("Back door is slightly open.")
    
    # add clues automatically
    if ("dog_evidence" not in player["clues"]):
        player["clues"].append("dog_evidence")
        player["score"] += 20
    
    print("options: [ living room , upstairs , call arthur , basement ]")
    pcmd = input(">")
    
    if (pcmd == "living room"):
        livingRoom()
    elif (pcmd == "upstairs"):
        upstairs()
    elif (pcmd == "call arthur"):
        callArthur()
    elif (pcmd == "basement"):
        basement()
    else:
        print("I don't understand that")
        kitchen()

def upstairs():
    print("You go upstairs to your bedroom.")
    print("Clothes are scattered on the floor.")
    print("You hear scratching sounds from below.")
    
    if ("scratching" not in player["clues"]):
        player["clues"].append("scratching")
        player["score"] += 10
    
    # random cold feeling for spooky path
    coldChance = random.randint(1,10)
    if (coldChance > 7):
        print("The room feels strangely cold...")
        player["clues"].append("cold")
    
    print("options: [ living room , kitchen , call arthur , basement ]")
    pcmd = input(">")
    
    if (pcmd == "living room"):
        livingRoom()
    elif (pcmd == "kitchen"):
        kitchen()
    elif (pcmd == "call arthur"):
        callArthur()
    elif (pcmd == "basement"):
        basement()
    else:
        print("I don't understand that")
        upstairs()

def callArthur():
    # FIRST DICE ROLL - call arthur
    print("You call out loudly: ARTHUR! Here boy!")
    print("Let's roll a dice to see if Arthur responds!")
    input("press enter to roll >")
    
    difficulty = 12
    success = rollDice(1, 20, difficulty)
    
    if (success):
        print("You hear barking from the basement!")
        player["clues"].append("arthur_responds")
        player["score"] += 25
    else:
        print("Silence. No response at all.")
        player["clues"].append("no_response")
    
    input("press enter >")
    
    print("options: [ living room , kitchen , upstairs , basement ]")
    pcmd = input(">")
    
    if (pcmd == "living room"):
        livingRoom()
    elif (pcmd == "kitchen"):
        kitchen()
    elif (pcmd == "upstairs"):
        upstairs()
    elif (pcmd == "basement"):
        basement()
    else:
        callArthur()

def basement():
    print("You open the basement door and go downstairs.")
    
    if ("arthur_responds" in player["clues"]):
        print("You see Arthur trapped behind fallen boxes!")
        print("He's covered in dust and looks guilty.")
        
        print("Do you want to search around first?")
        pcmd = input("search or free arthur >")
        
        if (pcmd == "search"):
            # SECOND DICE ROLL 
            print("Let's roll to see what you find!")
            input("press enter to roll >")
            
            difficulty = 1
            success = rollDice(1, 20, difficulty)
            
            if (success):
                print("You find a torn bag of potato chips—looks like Arthur was sneaking snacks in the basement again.")
                player["clues"].append("chips")
                player["score"] += 20
        
        print("You free Arthur. He jumps on you happily!")
        player["clues"].append("found_arthur")
        decideEnding()
        
    else:
        print("The basement is empty. No Arthur anywhere.")
        print("Just then, your neighbor knocks on the front door.")
        print("'He wandered into my yard this morning. Just thought I'd bring him back!'")
        print("You're stunned. Arthur's been at their place all day?")
        print("But then... what made this mess?")
        player["clues"].append("arthur_at_neighbors")
        decideEnding()

def checkTime():
    print("You check your phone: 5:42 PM")
    print("Wait... you left work at 5:30 PM")
    print("Your house is 20 minutes away...")
    
    # time math calculations
    timeElapsed = 42 - 30  # 12 minutes
    travelTime = 20        # 20 minutes needed
    
    print("Time since leaving work: " + str(timeElapsed) + " minutes")
    print("Travel time needed: " + str(travelTime) + " minutes")
    
    # comparison operator
    if (timeElapsed < travelTime):
        print("That's impossible!")
        gameOver("dream")
    else:
        print("The timing works out.")
        livingRoom()

def decideEnding():
    # count clues to decide ending
    dogClues = 0
    spookyClues = 0
    
    # check for dog evidence
    if ("dog_evidence" in player["clues"]):
        dogClues += 1
    if ("arthur_responds" in player["clues"]):
        dogClues += 1
    if ("found_arthur" in player["clues"]):
        dogClues += 1
    if ("chips" in player["clues"]):
        dogClues += 1
    
    # check for spooky evidence
    if ("no_response" in player["clues"]):
        spookyClues += 1
    if ("cold" in player["clues"]):
        spookyClues += 1
    if ("arthur_at_neighbors" in player["clues"]):
        spookyClues += 2  # strong spooky evidence
    
    # logical operators to decide
    if (dogClues >= 3 and "found_arthur" in player["clues"]):
        gameOver("pet")
    elif (spookyClues >= 2 or "arthur_at_neighbors" in player["clues"]):
        gameOver("spooky")
    else:
        # default based on most evidence
        if (dogClues > spookyClues):
            gameOver("pet")
        else:
            gameOver("spooky")

def startGame():
    print("SOMETHING'S NOT RIGHT AT HOME")
    print("You arrive home from work.")
    print("The front door is unlocked... you always lock it.")
    print("You step inside. Something feels wrong.")
    
    print("What's your name?")
    player["name"] = input(">")
    
    print("Where do you want to go first, " + player["name"] + "?")
    print("options: [ living room , kitchen , upstairs ]")
    
    pcmd = input(">")
    
    if (pcmd == "living room"):
        livingRoom()
    elif (pcmd == "kitchen"):
        kitchen()
    elif (pcmd == "upstairs"):
        upstairs()
    else:
        print("Let's start in the living room.")
        livingRoom()

# main! most programs start with this.
def main():
    startGame()

main()