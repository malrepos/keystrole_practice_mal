#!/usr/bin/env python
# coding: utf-8

# game to help develop speed when typing for python.coding

import random

#List of common keyboard strokes
list_ =  [ "*","(",")","_","+",
         "{","}","|","[","]","\\",
         ":","""""",";","'",
         "<",">","?",",",".","?" ]

# Initialise Input
new_input = ""

print("Develop your strenght for touch common sytax characters")
print ("<---------------------------------------------------->\n")
print("GO!\n\n")

# Game will continue untile the user types "quit" or "x"

while new_input != "quit":
    print("_______\n")
    print(random.choice(list_))
    print("_______\n")
    new_input = input("")


# In[ ]:




