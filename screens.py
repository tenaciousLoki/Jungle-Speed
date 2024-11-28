import pygame
import os

# loading images into pygame
settingsIcon_image = pygame.transform.scale(pygame.image.load(r"img\icons\settings.png"), (50,50))
backIcon_image = pygame.transform.scale(pygame.image.load(r"img\icons\back.png"), (50,50))
crownIcon_image = pygame.transform.scale(pygame.image.load(r"img\icons\crown.png"), (100,100))

# function for drawing text visible to the user
def draw_text(text, font, color, surface, xaxis, yaxis):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (xaxis, yaxis)
    surface.blit(textobj, textrect)


# draw the authentication screen
def draw_authentication_screen(screen, title_font, button_font, WIDTH, HEIGHT, LIGHTRED, RED, WHITE, BLACK):
    screen.fill(LIGHTRED)
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
    # draw background colour 
    screen.fill(LIGHTRED)

    # draw header
    draw_text("Main Menu", title_font, pygame.Color('black'), screen, WIDTH // 2, HEIGHT // 8)

    # draw buttons and their contents to main menu screen
    settings_button = screen.blit(settingsIcon_image, (740, 10))
    back_button = screen.blit(backIcon_image, (10,10))
    play_button = pygame.Rect(245, 400, WIDTH // 2.5, 75)
    pygame.draw.rect(screen, RED, play_button)
    draw_text("Play", pygame.font.Font(None, 55), WHITE, screen, 405, 440)

    # draw crown image and its data
    screen.blit(crownIcon_image, (350, 122.5))
    draw_text(f"{winScore}", pygame.font.Font(None, 35), WHITE, screen, 400, 260)

    

    return play_button, settings_button, back_button

# draw game screen
def draw_game_screen(screen, title_font, button_font, WIDTH, HEIGHT, LIGHTRED, RED, WHITE):
    screen.fill(LIGHTRED)

