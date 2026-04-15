import pygame
import sys
from player import MusicPlayer

pygame.init()

# Setup Screen
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Music Player")
font = pygame.font.SysFont("Arial", 24)

# Initialize Player (Points to your music folder)
player = MusicPlayer("music")

def draw_text(text, x, y, color=(255, 255, 255)):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

# Main Loop
while True:
    screen.fill((30, 30, 30)) # Dark Grey background
    
    # UI Instructions
    draw_text(f"Currently Playing: {player.get_current_track_name()}", 50, 100, (0, 255, 0))
    draw_text("P: Play | S: Stop | N: Next | B: Back | Q: Quit", 50, 200)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()
            elif event.key == pygame.K_s:
                player.stop()
            elif event.key == pygame.K_n:
                player.next_track()
            elif event.key == pygame.K_b:
                player.prev_track()
            elif event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

    pygame.display.flip()