import pygame
import sys
import random
import os
import screens

# initialize Pygame
pygame.init()

# screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jungle Speed")

# color variables
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
LIGHTRED = (255, 182, 193)
GREEN = (0, 255, 0)

# fonts
title_font = pygame.font.Font(None, 74)
button_font = pygame.font.Font(None, 50)



# variable used to determine current screen state
current_screen = "authentication"



# main game loop
while True:
    # event handler
    for event in pygame.event.get():
        # quits program if user clicks the cross button
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # when mouse has been clicked, the next conditional statements are checked
        if event.type == pygame.MOUSEBUTTONDOWN:
            # checks current screen
            if current_screen == "authentication":
                # draws authentication screen and the returned button details are assigned to the three buttons
                signin_button, signup_button, skip_button = screens.draw_authentication_screen(screen, title_font, button_font, WIDTH, HEIGHT, LIGHTRED, RED, WHITE, BLACK)
                if signin_button.collidepoint(event.pos):
                    # test case
                    print("Sign in button clicked!") 
                elif signup_button.collidepoint(event.pos):
                    # test case
                    print("Sign up button clicked!")
                elif skip_button.collidepoint(event.pos):
                    # current_screen updated so that next iteration actually drawns main menu screen
                    current_screen = "skip"
                    print("Skip button clicked!")
            # checks if skip button is clicked, if so, draws main menu screen
            elif current_screen == "skip":
                # draws the main menu screen, using function and assigning returned values to the three buttons
                play_button, settings_button, back_button, info_button = screens.draw_mainMenu_screen(screen, title_font, button_font, WIDTH, HEIGHT, LIGHTRED, RED, WHITE)
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
                else:
                    # test case
                    print("Play button clicked!")
                    # add the new screen here
                

    screen.fill(LIGHTRED)
    # draws the screen according to the current_screen variable so that the screen keepings running for the user
    if current_screen == "authentication":
        screens.draw_authentication_screen(screen, title_font, button_font, WIDTH, HEIGHT, LIGHTRED, RED, WHITE, BLACK)
    elif current_screen == "skip":
        screens.draw_mainMenu_screen(screen, title_font, button_font, WIDTH, HEIGHT, LIGHTRED, RED, WHITE)

    pygame.display.flip()