import os

import pygame
from pygame.locals import *

from views.game_widow import GameWindow


class StartWindow:
    def __init__(self, config_path):
        self.config_path = config_path
        # Initialize Pygame
        pygame.init()

        # Set the window dimensions
        window_width = 1244
        window_height = 1016

        # Create the window
        window = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption("ai_drive")

        # Load the images
        map1 = pygame.image.load(os.path.join("Assets", "track.png"))
        map2 = pygame.image.load(os.path.join("Assets", "2.png"))
        map3 = pygame.image.load(os.path.join("Assets", "3.png"))
        logo = pygame.image.load(os.path.join("Assets", "logo.png"))

        # Set the initial image to None
        current_map = None

        # Create the buttons
        button_width = 200
        button_height = 100
        button_margin = 20

        button_total_width = 3 * button_width + 2 * button_margin
        button_start_x = (window_width - button_total_width) // 2
        button_start_y = (window_height - button_height) // 2

        button1_rect = pygame.Rect(
            button_start_x,
            button_start_y + 350,
            button_width,
            button_height,
        )
        button2_rect = pygame.Rect(
            button_start_x + button_width + button_margin,
            button_start_y + 350,
            button_width,
            button_height,
        )
        button3_rect = pygame.Rect(
            button_start_x + 2 * (button_width + button_margin),
            button_start_y + 350,
            button_width,
            button_height,
        )

        # Load the button images
        button_image1 = pygame.image.load(os.path.join("Assets", "button_image1.png"))
        button_image2 = pygame.image.load(os.path.join("Assets", "button_image2.png"))
        button_image3 = pygame.image.load(os.path.join("Assets", "button_image3.png"))

        # Calculate the logo position
        logo_rect = logo.get_rect(center=(window_width // 2, 250))

        # Run the game loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == MOUSEBUTTONDOWN:
                    # Check if a button was clicked
                    if button1_rect.collidepoint(event.pos):
                        current_map = map1
                    elif button2_rect.collidepoint(event.pos):
                        current_map = map2
                    elif button3_rect.collidepoint(event.pos):
                        current_map = map3

            # Clear the window with a gray background
            window.fill((200, 200, 200))

            # Display the logo at the top center
            window.blit(logo, logo_rect)

            # Draw the buttons
            window.blit(button_image1, button1_rect)
            window.blit(button_image2, button2_rect)
            window.blit(button_image3, button3_rect)

            # Display the current image
            if current_map:
                GameWindow(window, current_map, self.config_path)

            # Update the display
            pygame.display.update()

        # Quit Pygame
        pygame.quit()