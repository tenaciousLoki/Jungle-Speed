import pygame
import os

# loading images into pygame
settingsIcon_image = pygame.transform.scale(pygame.image.load(r"img\icons\settings.png"), (50,50))
backIcon_image = pygame.transform.scale(pygame.image.load(r"img\icons\back.png"), (50,50))
crownIcon_image = pygame.transform.scale(pygame.image.load(r"img\icons\crown.png"), (100,100))
infoIcon_image = pygame.transform.scale(pygame.image.load(r"img\icons\info.png"), (49,49))

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
    
    signup_button = pygame.Rect(WIDTH // 4, HEIGHT // 2 - 100, WIDTH // 2, 50) 
    signin_button = pygame.Rect(WIDTH // 4, HEIGHT // 2, WIDTH // 2, 50) 
    skip_button = pygame.Rect(WIDTH // 4, HEIGHT // 2 + 100, WIDTH // 2, 50) 

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
    draw_text("Jungle Speed", title_font, pygame.Color('black'), screen, WIDTH // 2, HEIGHT // 8)