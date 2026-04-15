import pygame
import datetime

def prepare_hand(image):
    # This removes the white background from your hand image
    image.set_colorkey((255, 255, 255))
    
    rect = image.get_rect()
    # Double height surface so it rotates around the shoulder (the bottom)
    new_surf = pygame.Surface((rect.width, rect.height * 2), pygame.SRCALPHA)
    new_surf.blit(image, (0, 0))
    return new_surf

def get_angles():
    now = datetime.datetime.now()
    # Pygame rotates CCW, so we use negative. 6 degrees per tick.
    # Adjust by adding 90 if your hand points at 3 o'clock instead of 12.
    minute_angle = -now.minute * 6
    second_angle = -now.second * 6
    return minute_angle, second_angle

def rotate_hand(image, angle, center):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=center)
    return rotated_image, new_rect