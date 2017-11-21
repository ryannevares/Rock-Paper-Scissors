"""
Author: Ryan Nevares
Date: November 20 2017
Version: 1.2
Title: Rock, Paper, Scissors game.

This game will use use the random module to select rock, paper, or scissors.  It will then prompt the user for input, then finally make a comparrison to determine who won.

Please report any bugs to ryannevares@gmail.com
"""
from random import randint
from textwrap import fill
from time import sleep
from sys import stdout

# declare the options:  rock paper and scissors
OPTIONS = ['R','P','S'] # indices 0,1,2
# message for the loser and winner
LOSER = " YOU LOSE!!! \n YOU LOSE!!! \n YOU LOSE!!! \n YOU LOSE!!!"
WINNER = " YOU WIN!!! \n YOU WIN!!! \n YOU WIN!!! \n YOU WIN!!!"

def print_slow(string):
    for letter in fill(string):
        stdout.write(letter)
        stdout.flush()
        sleep(.03)
    print ""

# Print initial message to the user
# print our initial message to the user
print ""
print ""
print_slow ("Welcome to Rock, Paper, Scissors!")
sleep (1)
print_slow ("I promise I won't cheat...")
print "\n\n"
sleep(1)

# Define a function to decide on a winner
def decide_winner(user_choice, comp_choice):
  print_slow ("You have chosen  %s" % user_choice)
  sleep(.5)
  print_slow ("Computer selecting ...")
  sleep(1)
  print_slow ("The computer has chosen  %s" % comp_choice)
  sleep(1.2)
  print ""
  user_choice_index = OPTIONS.index(user_choice)
  comp_choice_index = OPTIONS.index(comp_choice)
  if user_choice_index == comp_choice_index:
    print "Tie!  Go again \n \n "
    sleep(1)
    play_RPS()
  # Only need to program the winning scenarios, the rest just fall into the else
  elif user_choice_index == 0 and comp_choice_index == 2:
    print WINNER
    sleep(1)
  elif user_choice_index ==1 and comp_choice_index == 0:
    print WINNER
    sleep(1)
  elif user_choice_index == 2 and comp_choice_index == 1:
    print WINNER
    sleep(1)
  elif user_choice_index > 2:
    print "Invalid user index"
    sleep(.5)
    return
  else:
    print LOSER
    sleep(1)
  again()

# Define a function to ask the user if they want to play again
def again():
    print ""
    playagain = raw_input("Play again?? (y/n): ")
    playagain = playagain.lower()
    if playagain == "y":
        print_slow ("Alright!  Let's go!")
        print "\n\n\n"
        sleep(1.5)
        play_RPS()
    elif playagain == "n":
        print ""
        print_slow ("Sorry to see you go, exiting now ....")
        print "\n\n\n"
        exit()
    else:
        print_slow ("Please choose y or n: ")
        sleep (1)
        again()

# Define a function to actually play the game
def play_RPS():
  print_slow ("R for Rock")
  sleep (.4)
  print_slow ("P for Paper")
  sleep(.4)
  print_slow ("S for Scissors")
  sleep(.4)
  user_choice = raw_input('Choose R, P, or S:  ')
  user_choice = user_choice.upper()
  if user_choice != 'R' and user_choice != 'P' and user_choice != 'S':
      print_slow ("You need to choose Rock, Paper, or Scissors")
      print "\n\n"
      play_RPS()
  sleep(1)
  # Now the computer makes a choice
  comp_choice = randint (0,len(OPTIONS)-1)
  comp_choice = OPTIONS[comp_choice]
  # Call the decide winner function
  decide_winner(user_choice,comp_choice)

# Call the main function "play_RPS"
play_RPS()

"""
FUTURE SUGGESTIONS:  Make textwrap work with any size window.
"""
