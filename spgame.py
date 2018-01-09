#explaining objective and game directions
objective = "the objective of this game is to run away from the monster that is chasing you. Along the way you will encounter obstacles and traps. You will aslo come across powerups and boosts you can use them to help you. When you get away from the monster you will win the game."
directions = "Along the way you will encounter obstacles and scenarios. At these events you will be given 4 choices to choose from. These choices will dictate what you do. To pick a choice type its corresponding letter. If you make the right choice you will move on, if you do not you will lose the game."

#creating a name for the character
print("hello what is your name?")
name = input("create a name for you character")

#printing directions and objective
objective = "the objective of this game is to run away from the monster that is chasing you. Along the way you will encounter obstacles and traps. You will aslo come across powerups and boosts you can use them to help you. When you get away from the monster you will win the game."
print(name, objective)
print(directions)

#start of the game
print("Begin your adventure")

#scenario one
A= "A) run into the bushes"
B= "B) let him eat you"
C= "C) jump to the ground and hope he can't see you"
D= "D) climb a tree next to you#inputting their choice
print("You are walking through the Amazon Rain Forest, all of a sudden Abominable Snowman jumps into your path, what do you do?")
x = input("Do you...", A, B, C, D)
if x = A:
    print("You manage to evade the monster by running into the bushes, but you don't know for how long.")
if x = B:
    print("You let him eat you, you die and lose the game")


