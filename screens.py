import pygame
import os

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
discardPile_image = pygame.transform.scale(pygame.image.load(r"img\discard_Pile.png"), (210.9375, 316.40625))

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
        card_img = pygame.transform.scale(pygame.image.load(card_path), (37.5, 56.25))
        # now the card has been loaded, it is appended to a deck list for later use
        deck.append(card_img)

# test case to see if cards have been correctly stored
pygame.init()
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

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

# color variables
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
LIGHTRED = (255, 182, 193)
GREEN = (0, 255, 0)
GREY = (200, 200, 200)

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

def draw_game_screen(screen, title_font, button_font, WIDTH, HEIGHT, RED, WHITE):
    #screen.blit(logo_Image, (WIDTH // 2, HEIGHT // 2))
    # draws the totem, which is used in duels
    screen.blit(totem_Image, (WIDTH // 2 - 100, HEIGHT // 2 - 90))
    # draws a hand, this is used to show the outcomes of duels 
    screen.blit(hand_Image, (WIDTH - 780, HEIGHT - 280))
    # draws the same hand but upside down, for player 2
    screen.blit(pygame.transform.rotate(hand_Image, 180), (WIDTH - 390, HEIGHT - 630))
    # cards which will be in use during game
    screen.blit(pygame.transform.rotate(discardPile_image, 90), (WIDTH // 2 - 120, HEIGHT // 2 - 30))
    screen.blit(deck[0], (WIDTH //2 , HEIGHT // 2))
    