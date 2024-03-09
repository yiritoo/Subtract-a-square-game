# File: CS112_A1_T2_3_20230471.py
# Purpose: The 'Subtract a square" game made in python.
#          Two players pick from perfect square numbers and whoever takes the last coin wins.
# Author: Yassen Elsayed Kamal
# ID: 20230471

import random
import math

def main():

    #Randomly choosing the number of coins used for the game
    coins = random.randint(1, 1000)

    def is_perfect_square(number):
    #For checking if the input is a perfect square
        square_root = math.isqrt(number)
        return square_root * square_root == number
    
    #Displaying a welcome message and the number of coins
    print('** Welcome to the subtract a square game! The player who takes the last coin wins **')
    print('Number of coins =', coins)

    #Gameplay
    while coins > 0:
        move = int(input('Player 1: Take a perfect square amount of coins '))
        #Checking if the number of coins taken is valid

        #Checking if the inputted number from the player is a perfect square 
        while not is_perfect_square(move):
            move = int(input('Player 1: Take a perfect square amount of coins '))
        
        #Checking if there are enough coins
        while move > coins:
            move = int(input('Player 1: Select a smaller viable number '))
        coins -= move
        print('Number of coins is', coins)

        #Game ending condition
        if coins == 0:
            print('Victory for Player 1!')
            break

        move = int(input('Player 2: Take a perfect square amount of coins '))
        #Checking if the number of coins taken is valid

        #Checking if the inputted number from the player is a perfect square 
        while not is_perfect_square(move):
            move = int(input('Player 2: Take a perfect square amount of coins '))
        
        #Checking if there are enough coins
        while move > coins:
            move = int(input('Player 2: Select a smaller valid number '))
        coins -= move
        print('Number of coins is', coins)

        #Game ending condition
        if coins == 0:
            print('Victory for Player 2!')
            break

if __name__ == "__main__":
    main()


    