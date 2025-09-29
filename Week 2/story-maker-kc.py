# let the user know what's going on
print ("Welcome to MadLibs!")
print ("Answer the questions below to play.")
print ("-----------------------------------")

# variables containing all of your story info
pet_type = input("Type of pet: ")
pet_name = input("Name of pet: ")
restaurant1 = input("What is your favorite restaurant?: ")
music_artist = input("Name your favorite music artist: ")
silly_dance = input("Name a silly dance move: ")
verb1=input("Enter a verb: ")

# this is the story. it is made up of strings and variables.
# the \ at the end of each line let's the computer know our string is a long one
# (a whole paragraph!) and we want to continue more code on the next line. 
# play close attention to the syntax!

story = "After you leave, your " + pet_type + " named " + pet_name + " starts their secret routine. " \
+ pet_name + " discovers your leftovers from " + restaurant1 + " and devours every last bite. " \
"Feeling satisfied, " + pet_name + " turns on " + music_artist + " and starts doing the " + silly_dance + " around the living room. " \
"Suddenly, " + pet_name + " hears your keys jingling outside and quickly turns off the music and " + verb1 + " back to their bed. " \
"When you walk in, " + pet_name + " pretends to be asleep. " \
"You're completely oblivious and give " + pet_name + " a loving pet before you make your way to the fridge. " \
"You open the fridge and wonder out loud, 'Where did my " + restaurant1 + " leftovers go?' "


# finally we print the story
print(story)
