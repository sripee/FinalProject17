#defining powerup for later
powerup=[]

#importing sys to exit when they lose
import sys

#class for their name
class Player(object):
    def __init__(self, name):
        self.name = name

#what is the game
objective = "the objective of The Game of Sri is to run away from the monster that is chasing you. Along the way you will encounter obstacles and traps. You will aslo come across powerups and boosts you can use them to help you. When you get away from the monster you will win the game."
instructions = "Along the way you will encounter obstacles and scenarios. At these events you will be given 4 choices to choose from. These choices will dictate what you do. To pick a choice type its corresponding letter. If you make the right choice you will move on, if you do not you will lose the game."

#creating a name for the character
print("hello what is your name?")
player = Player(input("create a name for your character"))

#printing directions and objective
def game():
    print(player.name, objective, instructions)

#printing the game
game()

#start of the game
print("Begin your adventure")

#scenario one
A= "A)run into the bushes"
B= "B)let him eat you"
C= "C)jump to the ground and hope he can't see you"
D= "D)climb a tree next to you"
#inputting their choice
print("You are walking through the Amazon Rain Forest, all of a sudden Abominable Snowman jumps into your path, what do you do?")
print(A, B, C, D)
x = input("Do you... ")
if x == "A":
    print("You manage to evade the monster by running into the bushes, but you don't know for how long.")
if x == "B":
    print("You let him eat you and die")
if x == "C":
    print("He finds you and eats you, you die")
if x == "D":
    print("He knocks down the tree and eats you, you die")
if x == "B" or x == "C" or x == "D":
    print("you lose the game")
    sys.exit()

#scenario 2
A = "A)you try to eat the cobra"
B = "B)you kick the cobra in the face, and run away"
C = "C)you try to scare the cobra away"
D = "D)you bellyflop onto the snake"
#input their choice
print("You get up from the ground, to see a king cobra in front of you, what should you?")
print(A, B, C, D)
x = input("Do you...")
if x == "A":
    print("The snake bites you mouth, and kills you")
if x == "B":
    print("You knock the snake out and run away")
if x == "C":
    print("He lunges at you, bites you, and kills you")
if x == "D":
    print("The cobra bites in mid air, you die")
if x == "A" or x == "C" or x == "D":
    print("you lose the game")
    sys.exit()

#scenario 3
A = "A)go into the cave"
B = "B)go back into the forest"
C = "C)climb the mountain"
D = "D)curl up into a ball and cry"
#input their choice
print("You walk out of the forest, and see a snowy mountain,but there is also a cave under it, what do you do?")
print(A, B, C, D)
x = input("Do you...")
if x == "A":
    print("You walk into the cave, but inside the abominable snowman is waiting you, he rips you in half")
if x == "B":
    print("You walk into a bear trp, and die")
if x == "C":
    print("You climb the mountain, but see the Snowman behind you, though you are safe for now")
if x == "D":
    print("The snow man finds you, and eats you")
if x == "A" or x == "B" or x == "D":
    print("you lose the game")
    sys.exit()

#They get powerup for getting question right
print("You come across the skip question powerup, you can only use it once")
powerup.append("skip")
print(powerup)

#scenario 3
A = "A)jump off the mountain"
B = "B)climb back down the mounatin"
C = "C)eat your arm"
D = "D)take the trail"
#input their choice
print("There is a trail ontop of the mountain, and the Abmominable Snowman is catching up to you, what do you do?")
print(A, B, C, D)
x = input("Do you...")
if x == "A":
    print("You fall to your death and die")
if x == "B":
    print("The Snowman catches you and kills you")
if x == "C":
    print("You are dumb and die")
if x == "D":
    print("You take the trail, and go to the other side of the mountain")
if x == "A" or x == "B" or x == "C":
    print("you lose the game")
    sys.exit()

#scenario 4
A = "A)pick up an apple and eat it"
B = "B)chop down the tree to block the snowman's path"
C = "C)climb the tree"
D = "D)Throw the apple away"
#input their choice
print("You reach the other side of the mountain, and find an apple tree, what do you do?")
#if they want to use powerup
if "skip" in powerup:
    s = input("do you want to use your powerup? write yes or no")
    if s == "yes":
        x == "A"
        powerup.remove("skip")

    else:
        print(A, B, C, D)
        x = input("Do you...")
else:
    print(A, B, C, D)
    x = input("Do you...")
    if x == "A":
        print("You eat the apple, and fill your stomach, you made the right choice")
    if x == "B":
        print("The Snowman jumps over the tree and eats you")
    if x == "C":
        print("The snowman knocks down the tree and eats you")
    if x == "D":
        print("You are stupid, you throw away food, and die of starvation")
    if x == "D" or x == "B" or x == "C":
        print("you lose the game")
        sys.exit()

#scenario 5
A = "A)eat the eggs in the birds nest"
B = "B)walk past it"
C = "C)smash the eggs in the nest"
D = "D)fart on the eggs"
#input their choice
print("You are walking down the mountain when you see a bird's nest full of eggs, what do you do?")
print(A, B, C, D)
x = input("Do you...")
if x == "A":
    print("The motherbird comes back, and claws your eyes out, and you die")
if x == "B":
    print("You calmly walk by the nest avoiding trouble")
if x == "C":
    print("The motherbird kills you for killing her children")
if x == "D":
    print("You are stupid, why would you fart on the eggs")
if x == "A" or x == "D" or x == "C":
    print("you lose the game")
    sys.exit()

#scenario 6
A = "A)run away from the tiger"
B = "B)try to fight the tiger"
C = "C)act like a bigger tiger"
D = "D)jump up an down"
#input their choice
print("You come into a clearing where you see a tiger, what do you do?")
print(A, B, C, D)
x = input("Do you...")
if x == "A":
    print("The tiger eats you")
if x == "B":
    print("The tiger mauls you to death")
if x == "C":
    print("The tiger gets scared of you, and runs away")
if x == "D":
    print("You are stupid, why would you jump up and down")
if x == "A" or x == "D" or x == "B":
    print("you lose the game")
    sys.exit()

#scenario 7
A = "A)attack the lion"
B = "B)try to eat the lion"
C = "C)punch the lion in the face"
D = "D)fart in the lions face"
#input their choice
print("You escape the tiger, but you come across a lion what do you do?")
print(A, B, C, D)
x = input("Do you...")
if x == "A":
    print("the lion kills you")
if x == "B":
    print("The lion eats you instead")
if x == "C":
    print("The lion bites off your hand and kills you")
if x == "D":
    print("The lion suffocates on your fart and passes out")
if x == "A" or x == "B" or x == "C":
    print("you lose the game")
    sys.exit()

#scenario 8
A = "A)eat the berries"
B = "B)don't eat the berries"
C = "C)drink the berry juice"
D = "D)burn the berries"
#input their choice
print("You get hungry and see a bush of berries, what do you do?")
print(A, B, C, D)
x = input("Do you...")
if x == "A":
    print("You eat the berries, but they are poisonous you die")
if x == "B":
    print("You dodged a bullet, the berries were poisonous")
if x == "C":
    print("The berry juice is poisonous you die")
if x == "D":
    print("You burn the berries, but the smoke is poisoned you die")
if x == "A" or x == "D" or x == "C":
    print("you lose the game")
    sys.exit()

#scenario 9
A = "A)kick it away"
B = "B)pick it up"
C = "C)break it"
D = "D)cut off your leg"
#input their choice
print("You find a sword on the ground what do you do?")
print(A, B, C, D)
x = input("Do you...")
if x == "A":
    print("You are stupid, why would you kick it away")
if x == "B":
    print("You are smart, you pick up the sword in case you run into danger")
if x == "C":
    print("You are stupid, why would you break apotential weapon")
if x == "D":
    print("You are stupid, why would you cut off your leg")
if x == "A" or x == "D" or x == "C":
    print("you lose the game")
    sys.exit()

#scenario 7
A = "A)fight the snowman with your sword"
B = "B)run away from the snowman"
C = "C)beg the snowman for mercy"
D = "D)kill yourself with the sword"
#input their choice
print("You run into the clearing, and you see the Abominable Snowman on the other side, what do you do?")
print(A, B, C, D)
x = input("Do you...")
if x == "A":
    print("You fight the snowman with your sword and kill him, Congratulations, you have won the game!!")
    sys.exit()
if x == "B":
    print("The snowman catches you and eats")
if x == "C":
    print("He does not give you mercy, and kills you")
if x == "D":
    print("You are stupid why would you kill yourself")
if x == "D" or x == "B" or x == "C":
    print("you lose the game")
    sys.exit()




