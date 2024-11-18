#importing dictionary from CharToMorse.py
from CharToMorse import MorseCoverter as MC
#importing Logo from logo.py
from logo import Logo

on = True
while on:
    #printing out Logo
    print(Logo)
    #Storing user input string in user_input
    user_input = input("enter your string you want to covert here: \n")
    #an empty list to store the coverted morse characters
    morse_code_list = []
    # a for loop to go through every character in user_input String
    for char in user_input:
        #coverting string char  to Morse char
        morse_Char = MC[char.upper()]
        #storing morse char in morse code
        morse_code_list.append(morse_Char)
    #coverting morse_code_list into a string
    morse_code = "".join(morse_code_list)
    #printing out MorseCode
    print(morse_code)
    #ask user do they want to continue
    user_input = (input("do you want to continue press 'Y' for yes and 'N' for no ")).upper()
    #if they press y then while loop continues start and if they press n then loop will break and program will exit
    if user_input == "N":
        on = False
