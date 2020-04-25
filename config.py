import pygame
import ctypes

pygame.init()

user32 = ctypes.windll.user32
user32.SetProcessDPIAware()

screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

text_alfa = pygame.Surface((screen_width * 0.25, screen_height))
text_alfa.fill((150, 150, 150))
text_alfa.set_alpha(50)

FPS = 60
clock = pygame.time.Clock()