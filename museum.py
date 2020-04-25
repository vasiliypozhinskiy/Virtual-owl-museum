import pygame
import os
import image_resize
import mainbuttons
import config as c

background = pygame.image.load("stairway.jpg")
background_rect = background.get_rect()

if background_rect.right > c.screen_width:
    image_resize.scale_image("stairway.jpg", "stairway_scaled.jpg", c.screen_width)
    background = pygame.image.load("stairway_scaled.jpg")
    background_rect = background.get_rect()
    os.remove("stairway_scaled.jpg")
if background_rect.bottom > c.screen_height:
    image_resize.scale_image("stairway.jpg", "stairway_scaled.jpg", None, c.screen_height)
    background = pygame.image.load("stairway_scaled.jpg")
    background_rect = background.get_rect()
    os.remove("stairway_scaled.jpg")

background_rect.centerx = c.screen_width // 2
background_rect.centery = c.screen_height // 2
run = True

buttons = []
exitbutton = mainbuttons.ExitButton((background_rect.right - 175, background_rect.bottom - 100, 150, 75))
antiquitybutton = mainbuttons.AntiquityButton((background_rect.left + 25, background_rect.top + 25, 300, 169))
middleagesbutton = mainbuttons.MiddleAgesButton((background_rect.left + 25, antiquitybutton.rect.bottom + 25 , 300, 298))
buttons.append(exitbutton)
buttons.append(antiquitybutton)
buttons.append(middleagesbutton)

while run:
    c.screen.fill((0, 0, 0))
    c.screen.blit(background, background_rect)

    for button in buttons:
        button.draw(c.screen)

    for i in pygame.event.get():
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_ESCAPE:
                run = False

        if i.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (True, False, False):
                mouse_position = pygame.mouse.get_pos()
                for button in buttons:
                    if button.rect.collidepoint(mouse_position):
                        button.clicked()
    c.clock.tick(c.FPS)
    pygame.display.update()

