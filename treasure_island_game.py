print('''
                                                   .       .
                                                    \     /
                                                 ._  '   '  _.
                                                   '  o@o  '
                                                     o@@@o
                                                 .-'  o@o  '-.
                                                     .   .
                                                    /     \
                         
                             'Xx  xX*,
                          ,*xXXx_xXx
                            _xXXXXXxx*,
                          ,*XXx@x@Xx
                            X @|@@ `x
                            '  ||    '
                               ||
                               ||
                               ||
                               ||
                            /ssssssss.
                      /sssssssSSSSssssssssss.
        /\         /sssssSSSSSSSSSSSSSSSssssssssssss.              Dani
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~''')
print("Welcome to the island of the lost treasure.")
print("Your mission is to find the treasure or escape.")
choice1 = input('You\'re at a seashore, where do you want to go in the jungle or wait? Type "jungle" or "wait".\n').lower()   
if choice1 == "jungle":
  print("You went in to explore the jungle. You encounter a wild beast.")
  choice2 = input("Do you want to fight or run? Type 'fight' or 'run'.\n").lower()
  if choice2 == "fight":
    print("You fought the beast and won. You are now damage.")
    choice3 = input("Do you want to continue or rest? Type 'continue' or 'rest'. \n").lower()
    if choice3 == "continue":
      print("You continued and found wild berries. You ate and recovered your health.")
      choice4 = input("You found a cave. Do you want to go in or wait? Type 'go in' or 'wait'.\n").lower()
      if choice4 == "go in":
        print("You went in and heard noises. You hide behind a rock and see barbarian.")
        choice5 = input("Do you want to fight, run or wait? Type 'fight' or 'run' or 'wait'.\n").lower()
        if choice5 == "fight": 
          print("You fought barbarian and found the treasure. You win!")
        elif choice5 == "run":
          print("You ran away and chased by barbarian and died. You lose.")
        elif choice5 == "wait":
          print("Barbarian found you and killed you. You lose.")
      else:
        print("You waited and attacked by pack of wolves. You lose.")
    else:
      print("You rested and bit by snake you died. You lose.")
  else:
    print("You ran away and chased by beast and died. You lose.")
else:
  print("You waited and saw boat coming toward you.")
  choice6 = input("Do you want to hide or ask for help? Type 'hide' or 'help'.\n")
  if choice6 == "hide":
    print("You hide in the bushes and aw it's a pirate boat. You waited for them to go int the jungle. You get in the boat and escaped. You win!")
  elif choice6 == "help":
    print("You asked for help and they are pirates. They killed you. You lose.")
