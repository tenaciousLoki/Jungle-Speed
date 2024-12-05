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
GREY = (200, 200, 200)

# fonts
title_font = pygame.font.Font(None, 74)
button_font = pygame.font.Font(None, 50)
small_font = pygame.font.Font(None, 24)


# variable used to determine current screen state
current_screen = "authentication"



# main game loop
while True:
    # input fields from setup screen
    useroneName_inputfield = screens.textInput(300, 200, 200, 40, button_font)
    usertwoName_inputfield = screens.textInput(300, 300, 200, 40, button_font)
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
                    current_screen = "mainMenu"
                    print("Skip button clicked!")
            # checks if skip button is clicked, if so, draws main menu screen
            elif current_screen == "mainMenu":
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
                elif play_button.collidepoint(event.pos):
                    current_screen = "setup"
                    # test case
                    print("Play button clicked!")
            elif current_screen == "setup":
                useroneName_inputfield.handle_event(event)
                usertwoName_inputfield.handle_event(event)
                # assigns the returned variables from the function into the following variables
                submit_button, back_button = screens.draw_setUp_screen(
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
                screens.draw_game_screen(screen, title_font, button_font, WIDTH, HEIGHT, RED, WHITE)
                

    screen.fill(LIGHTRED)
    # draws the screen according to the current_screen variable so that the screen keeps running for the user
    if current_screen == "authentication":
        screens.draw_authentication_screen(screen, title_font, button_font, WIDTH, HEIGHT, LIGHTRED, RED, WHITE, BLACK)
    elif current_screen == "mainMenu":
        screens.draw_mainMenu_screen(screen, title_font, button_font, WIDTH, HEIGHT, LIGHTRED, RED, WHITE)
    elif current_screen == "setup":
        screens.draw_setUp_screen(screen, title_font, button_font, WIDTH, HEIGHT, RED, WHITE)
        useroneName_inputfield.update()
        usertwoName_inputfield.update()
        useroneName_inputfield.draw(screen)
        usertwoName_inputfield.draw(screen)
    elif current_screen == "game":
        screens.draw_game_screen(screen, title_font, button_font, WIDTH, HEIGHT, RED, WHITE)
    pygame.display.flip()