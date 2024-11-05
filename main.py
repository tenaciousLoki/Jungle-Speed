import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jungle Speed")

# Color variables
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
LIGHTRED = (255, 182, 193)
GREEN = (0, 255, 0)

# Fonts
title_font = pygame.font.Font(None, 74)
button_font = pygame.font.Font(None, 50)

# Function for drawing text visible to the user
def draw_text(text, font, color, surface, xaxis, yaxis):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (xaxis, yaxis)
    surface.blit(textobj, textrect)

# Main game loop
while True:
    
    # Fill background color white
    screen.fill(LIGHTRED)

    # Draw title
    draw_text("Authentication", title_font, BLACK, screen, WIDTH // 2, HEIGHT // 8)

    # TEST CASE
    # draw_text("Hello", title_font, BLUE, screen, 350, 100)

    # Draw buttons
    login_button = pygame.Rect(WIDTH // 4, HEIGHT // 2 + 100, WIDTH // 2, 50)
    signup_button = pygame.Rect(WIDTH // 4, HEIGHT // 2, WIDTH // 2, 50)
    pygame.draw.rect(screen, RED, login_button)
    pygame.draw.rect(screen, RED, signup_button)
    # Draw text
    draw_text("Sign up", button_font, WHITE, screen, WIDTH // 2, HEIGHT // 2 + 25)
    draw_text("Log in", button_font, WHITE, screen, WIDTH // 2, HEIGHT // 2 + 125)

    # Event handler
    for event in pygame.event.get():
        # Handles the quit event
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # If mouse has been clicked and within either of the buttons - then print
        if event.type == pygame.MOUSEBUTTONDOWN:
            if signup_button.collidepoint(event.pos):
                # Test case
                print("Sign up button clicked!")
            if login_button.collidepoint(event.pos):
                # Test case
                print("Log in button clicked!")
    # updates the entire screen with the latest drawn content                
    pygame.display.flip()

