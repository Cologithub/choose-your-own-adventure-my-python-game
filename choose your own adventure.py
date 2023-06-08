#start date:05/06/23
#end date:06/06/23

#Choose your own adventure game. The user's choices will ulitmatley determine the progress of the game.
#the results of the user's choice will be different throughout the game, depending on what they select to move forward.

from tracemalloc import start

username=input("What is your name? ")
print ("Hello " + username + (" ! "))

print("Welome to the TREASURE HUNT!! CHOOSE YOUR OWN ADVENTURE!!")
playing=input("Would you like to play:)? Answer with Yes or No:  ")

if playing !="Yes":
    print("Game has ended.")
    quit()

print("GAME HAS BEGUN!")

print("HI THERE "+ username + " !" )
print("Welcome to The Royal Treasure House! ")
print ("Somewhere in this house, there are exciting hidden treasres to be found!")  
print ("Which ones you find however, will all determine on the choices you make.")

#treasure 1- block of gold
#treasure 2- $20,000 in an envelope
#treasure 3- a rolex watch

backyard=("B")
living_room=("LR")
master_bedroom=("MB")

print("The game has officialy begun. There are three areas in the house to look for the treasure. Backyard, Living room and the Master bedroom. ")
locations=input("Starting locations to look: Type B to choose backyard, LR to choose living room and type MB to choose the master bedroom: ")

#user selects their location of choice
#D1-decision

if locations==backyard:
    print("You have selected the backyard.")
    D1=int(input("Type 1 to continue: "))


if locations==living_room:
    print("You have selected the living room.")
    D1=int(input("Type 2 to continue: "))


if locations==master_bedroom:
    print("You have selected the master bedroom.")
    D1=int(input("Type 3 to continue: "))


#Stage 2 of search

#tip-state the variables before you start the if staements.

#D1 and S1 are constants for the first satge. (The only thing that changes would be the user's input.)

print("You've reached stage 2 of the hunt!")


if D1==1:
    print("You're now in the backyard.")
    print ("You've looked around the area, and there are 3 main areas to keep searching. The shed, the mango tree and the tall grass.")
    print ("Which area would you like to choose?")
    S1=input("Type S to select the shed, MT to select the mango tree or TG to select the tall grass: ")
    

if D1==2:
    print("You're now in the living room.")
    print ("You've looked around the area, and there are 3 main areas to keep searching. The kitchen, the sofa, or the dining table.")
    print ("Which area would you like to choose?")
    S1=input("Type K to select the kitchen, TS to select the sofa, or TDT to select the dining table: ")
    

if D1==3:
    print("You're now in the master bedroom.")
    print ("You've looked around the area, and there are 3 main areas to keep searching. The night stand, the dresser or inside the closet.")
    print ("Which area would you like to choose?")
    S1=input("Type NS to select the night stand, D to select the dresser, or C to select the closet: ")
    
 #stating variables so the computer knows what the user is referring to.   
#backyard options
the_shed=("S")
the_mango_tree=("MT")
tall_grass=("TG")

#living room options
kitchen=("K")
the_sofa=("TS")
the_dining_table=("TDT")

#master bedroom options
night_stand=("NS")
dresser=("D")
closet=("C")

#Then i start the IF statements:
#Now, we are continuing by the user's selections, hence S1/selection 1 would be our variable.


#backyard selection 1

if S1==("S"):
    print("HOORAY:) YOU'RE NOW IN THE SHED! KEEP GOING! ")
    print("You now have three places you can look. The toolbox, inside the bucket, or behind the old tires.")
    S1=input("Type TB to select the toolbox, ITB for inside the bucket, or BTT for behind the old tires. ")


if S1==("MT"):
    print("HOORAY:) YOUVE NOW CLIMBED THE MANGO TREE! KEEP GOING! ")
    print("Upon climbing the tree, you noticed 2 strange yellow objects through the thickness of the leaves.")
    print("could just be a ripe mango, you thought. OR it could be treasure....")
    print("You can either reach to the left, or to the right to grab the object. You can only grab one. So choose wisely.")
    S1=input("Type L to reach to your left, or R to reach to your right: ")


if S1==("TG"):
    print("HOORAY:) YOU'RE NOW IN THE TALL GRASS! KEEP GOING! ")
    print("In the grass, your eyes spot three things.")
    print("A weird patch of no grass, some tree branches, and an old soda can. ")
    print("Which place would you like to investigate?")
    S1=input("Type NG to select no grass, TB to select tree branches, or SD to select the old soda can: ")


#living room selection 1

if S1==("K"):
    print("HOORAY:) YOU'RE NOW IN THE KITCHEN!")
    print("You now have three places you can look. Inside the oven, or in the cutlery drawer.")
    S1=input("Type O to select the oven, or CD to select the cutlerty drawer: ")


if S1==("TS"):
    print("HOORAY:) YOU'RE NOW AT THE SOFA! ")
    print("You can check under the sofa or between the cushions:)")
    S1=input("Type UTS to select under the sofa, or BTC to select between the cushions: ")


if S1==("TDT"):
    print("HOORAY:) YOU'RE NOW AT THE DINING TABLE!")
    print("Theres a flower pot, a pan cover.")
    print("Which one could the treasure hold? Up to you ;)")

    S1=input("Type FP to select the flower pot, or PC to select the pan cover: ")


#master bedroom selection 1

if S1==("NS"):
    print("HOORAY:) YOU'RE NOW AT THE NIGHT STAND!")
    print("You can check by the alarm or by the lamp.")
    S1=input("Type A to select by the alarm, or BTL to select by the lamp: ")


if S1==("D"):
    print("HOORAY:) YOU'RE NOW AT THE DRESSER! ")
    print("Maybe the treasure is inside the 1st drawer... or maybe the 2nd :)")
    S1=input("Type TFD to select the first drawer, or TSD to select the second drawer: ")


if S1==("C"):
    print("HOORAY:) YOU'RE NOW IN THE CLOSET!")
    print("You can check inside shirt pockets, or inside shoe boxes to find the treasure...But choose wisely:)")
    S1=input("Type ITP to select inside shirt pockets, or ISB to select inside shoe boxes: ")

#finding the treasure (if the user is lucky lol)
#Again, listing new variables


#backyard final selection- the shed
tool_box=("TB")
inside_the_bucket=("ITB")
behind_the_old_tires=("BTT")

#backyard final selection- the mango tree
left=("L")
right=("R")

#backyard final selection- tall grass
no_grass=("NG")
tree_braches=("TB")
soda_can=("SD")


#living room final selection- kitchen
oven=("O")
cutlery_drawer=("CD")

#living room final selection- the sofa
under_the_sofa=("UTS")
between_the_cushions=("BTC")

#living room final selection- the dining table
flower_pot=("FP")
pan_cover=("PC")


#master bedroom final selection-nightstand
alarm=("A")
by_the_lamp=("BTL")

#master bedroom final selection-dresser
the_first_drawer=("TFD")
the_second_drawer=("TSD")

#master bedroom final selection-closet
inside_shirt_pockets=("ITP")
inside_shoe_boxes=("ISB")

#Final if satements:

#backyard

while S1==("TB"):
    print("CONGRATS! YOUVE FOUND A BLOCK OF GOLD:) GLAD YOU FOUND THE TREASURE!")
    break

#living room

while S1==("PC"):
    print("YAYY YOU FOUND A ROLEX WATCH! ENJOYY:)")
    break


#master bedroom

while S1==("ITP"):
    print("YOU FOUND AN ENVELOPE WITH $20,000!!! ENJOY:)")
    break

#Program was completed on 06/06/23 at 9:29pm.
#This is my first time doing a python project with zero youtube tutorials on this topic.
#The only research i did was on string concatenation and user input, which didnt take long.
#Im proud to say this mini game was my imagination:) thank the Lord:)

