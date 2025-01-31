# card images found here: https://github.com/marcllopis/JungleSpeed-match
import pygame
import sys
import random
import os
import time

# initialize pygame
pygame.init()

# screen dimensions
WIDTH, HEIGHT = 960, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jungle Speed")

# color variables
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
LIGHTRED = (255, 182, 193)
GREEN = (0, 255, 0)
GREY = (200, 200, 200)

# fonts
title_font = pygame.font.Font(None, 80)
button_font = pygame.font.Font(None, 50)
small_font = pygame.font.Font(None, 27)
countdown_font = pygame.font.SysFont(None, 380)
# change to timesnewroman which is nicer after NEA

'''# back card
back_Card = deck[0]
# player deck dictionaries
player1 = {
    # ideas for later
    deck[0]: "1";

}'''



# screens section

# loading images into pygame
# buttons
settingsIcon_image = pygame.transform.scale(pygame.image.load(r"img\icons\settings.png"), (50,50))
backIcon_image = pygame.transform.scale(pygame.image.load(r"img\icons\back.png"), (50,50))
crownIcon_image = pygame.transform.scale(pygame.image.load(r"img\icons\crown.png"), (100,100))
infoIcon_image = pygame.transform.scale(pygame.image.load(r"img\icons\info.png"), (49,49))
# match screen components
totem_Image = pygame.transform.scale(pygame.image.load(r"img\totem.png"), (204, 204))
logo_Image = pygame.transform.scale(pygame.image.load(r"img\logo.png"), (170,170))
hand_Image = pygame.transform.scale(pygame.image.load(r"img\hand.png"), (310,310))
defaultcard_Size = (210, 316)
discardPile_image = pygame.transform.scale(pygame.image.load(r"img\discard_Pile.png"), (defaultcard_Size))

# variables loading all cards into pygame
cards_Folder = r"img\cards"
deck = []

# variable used for handling cards
count = 0


''' CODE FOR IMPORTING ACTUAL CARDS INTO PROGRAM - FOR LATER USE'''
# for loop which loads the cards folder into the main program
for card in os.listdir(cards_Folder):
    # checks if file type is jpg
    if card.endswith(".jpg"):
        # holds the path of img within index 'card'
        card_path = os.path.join(cards_Folder, card)
        # uses individual card path to load into pygame
        card_img = pygame.transform.scale(pygame.image.load(card_path), (85, 120)) 
        # now the card has been loaded, it is appended to a deck list for later use
        deck.append(card_img)
back_Card1 = deck[0]
back_Card2 = deck[0]


# function for drawing text visible to the user
def draw_text(text, font, color, surface, xaxis, yaxis):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (xaxis, yaxis)
    surface.blit(textobj, textrect)

# draw the authentication screen
def draw_authentication_screen(screen, title_font, button_font, WIDTH, HEIGHT, LIGHTRED, RED, WHITE, BLACK):
    
    # draw header
    draw_text("Authentication", title_font, BLACK, screen, WIDTH // 2, HEIGHT // 8)
    
    # draws shapes of buttons
    signup_button = pygame.Rect(WIDTH // 4, HEIGHT // 2 - 100, WIDTH // 2, 50) 
    signin_button = pygame.Rect(WIDTH // 4, HEIGHT // 2, WIDTH // 2, 50) 
    skip_button = pygame.Rect(WIDTH // 4, HEIGHT // 2 + 100, WIDTH // 2, 50) 

    # draws the button and text
    pygame.draw.rect(screen, RED, signup_button) 
    pygame.draw.rect(screen, RED, signin_button) 
    pygame.draw.rect(screen, RED, skip_button) 
    draw_text("Sign up", button_font, WHITE, screen, WIDTH // 2, HEIGHT // 2 - 75) 
    draw_text("Sign in", button_font, WHITE, screen, WIDTH // 2, HEIGHT // 2 + 25) 
    draw_text("Skip", button_font, WHITE, screen, WIDTH // 2, HEIGHT // 2 + 125)
    
    return signin_button, signup_button, skip_button

# variable that keeps track of user's total number of wins
winScore = 50

# draw the main menu screen
def draw_mainMenu_screen(screen, title_font, button_font, WIDTH, HEIGHT, LIGHTRED, RED, WHITE):

    # draw header
    draw_text("Main Menu", title_font, pygame.Color('black'), screen, WIDTH // 2, HEIGHT // 8)

    # draw buttons and their contents to main menu screen
    settings_button = screen.blit(settingsIcon_image, (WIDTH * 0.93, HEIGHT * 0.013888889))
    back_button = screen.blit(backIcon_image, (10,10)) 
    info_button = screen.blit(infoIcon_image, (WIDTH * 0.87, HEIGHT * 0.013888889))
    play_button = pygame.Rect(WIDTH * 0.298, HEIGHT * 0.55555556, WIDTH // 2.5, HEIGHT * 0.10396667)
    pygame.draw.rect(screen, RED, play_button)
    draw_text("Play", pygame.font.Font(None, 55), WHITE, screen, WIDTH * 0.493, HEIGHT * 0.611111111)

    # draw crown image and its data
    screen.blit(crownIcon_image, (WIDTH * 0.44, HEIGHT * 0.18))
    draw_text(f"{winScore}", pygame.font.Font(None, 35), WHITE, screen, WIDTH * 0.493, HEIGHT * 0.361)

    return play_button, settings_button, back_button, info_button


'''CLASSES '''
# text input class
class textInput:
    # x and y represent coordinates for positioning on a screen
    def __init__(self, x, y, width, height, font):
        # create a rectangle shape for the input field
        self.rect = pygame.Rect(x, y, width, height)
        # initial colour of input field
        self.color = GREY 
        # text within input field
        self.text = "" 
        # font used for input field text
        self.font = font 
        # rendered text surface
        self.text_surface = self.font.render(self.text, True, BLACK) 
        # checks to see if input box has been entered into
        self.active = True
    def handle_event(self, event):
        # quits in input screen
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        '''ERROR FIXED SOLUTION EXPLAINED'''
        # the problem is that it didn't register the key events since line 158 wasn't carried out.
        # also other issue was that the input fields instantiation were misplaced. 
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                # active state becomes true because input field has been clicked
                self.active = True
                self.color = BLACK
            else:
                # i.e. if the input field hasn't been clicked, active state remains false
                self.active = False
                self.color = GREY
        # checks if the user has pressed a key on their keyboard
        elif event.type == pygame.KEYDOWN:
            # checks if the key was pressed while the input field is active
            if self.active:
                # checks if user has pressed the backspace key on their keyboard
                if event.key == pygame.K_BACKSPACE:
                    # removes the last character upon pressing backspace key
                    self.text = self.text[:-1]
                else: 
                    # adds the typed character into the input field
                    self.text += event.unicode
            # render the updated text
            self.text_surface = self.font.render(self.text, True, BLACK)

    def update(self):
        width = max(200, self.text_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        # draws the text
        screen.blit(self.text_surface, (self.rect.x + 5, self.rect.y + 5)) 
        # draws the input box rectangle
        pygame.draw.rect(screen, self.color, self.rect, 2)

# draw the setup screen
def draw_setUp_screen(screen, title_font, button_font, WIDTH, HEIGHT, RED, WHITE):
    # title of the screen
    draw_text("Setup", title_font, BLACK, screen, WIDTH // 2, HEIGHT // 8 - 25)

    draw_text("Player Name:", pygame.font.Font(None, 45), BLACK, screen, WIDTH * 0.2510417, HEIGHT * 0.22222)
    draw_text("*top of screen*", pygame.font.Font(None, 35), BLACK, screen, WIDTH * 0.2510417, HEIGHT * 0.28)
    draw_text("Grab Key: A", pygame.font.Font(None, 45), RED, screen, WIDTH * 0.7271, HEIGHT * 0.22222)


    draw_text("Player Name:", pygame.font.Font(None, 45), BLACK, screen, WIDTH * 0.2510417, HEIGHT * 0.44)
    draw_text("*bottom of screen*", pygame.font.Font(None, 35), BLACK, screen, WIDTH * 0.2510417, HEIGHT * 0.50)
    draw_text("Grab Key: L", pygame.font.Font(None, 45), RED, screen, WIDTH * 0.7271, HEIGHT * 0.44)


    # submit button used for completion of assigning user names 
    submit_button = pygame.Rect(WIDTH * 0.33, HEIGHT * 0.65, WIDTH * 0.35, 75)
    # draws shape and text for the submit button
    pygame.draw.rect(screen, RED, submit_button)
    draw_text("Submit", button_font, WHITE, screen, WIDTH * 0.5, HEIGHT * 0.7)

    # displays back button
    back_button = screen.blit(backIcon_image, (10,10))

    return submit_button, back_button

class player():
    # constructor method
    def __init__(self, name, deck, score):
        self.__name = name
        self.__deck = deck
        self.__score = score
    
    # get methods
    def getName(self): # name getter
        return self.__name
    def getDeck(self): # deck getter
        return self.__deck
    def getDeckItem(self, index):
        return self.__deck[index]
    def getScore(self): # score getter
        return len(self.__deck)
    # set methods 
    def setName(self, newName): # name setter
        self.__name = newName
    def shuffleDeck(self, deck): # deck setter
        random.shuffle(deck)
    def appendDeck(self, newData): 
        self.__deck.append(newData)
    def popDeckItem(self, popIndex):
        self.__deck.pop(popIndex)


''' once score handling sorted, use this list:

[ # deck set from 1-12 repeating 4 times each for a total of 48 cards
    1, 1, 1, 1,
    2, 2, 2, 2,
    3, 3, 3, 3,
    4, 4, 4, 4,
    5, 5, 5, 5,
    6, 6, 6, 6,
    7, 7, 7, 7,
    8, 8, 8, 8,
    9, 9, 9, 9,
    10, 10, 10, 10,
    11, 11, 11, 11,
    12, 12, 12, 12]

'''

# instantiated player objects
playerOne = player("Player1", 
[ 
    1, 1, 
    2, 2, 
    3, 3, 
]
, 0)
playerTwo = player("Player2", 
[
    1, 1, 
    2, 2, 
    3, 3, 
]
, 0)

'''# test cases
# get methods
print(playerOne.getName())
print(playerOne.getDeck())
print(playerOne.getScore())
print(playerTwo.getName())
print(playerTwo.getDeck())
print(playerTwo.getScore())
# set method
playerOne.setName("John") # name test
print(playerOne.getName())
playerOne.appendDeck('21') # deck append test
print(playerOne.getDeck())
playerOne.shuffleDeck(playerOne.getDeck()) # deck shuffle test
print(playerOne.getDeck()) '''

# keeps track of the specific cards that have been flipped onto dashed box (discard pile)
discard_pile = []

# draws the match screen
def draw_match_screen(screen, title_font, button_font, WIDTH, HEIGHT, RED, WHITE):
    # center the totem in the middle of the screen
    totem_x = WIDTH // 2 - totem_Image.get_width() // 2
    totem_y = HEIGHT // 2 - totem_Image.get_height() // 2
    '''# test case
    print(totem_x, totem_y)'''

    screen.blit(totem_Image, (totem_x, totem_y))
    # place the first hand in the bottom right of the screen
    hand1_x = WIDTH - hand_Image.get_width() - 600
    hand1_y = HEIGHT - hand_Image.get_height() + 15
    screen.blit(hand_Image, (hand1_x, hand1_y))
    # place the second upside-down hand in the top right of the screen
    hand2_x = WIDTH - hand_Image.get_width() - 50
    hand2_y = -10
    screen.blit(pygame.transform.rotate(hand_Image, 180), (hand2_x, hand2_y))
    # place the first discard pile directly below the totem
    global discard1_x, discard1_y, discard2_x, discard2_y 
    discard1_x = totem_x - 50
    discard1_y = totem_y + totem_Image.get_height() - 50
    discard2_x = discard1_x
    discard2_y = totem_y + discardPile_image.get_height() - 475
    screen.blit(pygame.transform.rotate(discardPile_image, 90), (discard1_x, discard1_y))
    # place the second discard pile directly above the totem
    screen.blit(pygame.transform.rotate(discardPile_image, 90), (discard2_x, discard2_y))
    # place the first card directly underneath the first discard pile
    card1_x = discard1_x + 116.5
    card1_y = discard1_y + discardPile_image.get_height() - 140
    screen.blit(back_Card1, (card1_x, card1_y))
    # place the second upside-down card directly above the second discard pile
    card2_x = discard1_x + 116.5
    card2_y = discard2_y - 90
    screen.blit(pygame.transform.rotate(back_Card2, 180), (card2_x, card2_y))
    # place text beside player's decks and discard piles
    # data for player 1
    player1_nameBox = pygame.Rect(WIDTH * 0.25 - 85, -5, 120, 45)
    pygame.draw.rect(screen, RED, player1_nameBox)
    draw_text(f"{playerOne.getName()}", pygame.font.Font(None, 30), WHITE, screen, WIDTH * 0.25 - 30, 20)
    draw_text("Score", small_font, WHITE, screen, card2_x - 50, card2_y + 30)
    draw_text(f"{playerOne.getScore()}", small_font, WHITE, screen, card2_x - 50, card2_y + 50)
    # data for player 2
    player2_nameBox = pygame.Rect(WIDTH * 0.75 - 25, HEIGHT - 40, 120, 45)
    pygame.draw.rect(screen, RED, player2_nameBox)
    draw_text(f"{playerTwo.getName()}", pygame.font.Font(None, 30), WHITE, screen, WIDTH * 0.75 + 30, HEIGHT - 20)
    draw_text("Score", small_font, WHITE, screen, card1_x - 50, card1_y + 30)
    draw_text(f"{playerTwo.getScore()}", small_font, WHITE, screen, card1_x - 50, card1_y + 50)
    # discard pile total count
    draw_text("Discard Pile Total:", small_font, WHITE, screen, 80, HEIGHT // 2 - 85)
    if discard_pile == []:
        draw_text(f"{0}", small_font, WHITE, screen, 75, HEIGHT // 2 - 65)
    elif len(discard_pile) > 0:
        draw_text(f"{len(discard_pile)}", small_font, WHITE, screen, 75, HEIGHT // 2 - 65)

def draw_endgame_screen(screen, title_font, WIDTH, HEIGHT):
    screen.fill(LIGHTRED)
    draw_text("Game Over", title_font, BLACK, screen, WIDTH // 2, HEIGHT // 8)
    if playerOne.getScore() == 0:
        draw_text("{} Wins!".format(playerOne.getName()), title_font, GREEN, screen, WIDTH // 2, HEIGHT // 2)

    else:
        draw_text("{} Wins!".format(playerTwo.getName()), title_font, GREEN, screen, WIDTH // 2, HEIGHT // 2)

# variables used for game function
gameOn = False # boolean variable determines if game function is running
# where the core game begins and ends
def game(current_scrn):
    
    # time variables for duels and normal flips
    clock = pygame.time.Clock()
    round_start_time = None

    # boolean variable determines if game function runs or not
    gameOn = True
    # boolean variable determines if a deck is shuffled
    shuffle = False

    global show_numbers
    show_numbers = False
    

    # determines current card of player one
    playerone_currcard = 0
    # determines current card of player two
    playertwo_currcard = 0


    # determines who receives discard pile contents
    loser = 0

    # validates if deck has been shuffled
    if not shuffle:
        playerOne.shuffleDeck(playerOne.getDeck())
        playerTwo.shuffleDeck(playerTwo.getDeck())
        shuffle = True
    
    grabbed = False
    while True:

        screen.fill(LIGHTRED)
        draw_match_screen(screen, title_font, button_font, WIDTH, HEIGHT, RED, WHITE)
        

        ''' NOTE: THIS IS THE PROGRESS MADE WITH DISPLAYING MESSAGES TO PLAYERS, CONTINUE ANOTHER TIME
        the way it works is that you use the boolean variables to determine if a certain condition has been met.
        if you had simply drawn the message during the condition - it wouldo only run as long as you have pressed a key
        we don't want that, we want the message to be displayed for a certain amount of time and then disappear
        these variables will play a role in achieving that. then some conditions are done near the end of this second main loop
        which checks if conditions have been met and correspondingly ouputs a message
        # boolean variables check if certain conditions have been met
        # if so, a message is displayed
        normal_flip_player_one = False
        normal_flip_player_two = False
        duel_player_one = False
        duel_player_two = False'''
        # used for another purpose
        duel_player_one = False
        duel_player_two = False
        normal_flip_player_one = False
        normal_flip_player_two = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # checks if players have clicked a key event and if numbers should be shown
            if event.type == pygame.KEYDOWN and show_numbers:
                # duel check condition
                if playerone_currcard == playertwo_currcard:

                    # player one check
                    if event.key == pygame.K_a and not grabbed:
                        '''
                        # output
                        draw_text("{} won the duel!".format(playerOne.getName()), 
                        pygame.font.Font(None, 60), BLUE, screen, WIDTH // 2, HEIGHT // 2 )
                        # flag for displaying message result
                        duel_player_one = True'''
                        # display message
                        #if duel_player_one == False:
                        print("{} WON THE DUEL!".format(playerOne.getName()))
                        #    duel_player_one = True

                        # deck and discard pile updating
                        # add all cards in discard pile to loser's deck
                        (playerTwo.getDeck()).extend(discard_pile)
                        # empty discard pile as cards have been moved
                        discard_pile.clear()

                        grabbed = True
                        
                    # player two check
                    elif event.key == pygame.K_l and not grabbed:
                        '''
                        # output
                        draw_text("{} won the duel!".format(playerTwo.getName()), 
                        pygame.font.Font(None, 60), BLUE, screen, WIDTH // 2, HEIGHT // 2 )
                        # flag for displaying message result
                        duel_player_two = True'''

                        # display message   
                        #if duel_player_two == False:                     
                        print("{} WON THE DUEL!".format(playerTwo.getName()))
                         #   duel_player_two = True

                        # deck and discard pile updating
                        # add all cards in discard pile to loser's deck
                        (playerOne.getDeck()).extend(discard_pile)
                        # empty discard pile as cards have been moved
                        discard_pile.clear()

                    
                        grabbed = True
                        # player one is the loser of the duel
                        loser = 1
                    
                    
                
                # normal flip check if player wrongly pressed their allocated keys
                elif playerone_currcard != playertwo_currcard:
                    # player one check
                    
                    if event.key == pygame.K_a:
                        '''
                        # message
                        draw_text("{} misread the cards!".format(playerOne.getName()), 
                        pygame.font.Font(None, 60), BLUE, screen, WIDTH // 2 , HEIGHT // 2 )
                        # flag for displaying message result
                        normal_flip_player_one = True'''

                        # display message
                        if normal_flip_player_one == False:
                            print("{} MISREAD THE CARDS!".format(playerOne.getName()))
                            normal_flip_player_one = True


                        # deck and discard pile updated
                        (playerOne.getDeck()).extend(discard_pile)
                        discard_pile.clear()

                    # player two check
                    elif event.key == pygame.K_l:
                        '''
                        # message
                        draw_text("{} misread the cards!".format(playerTwo.getName()), 
                        pygame.font.Font(None, 60), BLUE, screen, WIDTH // 2, HEIGHT // 2 )
                        # flag for displaying message result
                        normal_flip_player_two = True'''

                        # display message
                        if normal_flip_player_two == False:
                            print("{} MISREAD THE CARDS!".format(playerTwo.getName()))
                            normal_flip_player_two = True

                        # deck updated
                        (playerTwo.getDeck()).extend(discard_pile)
                        discard_pile.clear()
                
        
        # start a new round
        if not show_numbers:
            playerone_currcard = random.choice(playerOne.getDeck())
            playertwo_currcard = random.choice(playerTwo.getDeck())
            round_start_time = time.time()
            show_numbers = True
            # boolean variable ensures cards are added to discard pile only once
            cards_added_to_discard = False
            grabbed = False
            # reset display boolean variables for next round
            '''
            duel_player_one = False
            duel_player_two = False
            normal_flip_player_one = False
            normal_flip_player_two = False'''

        # display numbers for 3 seconds
        if show_numbers:
            # displaying player one current card 
            draw_text(str(playerone_currcard), 
            pygame.font.Font(None, 100), (255, 0, 0), screen, discard1_x + 160, discard1_y + 100)
            # displaying player two current card
            draw_text(str(playertwo_currcard), 
            pygame.font.Font(None, 100), (255, 0, 0), screen, discard2_x + 160, discard2_y + 100)
        
            # updating discard pile and deck for both players
            if not cards_added_to_discard:
                discard_pile.append(str(playerone_currcard))
                discard_pile.append(str(playertwo_currcard))
                
            
                (playerOne.getDeck()).remove(playerone_currcard)
                
                
                (playerTwo.getDeck()).remove(playertwo_currcard)
                
                # so cards aren't added again
                cards_added_to_discard = True

            if time.time() - round_start_time > 3:
                show_numbers = False     

            '''elif time.time() - round_start_time < 3 and show_numbers: 
                if duel_player_one:
                    draw_text("{} won the duel!".format(playerOne.getName()), 
                        pygame.font.Font(None, 60), BLUE, screen, WIDTH // 2, HEIGHT // 2 )
                
                elif duel_player_two:
                    draw_text("{} won the duel!".format(playerTwo.getName()), 
                        pygame.font.Font(None, 60), BLUE, screen, WIDTH // 2, HEIGHT // 2 )
                        
                elif normal_flip_player_one:
                    draw_text("{} misread the cards!".format(playerOne.getName()), 
                        pygame.font.Font(None, 60), BLUE, screen, WIDTH // 2 , HEIGHT // 2 )
                        
                elif normal_flip_player_two:
                    draw_text("{} misread the cards!".format(playerTwo.getName()), 
                        pygame.font.Font(None, 60), BLUE, screen, WIDTH // 2, HEIGHT // 2 )
                        '''
        
        if playerOne.getScore() == "0":
            #current_scrn = "endgame"
            print("Game Over!")
            print("{} wins!".format(playerTwo.getName()))
            break
        elif playerTwo.getScore() == "0":
            print("Game Over!")
            print("{} wins!".format(playerOne.getName()))
            break
        pygame.display.flip()
        
        





    
    
    # use this at some point ESSENTIAL
    # if something blah blah:
    #   countdown_off = False

# variable used to determine current screen state
current_screen = "authentication"

# variables for countdown display
counter, text = 5, '5'

# initialises countdown
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1000)

# boolean variable which determines whether countdown is closed or left running
countdown_off = False


# input fields from setup screen
useroneName_inputfield = textInput(WIDTH * 0.396, HEIGHT * 0.209, 200, 40, button_font)
usertwoName_inputfield = textInput(WIDTH * 0.396, HEIGHT * 0.417, 200, 40, button_font)

# main loop
while True:
    # event handler
    for event in pygame.event.get():
        # quits program if user clicks the cross button
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        ''' WILL BE USED LATER: 
        for card in deck:
            count += 50
            screen.blit(card, (100 + count, 300 + count))'''

        # when mouse has been clicked, the next conditional statements are checked
        # you add another condition in line 375 so now it considers any keydown event - this fixed your input!
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
            # checks current screen
            if current_screen == "authentication":
                # draws authentication screen and the returned button details are assigned to the three buttons
                signin_button, signup_button, skip_button = draw_authentication_screen(screen, title_font, button_font, WIDTH, HEIGHT, LIGHTRED, RED, WHITE, BLACK)
                if signin_button.collidepoint(event.pos):
                    '''# test case
                    print("Sign in button clicked!") '''
                elif signup_button.collidepoint(event.pos):
                   ''' # test case
                    print("Sign up button clicked!")'''
                elif skip_button.collidepoint(event.pos):
                    # current_screen updated so that next iteration actually drawns main menu screen
                    current_screen = "mainMenu"
                    '''# test case
                    print("Skip button clicked!")'''
            # checks if skip button is clicked, if so, draws main menu screen
            elif current_screen == "mainMenu":
                # draws the main menu screen, using function and assigning returned values to the three buttons
                play_button, settings_button, back_button, info_button = draw_mainMenu_screen(screen, title_font, button_font, WIDTH, HEIGHT, LIGHTRED, RED, WHITE)
                # when back button is clicked, the current_screen is simply updated to 'authentication' so next iteration draws the according screen
                if back_button.collidepoint(event.pos):
                    current_screen = "authentication"
                    # test case 
                    print("Back button clicked!")
                elif settings_button.collidepoint(event.pos):
                    # test case
                    print("Settings button clicked!")
                elif info_button.collidepoint(event.pos):
                    # test case
                    print("Info button clicked!")
                elif play_button.collidepoint(event.pos):
                    current_screen = "setup"
                    # test case
                    print("Play button clicked!")
            elif current_screen == "setup":
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # assigns the returned variables from the function into the following variables
                submit_button, back_button = draw_setUp_screen(
                screen, title_font, button_font, WIDTH, HEIGHT, RED, WHITE)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if submit_button.collidepoint(event.pos):
                        current_screen = "match"
                        # test case
                        print("Submit button clicked!")
                        playerOne.setName(useroneName_inputfield.text)
                        playerTwo.setName(usertwoName_inputfield.text)

                    elif back_button.collidepoint(event.pos):
                        current_screen = "mainMenu"
                        # test case
                        print("Back button clicked!")

                # handle input event
                useroneName_inputfield.handle_event(event)
                usertwoName_inputfield.handle_event(event)

                # draw inputs
                useroneName_inputfield.update()
                usertwoName_inputfield.update()

                useroneName_inputfield.draw(screen)
                usertwoName_inputfield.draw(screen)

        # countdown timer 
        if event.type == pygame.USEREVENT and current_screen == "match":
            if countdown_off == False:
                if counter > 1:
                    counter -= 1
                    text = str(counter)
                else:
                    text = "Flip!"
                    # counter = 5 this sets off the recurring countdown use elsewhere like the game function
   
    clock.tick(60)


    screen.fill(LIGHTRED)
    

    # draws the screen according to the current_screen variable so that the screen keeps running for the user
    if current_screen == "authentication":
        draw_authentication_screen(screen, title_font, button_font, WIDTH, HEIGHT, LIGHTRED, RED, WHITE, BLACK)
    elif current_screen == "mainMenu":
        draw_mainMenu_screen(screen, title_font, button_font, WIDTH, HEIGHT, LIGHTRED, RED, WHITE)
    elif current_screen == "setup":
        draw_setUp_screen(screen, title_font, button_font, WIDTH, HEIGHT, RED, WHITE)
       
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        useroneName_inputfield.handle_event(event)
        usertwoName_inputfield.handle_event(event)
        
        useroneName_inputfield.update()
        usertwoName_inputfield.update()

        useroneName_inputfield.draw(screen)
        usertwoName_inputfield.draw(screen)

    elif current_screen == "match":
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        draw_match_screen(screen, title_font, button_font, WIDTH, HEIGHT, RED, WHITE)
        if countdown_off == False:
            screen.blit(countdown_font.render(text, True, (255, 255, 255)), 
            ((WIDTH // 2 - totem_Image.get_width() // 2) + 52, 
            (HEIGHT // 2 - totem_Image.get_height() // 2) + 18))
            
        if text == "Flip!" or countdown_off:
            # game function runs after end of countdown
            game(current_screen)
            countdown_off = True
        elif gameOn == True:
            game(current_screen)
            
    elif current_screen == "endgame":
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        draw_endgame_screen(screen, title_font, WIDTH, HEIGHT, RED, WHITE)
        



    pygame.display.flip()
    
    