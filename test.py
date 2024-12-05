import pygame
import sys

# Initialize Pygame
pygame.init()

# Define screen dimensions and colors
WIDTH, HEIGHT = 800, 600  # Screen width and height in pixels
WHITE = (255, 255, 255)   # RGB color code for white
BLACK = (0, 0, 0)         # RGB color code for black
GRAY = (200, 200, 200)    # RGB color code for gray
RED = (255, 0, 0)         # RGB color code for red

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Input Field Example')

# Font for rendering text
font = pygame.font.Font(None, 36)       # Standard font and size for normal text
small_font = pygame.font.Font(None, 24) # Smaller font for button text

# Text input class
class TextInput:
    def __init__(self, x, y, w, h, font):
        self.rect = pygame.Rect(x, y, w, h)  # Create a rectangle for the input field
        self.color = GRAY                     # Initial color of the input field
        self.text = ''                        # Text within the input field
        self.font = font                      # Font used for the input field text
        self.txt_surface = self.font.render(self.text, True, BLACK) # Rendered text surface
        self.active = False                   # State to check if input box is active

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active # Toggle the active state if the box is clicked
            else:
                self.active = False
            self.color = BLACK if self.active else GRAY # Change color based on state
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)           # Print the entered text on pressing enter
                    self.text = ''             # Clear the text field
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1] # Remove the last character on pressing backspace
                else:
                    self.text += event.unicode # Add the typed character to the text
                self.txt_surface = self.font.render(self.text, True, BLACK) # Render the updated text

    def update(self):
        width = max(200, self.txt_surface.get_width() + 10) # Adjust the box width based on text
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5)) # Draw the text
        pygame.draw.rect(screen, self.color, self.rect, 2) # Draw the input box rectangle

def draw_text(text, font, color, surface, x, y):
    text_surface = font.render(text, True, color) # Render the text
    surface.blit(text_surface, (x, y))            # Draw the text on the screen

# Main loop
def main():
    clock = pygame.time.Clock()       # Create a clock object to control the frame rate
    input_box = TextInput(300, 250, 200, 40, font) # Create an input box object
    submit_button = pygame.Rect(350, 320, 100, 50) # Create a rectangle for the submit button

    running = True
    while running:
        for event in pygame.event.get(): # Loop through the event queue
            if event.type == pygame.QUIT: # Check if the window close button is pressed
                pygame.quit()
                sys.exit()
            input_box.handle_event(event) # Pass events to the input box
            if event.type == pygame.MOUSEBUTTONDOWN:
                if submit_button.collidepoint(event.pos): # Check if the submit button is clicked
                    print("Submit button clicked with input:", input_box.text)
                    input_box.text = ''       # Clear the input field text
                    input_box.txt_surface = input_box.font.render(input_box.text, True, BLACK)

        input_box.update() # Update the input box

        screen.fill(WHITE) # Fill the screen with white color
        input_box.draw(screen) # Draw the input box
        pygame.draw.rect(screen, RED, submit_button) # Draw the submit button rectangle
        draw_text("Submit", small_font, WHITE, screen, submit_button.x + 10, submit_button.y + 10) # Draw the submit button text

        pygame.display.flip() # Update the display
        clock.tick(30)        # Maintain 30 frames per second

if __name__ == "__main__":
    main()
