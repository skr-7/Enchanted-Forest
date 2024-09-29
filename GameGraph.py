import pygame
import sys
import GameLibrary as GL
import os

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Enchanted Forest")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Fonts
font = pygame.font.Font(None, 32)
small_font = pygame.font.Font(None, 24)

# Load background image
background_image = pygame.image.load(os.path.join('forest.png'))
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Game state
game_state = "introduction"
history = []

# Function to update the game state and add to history
def update_game_state(new_state):
    global game_state
    game_state = new_state
    history.append(new_state)

# Pygame-based version of the make_choice function
def make_choice_pygame(option1, option2, result1, result2, next_step1=None, next_step2=None):
    button1 = pygame.Rect(50, 400, 300, 50)
    button2 = pygame.Rect(450, 400, 300, 50)
    
    choice_made = False
    while not choice_made:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button1.collidepoint(mouse_pos):
                    display_text(result1, 50, 500)
                    if next_step1:
                        update_game_state(next_step1.__name__)
                    choice_made = True
                elif button2.collidepoint(mouse_pos):
                    display_text(result2, 50, 500)
                    if next_step2:
                        update_game_state(next_step2.__name__)
                    choice_made = True
        
        screen.blit(background_image, (0, 0))
        display_text("You have two options:", 50, 350)
        pygame.draw.rect(screen, GRAY, button1)
        pygame.draw.rect(screen, GRAY, button2)
        display_text(option1, 60, 410)
        display_text(option2, 460, 410)
        pygame.display.flip()

# Function to display text
def display_text(text, x, y):
    lines = text.split('\n')
    for i, line in enumerate(lines):
        text_surface = small_font.render(line, True, BLACK)
        screen.blit(text_surface, (x, y + i * 30))

# Mapping the game state names to actual functions from GameLibrary
game_map = {
    "introduction": GL.introduction,
    "enter_forest": GL.enter_forest,
    "turn_back": GL.turn_back,
    "follow_the_path": GL.follow_the_path,
    "left_path": GL.left_path,
    "right_path": GL.right_path,
    "hermit_help": GL.hermit_help,
    "hermit_refuse": GL.hermit_refuse,
    "help_creatures": GL.help_creatures,
    "follow_the_voice": GL.follow_the_voice,
    "trust_the_figure": GL.trust_the_figure,
    "distrust_the_figure": GL.distrust_the_figure
}

# Main loop to control the flow of the game based on the state
def run_game():
    global game_state
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_state = "introduction"
                    history.clear()
        
        screen.blit(background_image, (0, 0))
        
        title = font.render("The Enchanted Forest", True, BLACK)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 20))
        
        welcome = small_font.render("Welcome to 'The Enchanted Forest'!", True, BLACK)
        screen.blit(welcome, (50, 80))
        
        state_text = small_font.render(f"Current game state: {game_state}", True, BLACK)
        screen.blit(state_text, (50, 120))
        
        if game_state in game_map:
            game_map[game_state]()
        else:
            display_text("Game over. Press 'R' to restart.", 50, 160)
        
        restart_text = small_font.render("Press 'R' to restart", True, BLACK)
        screen.blit(restart_text, (WIDTH - restart_text.get_width() - 20, HEIGHT - 40))
        
        pygame.display.flip()

    pygame.quit()

# Override the functions in GameLibrary to use the Pygame make_choice
GL.make_choice = make_choice_pygame

# Run the game
if __name__ == "__main__":
    run_game()
