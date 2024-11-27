import pygame

# Function for drawing text visible to the user
def draw_text(text, font, color, surface, xaxis, yaxis):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (xaxis, yaxis)
    surface.blit(textobj, textrect)


# Draw the authentication screen
def draw_authentication_screen(screen, title_font, button_font, WIDTH, HEIGHT, LIGHTRED, RED, WHITE, BLACK):
    screen.fill(LIGHTRED)
    draw_text("Authentication", title_font, BLACK, screen, WIDTH // 2, HEIGHT // 8)

    signin_button = pygame.Rect(WIDTH // 4, HEIGHT // 2 + 100, WIDTH // 2, 50)
    signup_button = pygame.Rect(WIDTH // 4, HEIGHT // 2, WIDTH // 2, 50)
    skip_button = pygame.Rect(WIDTH // 4, HEIGHT // 2 - 100, WIDTH // 2, 50)
    pygame.draw.rect(screen, RED, signin_button)
    pygame.draw.rect(screen, RED, signup_button)
    pygame.draw.rect(screen, RED, skip_button)
    
    draw_text("Sign up", button_font, WHITE, screen, WIDTH // 2, HEIGHT // 2 + 25)
    draw_text("Sign in", button_font, WHITE, screen, WIDTH // 2, HEIGHT // 2 + 125)
    draw_text("Skip", button_font, WHITE, screen, WIDTH // 2, HEIGHT // 2 - 75)
    
    return signin_button, signup_button, skip_button

# Draw the main menu screen
def draw_mainMenu_screen(screen, title_font, button_font, WIDTH, HEIGHT, LIGHTRED, RED, WHITE):
    screen.fill(LIGHTRED)
    # creating and drawing the buttons and their according text
    draw_text("Main Menu Screen", title_font, pygame.Color('black'), screen, WIDTH // 2, HEIGHT // 8)
    
    play_button = pygame.Rect(WIDTH // 4, HEIGHT // 2 + 100, WIDTH // 2, 50)
    options_button = pygame.Rect(WIDTH // 4, HEIGHT // 2, WIDTH // 2, 50)
    back_button = pygame.Rect(WIDTH // 4, HEIGHT // 2 - 100, WIDTH // 2, 50)
    pygame.draw.rect(screen, RED, play_button)
    pygame.draw.rect(screen, RED, options_button)
    pygame.draw.rect(screen, RED, back_button)
    
    draw_text("Play", button_font, WHITE, screen, WIDTH // 2, HEIGHT // 2 + 25)
    draw_text("Options", button_font, WHITE, screen, WIDTH // 2, HEIGHT // 2 + 125)
    draw_text("Back", button_font, WHITE, screen, WIDTH // 2, HEIGHT // 2 - 75)
    
    return play_button, options_button, back_button
