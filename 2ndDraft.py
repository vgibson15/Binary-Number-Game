import random
import math

WINNING = 5

 #welcome
def welcome():
    print("               Welcome to the binary Number Game")
    print("\n You will enter a number between 1 and 100 to play.")
    print("\n The computer will enter a number in decimal form.")
    print("   You will enter the same number in binary form.")
    print("\n The computer will enter a number in binary form.")
    print("  You will enter the same number in decimal form.")
    print("  If you are able to match the numbers correctly, you win.")
    print("\n binary numbers are in 0's or 1's and have a value of 2. ")
    print(" \n  Decimal numbers are in 1 - 100's. ")
    print('---------------------------------------------------------')
   
    #round
def round ():
    max_round = 0
    count = 0
     
    if max_round == 0:
        count = count + 1
        max_round = max_round + count
    for count in range(max_round):
        count = count + 1
        print("Round", max_round)
        print('---------------------------------------------------------')
    else:
        return max_round
              
#Computers Choice
def computer_choice():
    coin_flip = random.randint(0,3)
    
    #if binary number choosen
    if coin_flip != 3:
        binary = computer_choice = random.randint(1,100)
        computer_choice = int(computer_choice,2)
        #remove 0b in binary
        computer_choice = int(computer_choice,2)
        decimal_needed = input(print(" Enter", computer_choice, "in decimal form"))
    else:    
    #if decimal number choosen
        if coin_flip == 3: 
            decimal = computer_choice = random.randint(1,100)
            binary_needed = (input(print(" Enter", decimal, "in binary form")))
    
        
def winner():
user_choice = ?
computer_choice = ?

    #while round is less than 11 after each round say who wins
    while round != 11:
    
    #calculate if the user wins
    
    
    #say the user wins a round if it's decimal value = computers'binary value or binary value = computer'ss decimal
    round_winner = print ("You win this round!")
    # say the user loses a round if it's decimal value doesn't = the computers binary value or the decimal value doesn't = the computer's binary 
    
    #start the round process again
    
    
    
    #when the round is 11 display they won if they win more than 5 rounds then end the program
    
    
         

        return ("Congratulatons! You won the game!")
                
                
#User input
def user_choice():
    #binary numbers to find decimal number
    decimal_needed = 10
    binary_needed = bin(decimal_needed)
    binary_needed = int(binary_needed)
    
    #computer random number when decimal
    computer_choicea = random.randint(1,100)
    
    #computer random number when binary
    computer_choiceb = random.randint(1,100)
    computer_choiceb = bin(computer_choiceb)
    # take out ob needed computer_choiceb = 
  
    
    if decimal_needed == computer_choicea or decimal_needed == computer_choiceb:
        print("You won this round.")
        
    else:
      print("You lost this round.") 
      
      
    
def main():

        #welcome
        welcome()
        #Total of rounds
        round()
       #Get computer choice
        computer_choice()
       #Get user choice
        user_choice()
       #Winner
        winner()

#Call the function
main ()
