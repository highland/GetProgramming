#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
rock, paper, scissors game from Chapter 35
Created on Sun May 24 12:01:19 2020

@author: mark
"""

import random
import sys

options = "rock paper scissors"

choice = input(f"Choose {options}: ")
if choice not in options:
    print('Not one of the options. Exiting')
    sys.exit()

computers_choice = random.choice(options.split())

print(f"Computer chose {computers_choice}.")
if choice == computers_choice:
    print("Tie")
elif ((choice == 'rock' and computers_choice == 'scissors') or
      (choice == 'paper' and computers_choice == 'rock') or
      (choice == 'scissors' and computers_choice == 'paper')):
    print("You win!")
else:
    print("You lose")