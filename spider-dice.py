#Sean Carnie (CASEC171). Assignment submission for CSP1150D. 02/09/2020
#-----------------------------------------------------------------------------

#===============================================================================
#This program is used to emulate a game of spider dice for one or multiple
#players.


#The objective of spider dice is simple:



#The goal is to be the first to draw a spider. Each player rolls one dice at
#a time, if they roll a 6 they draw the body of the spider ( ). Once they
#have drawn the body – if they roll a 3 or 4 they can draw a leg, or a 1 
#to draw an eye. Their score is how many rolls are required to complete 
#the spider, however they must draw the body (6) before adding to the body.

#//\(oo)/\\




#The program is formatted for compact view,  contains many functions all built
#around allowing a user to input the number of players, thier names, as well as
#the number they roll for each repeated round, while progressing a spider until
#it is completed by adding all the individual body parts of the spider to it.
#===============================================================================















#===============================================================================  
#IMPORTANT IMPORTS AND GLOBAL VARIABLE.
#===============================================================================

#Both of these are used to generate the random value of the dice throw.
import random
from random import randint





#These two modules are imported for the sole purose of creating a delayed print
#in order to emulate the rolling of a dice to make the game more enjoyable.
import time
import sys


#A global variable created in order to validate the rule that a player cannot
#add to the body of the spider until a 6 is rolled, turning the value of this
#variable True.
unlocked_body = False
#===============================================================================



















#===============================================================================
#MAIN FUNCTION
#===============================================================================
def main():

#This is the main function.    

#----------------------------------------------------------------------------


    
    #A simple while loop created in order to repeat the game if the user desires.
    again = 'y' 
    while again == 'y':

        
#----------------------------------------------------------------------------


        #Printed explanation of game rules and welcome to the user.
        
        print("\nWelcome to spider dice!")
        print("\n\n\nThe rules of the game are simple:")
        input()
        print("\nThe goal of this game is to be the first person to complete \
                \nthe spider. Each player rolls one dice at a time, if they\
                \nroll a 6 they draw the body of the spider ( ). Once they have\
                \ndrawn the body – if they roll a 3 or 4 they can draw a leg, \
                \nor a 1 to draw an eye. \n\nThe first person to complete the \
                \nspider by adding a final part to it wins!, Note: The body of \
                \nthe spider (6) must be drawn before adding to the body.\
                \n\n⭜⭜⭝⮈⬩⬩⮊⭜⭝⭝")

        
#----------------------------------------------------------------------------
        #This is where the game begins. All main components of the program are
        #carried out in this function.
        
        player_name = main_player_input()
        
#----------------------------------------------------------------------------

        
        
        
        #Code to end loop that repeats the program.
        print('\n\n\n\n\nDo you want to play again?')
    
        again = input('\ny = yes, anything else = no: ')

        if again != 'y':
            print("\n\n\nThanks for playing!")

#===============================================================================        



























#===============================================================================
#FUNCTION TO CREATE SMALL DICE ROLLING ANIMATION
#===============================================================================

#This function serves the simple purpose of adding a delayed text output of a
#series of dice. It acts as a loading animation of sorts.
            
def animation():
    
    animation = "⚀ ⚁ ⚂ ⚃ ⚄ ⚅ "

    for i in range(35):
        time.sleep(0.03)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    return    
#===============================================================================


























            
#===============================================================================
#FUNCTION TO GET NUMBER OF PLAYERS, PLAYER NAMES, AND RETURN VALUES TO CREATE
# AND ADD TO SPIDER
#===============================================================================


#This function is the backbone of the program.

#The function obtains values from the user and goes on to create lists and
#dictionaries in order to constantly update them in a loop until the game
#ends.

def main_player_input():

    #Simple endless while loop to validate user input and ensure that a number
    #is entered here and the program does not produce an exception error.
    
    while True:

        try:

            #The number of players is input here by the user.    
            player = int(input('\n\nHow many people would like to play? '))
            
            step = 1
            player += 1
            
            #A two dimentional list in order to store both player value and
            #the progress of the spider.
            player_dict = {}
            
            #A list that the spider is input into constantly until it is complete.
            spider_drawing = [*[''],*[''],*[''],*[''],*[''],*[''],*[''],*[''],*\
                              [''],*['']]
            
            #This variable is used here to ensure that a player can only start
            #adding to the spider once a return roll value of 6 is obtained.
            
            global unlocked_body
            

            #The following variables are used to help aid the per round updating
            #of the spider for each player. It ensures that the code runs the way
            #it should as some of the parts of the spider are drawn using the same
            #roll value.
            
            spider_eye_count = 0
            spider_leg_count_1 = 0
            spider_leg_count_2 = 0
           
            
            
            
#----------------------------------------------------------------------------            
            
            #This loop is created in order to obtain and save the player names
            #inside of the player dictionary for as many players there.
            
            for pl in range(1, player, step):
                player_name = input(f'\nPlayer {str(pl)} enter your name here: ')


                #Each dictionary value is a list.
                player_dict[pl] = [player_name, '']  


                

            #This loop ensures that the game continues on until a player
            #completes the spider.
            while spider_drawing != [*['⭜'],*['⭜'],*['⭝'],*['⮈'],*['⬩'],\
                                     *['⬩'],*['⮊'],*['⭜'],*['⭝'],*['⭝']]:

                
                #This for loop ensures that each player of the game is able
                #to produce a value when rolling dice and use that return
                #value to draw the spider.
                
                for x in player_dict:
                    
                    


                    
                    #The main_game_output function is called here to obtain
                    #roll values.

                    #The player name is stored at the list index 0. The the
                    #main_game_output has it's required parameter variable.
                    
                    score = main_game_output(player_dict[x][0])


#----------------------------------------------------------------------------                     
#PART OF THE FUNCTION WHERE SPIDER IS UPDATED PER ROUND PER PLAYER.
#----------------------------------------------------------------------------
                    
#Most of the code here is reused from the main_game_output function

#----------------------------------------------------------------------------                    
#Body                   
#----------------------------------------------------------------------------
                        
                    #The program starts adding to body only after a 6 is returned from
                    #the main_game_output() function.
                    
                            
                    if unlocked_body == False:
                        
                        if score == 6:

                            #This is where the values for the indexes of the list
                            #spider_drawing are updated in order to keep progressing
                            #the spider.
                            
                            spider_drawing[3] = '⮈'
                            spider_drawing[6] = '⮊'
                            
                            #List is displayed as a string here in order to make
                            #it easier for the viewer to see.
                            spider_drawing_str = ''.join(spider_drawing)

                            #The progress of the spider is stored at index 1
                            #of the dictionary.
                            player_dict[x][1] = spider_drawing_str 
                            

                            
                            #The values of the global value is changed and so
                            #the players can start adding to the body of the
                            #spider in order to continue the game
                            
                            unlocked_body = True


#----------------------------------------------------------------------------
                            
#All of the following if statements only occur if a 6 is obtained by the player first. 
                                      
#----------------------------------------------------------------------------



#----------------------------------------------------------------------------                            
#Eyes
#---------------------------------------------------------------------------- 

#The following section obtains the value 1 and adds the eye of the spider.
                            
                    if unlocked_body == True:

                    

                        
                                
                        
                        if (score == 1):

                            #The value of the indexes are changed using this statment in
                            #order to keep progressing the spider by adding it's parts
                            #to it.
                            
                            spider_drawing[4]= '⬩'
                            spider_drawing_str = ''.join(spider_drawing)
                            
                            #The count is used to avoid logical errors as both eyes are produced
                            #using the number 1 but have different indexes on the spider_drawing
                            #list.
                            
                            spider_eye_count += 1

                            #The current value and progress of the spider is changed here.
                            player_dict[x][1] = spider_drawing_str 
                            
                            
                         
                            
                    if unlocked_body == True:
                        
                        #A comparison of if statements in order to avoid logical errors
                        #and ensure both eyes are added to to spider.
                        
                        if (score == 1) and (spider_eye_count == 2):

                            
                            spider_drawing[5]= '⬩'
                            spider_drawing_str = ''.join(spider_drawing)
                            player_dict[x][1] = spider_drawing_str           
    

 
#----------------------------------------------------------------------------                             
#Legs                    
#----------------------------------------------------------------------------



#The following section obtains the value 3 as well as 4, and adds the legs
#of the spider.
                            
#Most of the code from the section above is reused here.
                            
                    if unlocked_body == True:

                    

                        
                                
                        
                        if (score == 3):

                            
                            spider_drawing[2] = '⭝'
                            spider_drawing_str = ''.join(spider_drawing)
                            spider_leg_count_1 += 1
                            player_dict[x][1] = spider_drawing_str 
                            
                            
                         
                            
                    if unlocked_body == True:
                        
                        
                        
                        if (score == 3) and (spider_leg_count_1 == 2):
                            
                            spider_drawing[8] = '⭝'
                            spider_drawing_str = ''.join(spider_drawing)
                            player_dict[x][1] = spider_drawing_str   
    
                    if unlocked_body == True:
                        
                    
                        
                        if (score == 3) and (spider_leg_count_1 == 3):
                            
                            spider_drawing[9] = '⭝'
                            spider_drawing_str = ''.join(spider_drawing)
                            player_dict[x][1] = spider_drawing_str 

                            
    
                if unlocked_body == True:


                    
                    
                    if (score == 4):

                            



                        
                            spider_drawing[7] = '⭜'
                            spider_drawing_str = ''.join(spider_drawing)
                            spider_leg_count_2 += 1
                            player_dict[x][1] = spider_drawing_str 
                            
                            


                    if unlocked_body == True:
                        
                        
                        if (score == 4) and (spider_leg_count_2 == 2):

                            
                            spider_drawing[0] = '⭜'
                            spider_drawing_str = ''.join(spider_drawing)
                            player_dict[x][1] = spider_drawing_str 



        
                    if unlocked_body == True: 
                        if (score == 4) and (spider_leg_count_2 == 3):
                            

                            
                            spider_drawing[1] = '⭜'
                            spider_drawing_str = ''.join(spider_drawing)
                            player_dict[x][1] = spider_drawing_str                           

#----------------------------------------------------------------------------                    
          
                #This line of code shows the current progress of he spider
                #for each round the players play.
                            
                print ("The spider so far:", (spider_drawing))
                
            #This statement only prints once the game is over and the
            #spider is complete. The last person to add to the spider
            #(the first person to complete it)has their name displayed
            #as the winner. The game ends here.
                
            print(f'\n\n{player_name} wins the game!')
            

            
        #This is where the validation loop ends.
            break
        
        except ValueError:
            print('\nSorry, but you need to enter a number here.')
            
   
    #Player name is returned here in order to be used by the
    #main_game_output() function.
    return player_name
#===============================================================================
































#===============================================================================
#FUCTION THAT GENERATES THE VALUE FOR DICE ROLL, AND DISPLAYS MOST OF THE
#RESPONSES PER ROUND IN ORDER TO GUIDE THE PLAYER.
#===============================================================================

#This function serves the purpose of generating the values needed in order to
#create the spider.

#The function also serves to make the whole game more user friendly by providing
#constant feedback on game related information such as what player rolls, as well
# as what a roll means, throughout the rounds of the game.



#The function requires the player_name variable found in the
#main__player_input() function in order to carry out it's task.

def main_game_output(player_name):

    

    #This variable is created for the sole purpose of aiding to display
    #which part of the spider the player unlocks each turn.
    
    spider_part = ''

    #The same global function is used here in order to provide the right
    #responses to the user based on the numbers they roll and their current
    #situation in the game.
    
    global unlocked_body
    

    
        
        
#----------------------------------------------------------------------------

    #Simple validation while loop to ensure that the player enters 'r' in order
    #to the roll the dice, and avoid exception errors.
    
    while True:

        #The player name from main_player_input() is used here for displaying
        #purposes.
        
        start_rolling = input(f"\n\n\n{player_name} it's your turn:\n\
        \nPress 'r' to roll dice. ")
        if start_rolling == 'r' or start_rolling == 'R':
            roll = randint(1, 6)









#----------------------------------------------------------------------------
#The next few sections are a sequence of if statments that help the player
#understand which body parts of the spider they've unlocked, or not unlocked.
#----------------------------------------------------------------------------


            
            if roll == 6:
                spider_part = str(r' body ⮈ ⮊ this round!')
            if roll == 3:
                spider_part = str(r' leg ⭝ this round!')
            if roll == 4:
                spider_part = str(r' leg ⭜ this round!')
            if roll == 1:
                spider_part = str(r' eye ⬩ this round!')
            
            #This statement is simply used to make the displayed output more tidy.
                
            print('\n')
            
            #This is where the animation plays
            
            animation()

            



#----------------------------------------------------------------------------
#Body of the spider.          
#----------------------------------------------------------------------------
            
            #Just like in the main_player_input() function, the certain if statements
            #in this section are only carried out if the player has obtained a return
            #roll value of 6 and obtained the body of the spider, turning the
            #unlocked_body global variable True.
            
            if unlocked_body == False:
                
                if roll == 6:

                    print(f'\n\n{player_name} rolls a {roll}')
                    
                    #Added input() functions as pauses for viewer readability
                    
                    input()
                    
                    print(f"\n\n{player_name} congradulations! You've unlocked the spider's" + spider_part)
                    
                    #The rest of the if statments in this function can now be
                    #displayed as the player is able to start adding to the spider.
                    
                    unlocked_body == True



                    
                    
            #If statement used to ensure that the player cannot obtain the body
            #of the spider more than once.

            if unlocked_body == True:
                
                if roll == 6:

                    print(f'\n\n{player_name} rolls a {roll}')
                    input()
                    print(f"\n\n{player_name} you already have the spider's body. Try again!")
                    unlocked_body == True       



#----------------------------------------------------------------------------
#The rest of the spider.        
#----------------------------------------------------------------------------

            #If statement to ensure that players cannot add to the body of the spider unless
            #they roll 6 and acquire the spider body.
                    
            if unlocked_body == False:
                
                if roll == 3 or roll == 4 or roll == 1:
                        
                        
                        
                    print(f'\n\n{player_name} rolls a {roll}')
                    input()
                    print(f"\n\n{player_name}, you need to acquire the body before adding other parts to it. Keep trying!")
                        
                if roll == 2 or roll == 5:
                    print(f'\n\n{player_name} rolls a {roll}')
                    input()
                    print(f"\n\n{player_name} doesn't unlock anything this round. Better luck next time!")


                    


            #If statements telling a player their roll, as well as which part of the spider they
            #did / did not unlock.
                    
            if unlocked_body == True:            
                if roll == 3 or roll == 4 or roll == 1:
                        
                        
                        
                    print(f'\n\n{player_name} rolls a {roll}')
                    input()
                    print(f"\n\n{player_name} unlocks the spider's" \
                          + spider_part)
                        
                if roll == 2 or roll == 5:
                    print(f'\n\n{player_name} rolls a {roll}')
                    input()
                    print(f"\n\n{player_name} doesn't unlock anything this round. Better luck next time!")

                    
#----------------------------------------------------------------------------


                    
            #The value a player rolls is returned here.
                    
            return roll

        #This is where the validation loop ends.
        
            break
        else:
            
            print(f"\nYou need to press 'r' {player_name}!.")
            input()
        
    return
#===============================================================================
























#===============================================================================
#The main function is called and so the game begins.
main()
#===============================================================================
