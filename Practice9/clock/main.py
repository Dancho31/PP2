import pygame
import sys
import os
from clock import prepare_hand, get_angles, rotate_hand

pygame.init()

# 1. Setup Screen
SCREEN_SIZE = 800
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Mickey's Clock")
center_pos = (SCREEN_SIZE // 2, SCREEN_SIZE // 2)

# 2. Path Handling (Fixes most "File Not Found" errors)
base_path = os.path.dirname(__file__)
img_path = os.path.join(base_path, "images")

# 3. Load & Scale
try:
    bg = pygame.image.load(os.path.join(img_path, "mainclock.png")).convert()
    bg = pygame.transform.scale(bg, (SCREEN_SIZE, SCREEN_SIZE))
    
    hand_raw = pygame.image.load(os.path.join(img_path, "mickey_hand.png")).convert_alpha()
    # Scaled to fit comfortably in an 800px window
    hand_scaled = pygame.transform.scale(hand_raw, (180, 270))
except Exception as e:
    print(f"Error loading images: {e}")
    pygame.quit()
    sys.exit()

# 4. Prepare Hands
right_hand = prepare_hand(hand_scaled) # Minutes
left_hand = pygame.transform.flip(prepare_hand(hand_scaled), True, False) # Seconds

# 5. Loop
timer = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    min_angle, sec_angle = get_angles()

    screen.blit(bg, (0, 0))
    
    # Minutes (Right Hand)
    m_img, m_rect = rotate_hand(right_hand, min_angle, center_pos)
    screen.blit(m_img, m_rect)

    # Seconds (Left Hand)
    s_img, s_rect = rotate_hand(left_hand, sec_angle, center_pos)
    screen.blit(s_img, s_rect)

    pygame.display.flip()
    timer.tick(60)