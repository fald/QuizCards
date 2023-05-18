import pygame
from config import *

pygame.init()

pygame.display.set_caption("QuizCards - A flashcard app")
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Process events
    for event in pygame.event.get():
        pass
        
if __name__ == "__main__":
    pass
