import pygame
import sys
from settings import Settings
from ship import Ship  # Add this line

class AlienInvasion:
    """Overall class to manage game assets and behavior"""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")
        # Set the background color.
        self.bg_color = (230, 230, 230)

        self.ship = Ship(self)  # Create an instance of the Ship class

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events.""" 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()     # Exit the program
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                    #Move the ship to the right.
                    self.ship.rect.x += 1
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
    
        pygame.display.flip()  # This line should be here



# Make a game instance and run the game.
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

