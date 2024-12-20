import pygame
import sys
import random
import os

# initialize Pygame
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
title_font = pygame.font.Font(None, 74)
button_font = pygame.font.Font(None, 50)
small_font = pygame.font.Font(None, 24)

'''# back card
back_Card = deck[0]
# player deck dictionaries
player1 = {
    # ideas for later
    deck[0]: "1";

}'''

# variable used to determine current screen state
current_screen = "authentication"

# screens section

# loading images into pygame
# buttons
settingsIcon_image = pygame.transform.scale(pygame.image.load(r"img\icons\settings.png"), (50,50))
backIcon_image = pygame.transform.scale(pygame.image.load(r"img\icons\back.png"), (50,50))
crownIcon_image = pygame.transform.scale(pygame.image.load(r"img\icons\crown.png"), (100,100))
infoIcon_image = pygame.transform.scale(pygame.image.load(r"img\icons\info.png"), (49,49))
# game screen components
totem_Image = pygame.transform.scale(pygame.image.load(r"img\totem.png"), (204, 204))
logo_Image = pygame.transform.scale(pygame.image.load(r"img\logo.png"), (170,170))
hand_Image = pygame.transform.scale(pygame.image.load(r"img\hand.png"), (310,310))
defaultcard_Size = (210, 316)
discardPile_image = pygame.transform.scale(pygame.image.load(r"img\discard_Pile.png"), (defaultcard_Size))

# loading all cards into pygame
cards_Folder = r"img\cards"
deck = []

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


count = 0
'''# counter
count = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        for card in deck:
            count += 50
            screen.blit(card, (100 + count, 300 + count))
    pygame.display.flip()
'''

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
    settings_button = screen.blit(settingsIcon_image, (740, 10))
    back_button = screen.blit(backIcon_image, (10,10))
    info_button = screen.blit(infoIcon_image, (690,10))
    play_button = pygame.Rect(245, 400, WIDTH // 2.5, 75)
    pygame.draw.rect(screen, RED, play_button)
    draw_text("Play", pygame.font.Font(None, 55), WHITE, screen, 405, 440)

    # draw crown image and its data
    screen.blit(crownIcon_image, (350, 122.5))
    draw_text(f"{winScore}", pygame.font.Font(None, 35), WHITE, screen, 400, 260)

    return play_button, settings_button, back_button, info_button

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
        self.active = False
    
    def handle_event(self, event):
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
    draw_text("Setup", title_font, pygame.Color('black'), screen, WIDTH // 2, HEIGHT // 8)
    # initialises two input fields using textInput class
    #useroneName_inputfield = textInput(300, 200, 200, 40, button_font)
    #usertwoName_inputfield = textInput(300, 300, 200, 40, button_font)
    # submit button used for completion of assigning user names 
    submit_button = pygame.Rect(350, 400, 100, 50)
    # draws shape and text for the submit button
    pygame.draw.rect(screen, RED, submit_button)
    draw_text("Submit", button_font, WHITE, screen, 400, 425)
   # textInput.draw(useroneName_inputfield, screen)
    #textInput.draw(usertwoName_inputfield, screen)
    back_button = screen.blit(backIcon_image, (10,10))

    return submit_button, back_button

# draws the game screen
def draw_game_screen(screen, title_font, button_font, WIDTH, HEIGHT, RED, WHITE):
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
    discard1_x = totem_x - 50
    discard1_y = totem_y + totem_Image.get_height() - 50
    screen.blit(pygame.transform.rotate(discardPile_image, 90), (discard1_x, discard1_y))
    # place the second discard pile directly above the totem
    discard2_x = discard1_x
    discard2_y = totem_y + discardPile_image.get_height() - 475
    screen.blit(pygame.transform.rotate(discardPile_image, 90), (discard2_x, discard2_y))
    # place the first card directly underneath the first discard pile
    card1_x = discard1_x + 116.5
    card1_y = discard1_y + discardPile_image.get_height() - 140
    screen.blit(back_Card1, (card1_x, card1_y))
    # place the second upside-down card directly above the second discard pile
    card2_x = discard1_x + 116.5
    card2_y = discard2_y - 90
    screen.blit(pygame.transform.rotate(back_Card2, 180), (card2_x, card2_y))

'''
  # textIn# Define the new size for the card
new_card_width = 100  # Desired width
new_card_height = 150  # Desired height
# Scale the card image
scaled_card = pygame.transform.scale(deck[0], (new_card_width, new_card_height))

# Draw the scaled card
screen.blit(scaled_card, (WIDTH // 2, HEIGHT // 2))'''


# countdown initialising
countdown_timer = 3  # Starting countdown value
last_count_update = pygame.time.get_ticks()  # Tracks time of last update
countdown_active = True  # Toggle to start the countdown

# Draw countdown function
def draw_countdown(screen, countdown, font, color, WIDTH, HEIGHT):
    if countdown >= 0:
        draw_text(str(countdown), font, color, screen, 20, 20)

# main game loop
while True:
    # input fields from setup screen
    useroneName_inputfield = textInput(300, 200, 200, 40, button_font)
    usertwoName_inputfield = textInput(300, 300, 200, 40, button_font)
    # event handler
    for event in pygame.event.get():
        # quits program if user clicks the cross button
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        for card in deck:
            count += 50
            screen.blit(card, (100 + count, 300 + count))
        # when mouse has been clicked, the next conditional statements are checked
        if event.type == pygame.MOUSEBUTTONDOWN:
            # checks current screen
            if current_screen == "authentication":
                # draws authentication screen and the returned button details are assigned to the three buttons
                signin_button, signup_button, skip_button = draw_authentication_screen(screen, title_font, button_font, WIDTH, HEIGHT, LIGHTRED, RED, WHITE, BLACK)
                if signin_button.collidepoint(event.pos):
                    # test case
                    print("Sign in button clicked!") 
                elif signup_button.collidepoint(event.pos):
                    # test case
                    print("Sign up button clicked!")
                elif skip_button.collidepoint(event.pos):
                    # current_screen updated so that next iteration actually drawns main menu screen
                    current_screen = "mainMenu"
                    print("Skip button clicked!")
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
                useroneName_inputfield.handle_event(event)
                usertwoName_inputfield.handle_event(event)
                # assigns the returned variables from the function into the following variables
                submit_button, back_button = draw_setUp_screen(
                screen, title_font, button_font, WIDTH, HEIGHT, RED, WHITE)
                # handles user events for every input field
                #for field in input_fields:
                  #  field.handle_event(event)
                # checks if the submit button has been clicked
                if submit_button.collidepoint(event.pos):
                    current_screen = "game"
                    # test case
                    print("Submit button clicked!")
                elif back_button.collidepoint(event.pos):
                    current_screen = "mainMenu"
                    # test case
                    print("Back button clicked!")
            elif current_screen == "game":
                draw_game_screen(screen, title_font, button_font, WIDTH, HEIGHT, RED, WHITE)
                
                # Countdown logic
                if countdown_active:
                    current_time = pygame.time.get_ticks()
                    if current_time - last_count_update > 1000:  # Update every second
                        countdown_timer -= 1
                        last_count_update = current_time

                    # Display countdown
                    draw_countdown(screen, countdown_timer, title_font, RED, WIDTH, HEIGHT)

                    # End countdown when it reaches 0
                    if countdown_timer < 0:
                        countdown_active = False
                        print("Countdown finished! Start the game.")



    screen.fill(LIGHTRED)
    # draws the screen according to the current_screen variable so that the screen keeps running for the user
    if current_screen == "authentication":
        draw_authentication_screen(screen, title_font, button_font, WIDTH, HEIGHT, LIGHTRED, RED, WHITE, BLACK)
    elif current_screen == "mainMenu":
        draw_mainMenu_screen(screen, title_font, button_font, WIDTH, HEIGHT, LIGHTRED, RED, WHITE)
    elif current_screen == "setup":
        draw_setUp_screen(screen, title_font, button_font, WIDTH, HEIGHT, RED, WHITE)
        useroneName_inputfield.update()
        usertwoName_inputfield.update()
        useroneName_inputfield.draw(screen)
        usertwoName_inputfield.draw(screen)
    elif current_screen == "game":
        draw_game_screen(screen, title_font, button_font, WIDTH, HEIGHT, RED, WHITE)
    pygame.display.flip()