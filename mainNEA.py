# card images found here: https://github.com/marcllopis/JungleSpeed-match
import pygame
import sys
import random
import os
import time


# initialise pygame
pygame.init()

# screen dimensions
WIDTH, HEIGHT = 960, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jungle Speed")

# colour variables
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
    
    # draw shapes of buttons
    signup_button = pygame.Rect(WIDTH // 4, HEIGHT // 2 - 100, WIDTH // 2, 50) 
    signin_button = pygame.Rect(WIDTH // 4, HEIGHT // 2, WIDTH // 2, 50) 
    skip_button = pygame.Rect(WIDTH // 4, HEIGHT // 2 + 100, WIDTH // 2, 50) 

    # draw the button and text
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
        # render text surface
        self.text_surface = self.font.render(self.text, True, BLACK) 
        # check to see if input box has been entered into
        self.active = True

    def validation(self, input_text):
        if input_text == "":
            return False
        elif len(input_text) <= 8:
            return True
        else:
            return False
        
    def handle_event(self, event):
        # quit in input screen
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                # active state becomes true because input field has been clicked
                self.active = True
                self.color = BLACK
            else:
                # if the input field hasn't been clicked, active state remains false
                self.active = False
                self.color = GREY
        # check if the user has pressed a key on their keyboard
        elif event.type == pygame.KEYDOWN:
            # check if the key was pressed while the input field is active
            if self.active:
                # check if user has pressed the backspace key on their keyboard
                if event.key == pygame.K_BACKSPACE:
                    # remove the last character upon pressing backspace key
                    self.text = self.text[:-1]
                else: 
                    # add the typed character into the input field
                    self.text += event.unicode
                
            # render the updated text
            self.text_surface = self.font.render(self.text, True, BLACK)
    # updates input text
    def update(self):
        width = max(200, self.text_surface.get_width() + 10)
        self.rect.w = width

    # draws input onto the screen
    def draw(self, screen):
        # draw the text
        screen.blit(self.text_surface, (self.rect.x + 5, self.rect.y + 5)) 
        # draw the input box rectangle
        pygame.draw.rect(screen, self.color, self.rect, 2)

# draw the setup screen
def draw_setUp_screen(screen, title_font, button_font, WIDTH, HEIGHT, RED, WHITE):
    # title of the screen
    draw_text("Setup", title_font, BLACK, screen, WIDTH // 2, HEIGHT // 8 - 25)

    # first player input 
    draw_text("Player Name:", pygame.font.Font(None, 45), BLACK, screen, WIDTH * 0.2510417, HEIGHT * 0.22222)
    draw_text("*top of screen*", pygame.font.Font(None, 35), BLACK, screen, WIDTH * 0.2510417, HEIGHT * 0.28)
    draw_text("Grab Key: A", pygame.font.Font(None, 45), RED, screen, WIDTH * 0.7271, HEIGHT * 0.22222)

    # second player input
    draw_text("Player Name:", pygame.font.Font(None, 45), BLACK, screen, WIDTH * 0.2510417, HEIGHT * 0.44)
    draw_text("*bottom of screen*", pygame.font.Font(None, 35), BLACK, screen, WIDTH * 0.2510417, HEIGHT * 0.50)
    draw_text("Grab Key: L", pygame.font.Font(None, 45), RED, screen, WIDTH * 0.7271, HEIGHT * 0.44)


    # submit button used for completion of assigning user names 
    submit_button = pygame.Rect(WIDTH * 0.33, HEIGHT * 0.65, WIDTH * 0.35, 75)
    # draw shape and text for the submit button
    pygame.draw.rect(screen, RED, submit_button)
    draw_text("Submit", button_font, WHITE, screen, WIDTH * 0.5, HEIGHT * 0.7)

    # display back button
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
    12, 12, 12, 12
]
, 0)
playerTwo = player("Player2", 
[
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
    12, 12, 12, 12
]
, 0)

# keep track of the specific cards that have been flipped onto dashed box (discard pile)
discard_pile = []

# draw the match screen
def draw_match_screen(screen, title_font, button_font, WIDTH, HEIGHT, RED, WHITE):
    # center the totem in the middle of the screen
    totem_x = WIDTH // 2 - totem_Image.get_width() // 2
    totem_y = HEIGHT // 2 - totem_Image.get_height() // 2

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

# boolean variable determines if game function is running
gameOn = False 
# where the core game begins and ends
def game():

    # time variables for duels and normal flips
    clock = pygame.time.Clock()
    round_start_time = None

    # boolean variables
    gameOn = True # determine if game function runs or not
    shuffle = False # determine if a deck is shuffled
    global show_numbers # determine whether to display numbers to the screen
    show_numbers = False
    # prevent duplicate outputs from grab keys
    duel_action_player_one = False
    duel_action_player_two = False
    normalflip_action_player_one = False
    normalflip_action_player_two = False
    
    # determine current card of player one
    playerone_currcard = 0
    # determine current card of player two
    playertwo_currcard = 0


    # validate if deck has been shuffled
    if not shuffle:
        playerOne.shuffleDeck(playerOne.getDeck())
        playerTwo.shuffleDeck(playerTwo.getDeck())
        shuffle = True
    
    while True:

        screen.fill(LIGHTRED)
        draw_match_screen(screen, title_font, button_font, WIDTH, HEIGHT, RED, WHITE)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # check if players have clicked a key event and if numbers should be shown
            if event.type == pygame.KEYDOWN and show_numbers:
                # duel check condition
                if playerone_currcard == playertwo_currcard:

                    # player one check
                    if event.key == pygame.K_a and not duel_action_player_one:
                        
                        # message
                        print("{} WON THE DUEL!".format(playerOne.getName()))
                       
                        # deck and discard pile updating
                        # add all cards in discard pile to loser's deck
                        (playerTwo.getDeck()).extend(discard_pile)
                        # empty discard pile as cards have been moved
                        discard_pile.clear()

                        duel_action_player_one = True

                    # player two check
                    elif event.key == pygame.K_l and not duel_action_player_two:
                       
                        # display message                                  
                        print("{} WON THE DUEL!".format(playerTwo.getName()))

                        # deck and discard pile updating
                        # add all cards in discard pile to loser's deck
                        (playerOne.getDeck()).extend(discard_pile)
                        # empty discard pile as cards have been moved
                        discard_pile.clear()

                        duel_action_player_two = True
                    
                    
                
                # normal flip check if player wrongly pressed their allocated keys
                elif playerone_currcard != playertwo_currcard:
                    # player one check                    
                    if event.key == pygame.K_a and not normalflip_action_player_one:
                        
                        # display message                        
                        print("{} MISREAD THE CARDS!".format(playerOne.getName()))
                            
                        # deck and discard pile updated
                        (playerOne.getDeck()).extend(discard_pile)
                        discard_pile.clear()

                        normalflip_action_player_one = True 

                    # player two check
                    elif event.key == pygame.K_l and not normalflip_action_player_two:                       

                        # display message                
                        print("{} MISREAD THE CARDS!".format(playerTwo.getName()))                        

                        # deck updated
                        (playerTwo.getDeck()).extend(discard_pile)
                        discard_pile.clear()

                        normalflip_action_player_two = True
            
            # start a new round
            if not show_numbers:
                playerone_currcard = random.choice(playerOne.getDeck())
                playertwo_currcard = random.choice(playerTwo.getDeck())
                round_start_time = time.time()
                show_numbers = True
                # boolean variable ensures cards are added to discard pile only once
                cards_added_to_discard = False
                

            # display numbers for 3 seconds
            if show_numbers:
                # display player one current card 
                draw_text(str(playerone_currcard), 
                pygame.font.Font(None, 100), (255, 0, 0), screen, discard1_x + 160, discard1_y + 100)
                # display player two current card
                draw_text(str(playertwo_currcard), 
                pygame.font.Font(None, 100), (255, 0, 0), screen, discard2_x + 160, discard2_y + 100)
            
                # update discard pile and deck for both players
                if not cards_added_to_discard:
                    discard_pile.append(str(playerone_currcard))
                    discard_pile.append(str(playertwo_currcard))
                    
                
                    (playerOne.getDeck()).remove(playerone_currcard)
                    
                    
                    (playerTwo.getDeck()).remove(playertwo_currcard)
                    
                    # so cards aren't added again
                    cards_added_to_discard = True

                if time.time() - round_start_time > 3:
                    show_numbers = False    
                    # reset boolean variables for next round
                    duel_action_player_one = False
                    duel_action_player_two = False
                    normalflip_action_player_one = False
                    normalflip_action_player_two = False 
                   
            
            pygame.display.flip()
            clock.tick(60)

        if playerOne.getScore() == 0:
            # to colour text, ANSI escape codes are used
            print(("\033[92;1mGame Over!\nResult: '{}' WINS THE GAME.\033[0m".format(playerOne.getName())))
            pygame.quit()
            sys.exit()
        elif playerTwo.getScore() == 0:
            print("\033[92;1mGame Over!\nResult: '{}' WINS THE GAME.\033[0m".format(playerTwo.getName()))
            pygame.quit()
            sys.exit()

# variables
current_screen = "authentication" # determine current screen state
counter, text = 5, '5' # countdown display

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
        # quit program if user clicks the cross button
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
            # check current screen
            if current_screen == "authentication":
                # draw authentication screen and the returned button details are assigned to the three buttons
                signin_button, signup_button, skip_button = draw_authentication_screen(screen, title_font, button_font, WIDTH, HEIGHT, LIGHTRED, RED, WHITE, BLACK)
                if signin_button.collidepoint(event.pos):
                    print("Sign in button clicked.") 
                elif signup_button.collidepoint(event.pos):
                    print("Sign up button clicked.")
                elif skip_button.collidepoint(event.pos):
                    # current_screen updated so that next iteration actually drawns main menu screen
                    current_screen = "mainMenu"
                    print("Skip button clicked.")
            # check if skip button is clicked, if so, draws main menu screen
            elif current_screen == "mainMenu":
                # draw the main menu screen, using function and assigning returned values to the three buttons
                play_button, settings_button, back_button, info_button = draw_mainMenu_screen(screen, title_font, button_font, WIDTH, HEIGHT, LIGHTRED, RED, WHITE)
                # when back button is clicked, the current_screen is simply updated to 'authentication' so next iteration draws the according screen
                if back_button.collidepoint(event.pos):
                    # change screen
                    current_screen = "authentication"
                    print("Back button clicked.")
                elif settings_button.collidepoint(event.pos):
                    print("Settings button clicked.")
                elif info_button.collidepoint(event.pos):
                    print("Info button clicked.")
                elif play_button.collidepoint(event.pos):
                    # change screen
                    current_screen = "setup"
                    print("Play button clicked.")

            elif current_screen == "setup":
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # assign the returned variables from the function into the following variables
                submit_button, back_button = draw_setUp_screen(
                screen, title_font, button_font, WIDTH, HEIGHT, RED, WHITE)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if submit_button.collidepoint(event.pos):                                                    
                        current_screen = "match"
                        print("Submit button clicked.")

                        if (useroneName_inputfield.validation(useroneName_inputfield.text) and 
                        usertwoName_inputfield.validation(usertwoName_inputfield.text)):
                            playerOne.setName(useroneName_inputfield.text)
                            playerTwo.setName(usertwoName_inputfield.text)
                        # quit program if input invalid 
                        else:
                            print("\033[31;1mInvalid input from player one and/or player two.\n" 
                            "Info: Cannot enter nothing and only enter less than or equal to 8 alphanumeric/non-alphanumeric characters."
                            "\nRestart game and try again.\033[0m"
                            )
                            pygame.quit()
                            sys.exit()
                    elif back_button.collidepoint(event.pos):
                        # change screen
                        current_screen = "mainMenu"
                        print("Back button clicked.")
                
                # handle input event every iteration
                useroneName_inputfield.handle_event(event)
                usertwoName_inputfield.handle_event(event)

                # update inputs every iteration
                useroneName_inputfield.update()
                usertwoName_inputfield.update()

                # draw inputs every iteration
                useroneName_inputfield.draw(screen)
                usertwoName_inputfield.draw(screen)

        # countdown timer 
        if event.type == pygame.USEREVENT and current_screen == "match":
            if countdown_off == False:
                # decrement timer 
                if counter > 1:
                    counter -= 1
                    text = str(counter)
                else:
                    text = "Flip!"
   
    clock.tick(60)


    screen.fill(LIGHTRED)
    

    # draw the screen according to the current_screen variable so that the screen keeps running for the user
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
            game()
            countdown_off = True
        elif gameOn == True:
            game()


    pygame.display.flip()
    
